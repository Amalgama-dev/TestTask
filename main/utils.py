
from itertools import permutations

from nltk.tree import ParentedTree


class TreeManager:
    """
    Manager to parse, process and operate tree and its subtrees
    """

    # Options BY
    BY_PATTERN = "by_pattern"

    @staticmethod
    def get_subtrees_positions(
        tree: ParentedTree, by: str, label: str, pattern: str = None
    ) -> list[tuple[int]]:
        """
        Find subtrees in the tree, it can use different filters to search

        Now only 'pattern' option is implemented.
        Can be extended with other 'by' options.
        """

        subtrees_positions = []

        if by == TreeManager.BY_PATTERN:
            for subtree in tree.subtrees(lambda x: x.label() == label and len(x) > 1):
                subtree_labels = "".join([x.label() for x in subtree])
                if pattern.match(subtree_labels):
                    subtrees_positions.append(subtree.treeposition())

        return subtrees_positions

    @staticmethod
    def permutate_subtree_childrens(
        tree: ParentedTree,
        subtrees_positions: ParentedTree,
        children_label: str,
        limit: int = 20,
    ) -> list[ParentedTree]:
        """
        Go through all earlier found subtrees and permutate their specific children
        Children specification is provided as children_label
        """

        permutated_trees = []

        for subtree_position in subtrees_positions:
            subtree = tree[subtree_position]

            # Store elements that will be permutated
            elements_to_swap = tuple(
                element for element in subtree if element.label() == children_label
            )

            # Get current position of elements to filter this case
            elements_positions_in_subtree = tuple(
                element.treeposition() for element in elements_to_swap
            )

            # Permutate and create all possible combinations of elems positions
            permutated_elems = [
                x
                for x in permutations(elements_positions_in_subtree)
                if x != elements_positions_in_subtree
            ]

            # Modify copy of tree by permutated elements and add them to response
            for variant in permutated_elems[:limit]:
                for index, element in enumerate(elements_to_swap):
                    tree[variant[index]] = element.copy(deep=True)

                permutated_trees.append(str(tree).replace("\n", ""))

        return permutated_trees
