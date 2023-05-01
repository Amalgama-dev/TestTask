<h2 align="center">The project was developed in Python using the Django REST and NLTK libraries.</h2>
<h2 align="center" >Project goal</h2>
<p>Create API that accepts a syntax tree and returns paraphrased versions.</p>
<h2 align="center">Quick start</h2>
<p>Create an empty folder and copy the project with command</p>
<pre lang="no-highlight">
<code>git clone https://github.com/Amalgama-dev/TestTask.git</code>
</pre>
<p>After we run the project through docker using the commands</p>
<pre lang="no-highlight">
<code>sudo docker-compose build </code>
</pre>
<pre lang="no-highlight">
<code>sudo docker-compose up</code>
</pre>
<h2 align="center">How to use</h2>
<p>To use go to the browser and in the search bar enter the query</p>
<p>
<strong>localhost:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )&limit=20</strong>
</p> 
<p>tree: syntax tree in the form of a line</p> 
<p>limit: maximum number of rephrasing tests, optional parameter, standard value = 20</p>

