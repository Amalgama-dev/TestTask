import re

from rest_framework.response import Response
from nltk.tree import ParentedTree
from rest_framework.views import APIView
from django.http.response import JsonResponse

from main.utils import TreeManager


class ParaphraseView(APIView):
    def get(self, request):
        """
        Process GET request with provided arguments and paraphrase a sentence
        Return JsonResponse with paraphrased sentences
        """
        # Assign GET arguments
        tree_str = str(request.GET.get("tree", None))
        limit = int(request.GET.get("limit", 20))

        # Return error if tree was not provided
        if not tree_str:
            data = {"error": "You must specify tree"}
            return JsonResponse(status=400, data=data)

        # Pattern to check if subtree childrens are valid (Only NP separated by comma or CC)
        subtree_pattern = re.compile(r"^(NP(?:,|CC))+NP$")
        response = {"paraphrases": []}
        tree = ParentedTree.fromstring(tree_str)

        # Retrieve needed subtrees positions
        subtrees_to_modify_positions = TreeManager.get_subtrees_positions(
            tree=tree,
            by=TreeManager.BY_PATTERN,
            pattern=subtree_pattern,
            label="NP",
        )

        # Permutate subtrees
        paraphrases = TreeManager.permutate_subtree_childrens(
            tree=tree.copy(deep=True),
            subtrees_positions=subtrees_to_modify_positions,
            children_label="NP",
            limit=limit,
        )

        response['paraphrases'] = [{'tree': x} for x in paraphrases]
        # Return paraphrased sentences
        return Response(status=200, data=response)
