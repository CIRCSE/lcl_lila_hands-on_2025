# lcl_lila_hands-on_2025
LCL 20250 - LiLa hands-on session 
## Exercise:

Create a mock dictionary entry, using the data modelled according to the Linked Open Data and turning it into Natural Language, using the generative power of LLMs.


From this mess:
|lemma                                  |property		   |value                                |definition                           |
|---------------------------------------|------------------|-------------------------------------|-------------------------------------|
|http://lila-erc.eu/data/id/lemma/117081|lila:hasPOS       |lila:noun                            |A rhet. figure, in which a thi...... |
|http://lila-erc.eu/data/id/lemma/117081|lila:hasBase      |http://lila-erc.eu/data/id/base/116  |In partic., leave , permission       |
|http://lila-erc.eu/data/id/lemma/117081|lila:hasPrefix    |http://lila-erc.eu/data/id/prefix/14 |In partic., leave , permission       |
|http://lila-erc.eu/data/id/lemma/117081|rdfs:label        |permissio                            |In gen., a giving up , yielding..... |
|http://lila-erc.eu/data/id/lemma/117081|ontolex_writtenRep|permissio                            |A rhet. figure, in which a thing ... |
|http://lila-erc.eu/data/id/lemma/117081|lila:hasGender    |lila:feminine                        |In gen., a giving up , yielding..... |
|http://lila-erc.eu/data/id/lemma/117081|lila:hasPOS       |lila:noun                            |In partic., leave , permission       |
|http://lila-erc.eu/data/id/lemma/117081|lila:hasSuffix    |http://lila-erc.eu/data/id/suffix/2  |A rhet. figure, in which a thing.... |

To this:

*permissio noun, feminine [per-; -io(n)] (permissio): third declension noun with genitive plural in –um/-ium.  
In particular, leave, permission.  
In general, a giving up, yielding, ceding to another's will and pleasure; an unconditional surrender.  
A rhetorical figure, in which a thing is committed to the decision of one's opponent, permission.*


## Requirements 

- Python 3
- An editor to write code (Visual Studio Code suggested)

## Steps:

- gather materials
  - load LiLa OWL to *instruct* the LLM
  - get the results of the example queries by quering the lila endpoint
- combining them in order to prompting the LLM
- check the results


## Ingredients:

LiLa Ontology OWL (Also in this repo): [https://raw.githubusercontent.com/CIRCSE/LiLaOntologies/refs/heads/main/lila.owl](https://raw.githubusercontent.com/CIRCSE/LiLaOntologies/refs/heads/main/lila.owl)

LiLa SPARQL Endpoint: [https://lila-erc.eu/sparql/lila_knowledge_base/sparql](https://lila-erc.eu/sparql/lila_knowledge_base/sparql)

Python modules : ```requests, openai```

example queries (in this repository)



## Hint:

to query a triplestore, use Python’s requests module and make a POST request to the endpoint, passing the parameters with the data argument.  
The most suitable response format for the endpoint is json.  

```
params = {query': a query', "format": "json"}
x = requests.post(url, data=params)}
```

## Documentation 

OpenAI API Documentation : https://platform.openai.com/docs/quickstart


## API Key:


