import requests
from openai import OpenAI
import io,sys
import os


## Simple client to reformat sparql query results in natural language 
## This exercise is a baseline and absolutely needs to be improved to achieve better performances.
os.environ['OPENAI_API_KEY'] = "paste api key here"

client = OpenAI()


def readFile(file):
    text = ""
    with io.open(file,'r',encoding='utf8') as f:
        text = f.read()
    return text


## lemma to be analysed
inputWord = "admirator"


## LiLa endpoint URL
url = 'https://lila-erc.eu/sparql/lila_knowledge_base/sparql'


## read example query 1
params = {'query': readFile("example_query1.txt"), 
"format" : "json"}
x = requests.post(url, data=params)
firstExample = x.text

## read example query 2
params = {'query': readFile("example_query2.txt"), 
"format" : "json"}
x = requests.post(url, data=params)
secondExample = x.text


## now a new query is submitted with the word I want to analyze
params = {'query': '''
PREFIX lila: <http://lila-erc.eu/ontologies/lila/>
PREFIX lime: <http://www.w3.org/ns/lemon/lime#>
PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?l ?p ?v (GROUP_CONCAT(DISTINCT ?varLabel ;separator=", ") as ?varLabels) ?definition where {
  ?l rdfs:label "'''+inputWord+'''".
  ?l  ?p ?v;
      dcterms:isPartOf <http://lila-erc.eu/data/id/lemma/LemmaBank>.
  optional {
    <http://lila-erc.eu/data/lexicalResources/LewisShort/Lexicon> lime:entry ?le.
    ?le ontolex:canonicalForm ?l;
        ontolex:sense ?sense.
    ?sense <http://www.w3.org/2004/02/skos#definition> ?definition.
  }
  optional{
  	?l lila:lemmaVariant ?var.
    ?var rdfs:label ?varLabel.
  }
} group by ?l ?p ?v ?definition
''', 
"format" : "json"}
x = requests.post(url, data=params)
toBeProcessed = x.text


## read LiLa OWL
lilaOntology = readFile("lila.owl")


print("Running llm...")


## example of few-shot promt : 
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Given the following ontology in OWL format:"},
            {"role": "user", "content": lilaOntology},
            {"role": "user", "content": "generate a standard vocabulary entry like the following:"},
            {"role": "user", "content": """permissio ["per-";"-(t)io(n)"] (permissio); third declension noun with gen pl in –um/-ium. 
In partic., leave , permission
In gen., a giving up , yielding , ceding to another's will and pleasure; an unconditional turrender
A rhet. figure, in which a thing is committed to the decision of one's opponent, permission
"""},
            {"role": "user", "content": "put square brackets only around prefixes and suffixes such as ""per-"", ""-(t)io(n)"", skip notes. Do not add anything else."},
            {"role": "user", "content": "using the result of the following SPARQL query: "},
            {"role": "user", "content": "query result: " + firstExample},
            {"role": "user", "content": "continue generating entries for the results of the following queries"},
            {"role": "user", "content":  "query result: " +secondExample},
            {"role": "assistant", "content": """exsequiae noun, feminine (exsequiae, exequiae): first declension noun; also as: exsequium
A funeral procession , funeral obsequies
Transf. , in late Lat., for reliquiae, the earthly remains , relics
"""},
           
            {"role": "user", "content":  "query result: " + toBeProcessed},
              ],
    temperature = 0.05,
    top_p = 1, 
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")