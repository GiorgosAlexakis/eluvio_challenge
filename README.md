# Eluvio Challenge
### Introduction 

We are being asked to "find a problem" to solve in a given Dataset from Eluvio. It contains small 
titles of users which mainly seem to be about conflicts,geopolitical news,wars etc. The dataset  also gives us other information too(if they are adults,their username,upvotes,downvotes,etc). I decided to use spaCy at first but I also used gensim for unsupervised clustering.

### spaCy
Considering Eluvio's very large datasets I had to first  find the best performing open-source library in order to maximize speed and efficiency at which we process our data.Spacy is a very popular library that provide us with what we need.As we can see from its benchmarks it perfoms very well.

![spacy-benchmark](https://user-images.githubusercontent.com/58263228/114309621-758dfc00-9af0-11eb-911e-f75281d2e5ba.png)





Spacy provides its users with pre-trained "pipelines" that can be installed as Python packages. 

![selected trained pipeline](https://user-images.githubusercontent.com/58263228/114309637-80489100-9af0-11eb-9bf4-721885a0c019.png)





Below is a summary of the features spaCy is providing:

![features overview](https://user-images.githubusercontent.com/58263228/114309647-863e7200-9af0-11eb-83b0-c8be00f20d89.png)



**Pretrained model used:** en_core_web_lg (lg indicating the large volume of text it was pretrained on)

**Pipeline**: ['tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer']


* **Tokenization**: Segments text into words,punctuations marks,etc
* **tok2vec**: Transforms tokens into vectors and saves them in Token.vector. The library generates word vectors using an algorithm called word2vec under the hood.
* **tagger**: Assigning word types to tokens,like verb or noun.
* **parser**: Assigns syntantic dependency labels,describing the relations between individual tokens,like subject or object.
* **ner**: labelling named "real-world" objects, like persons,companies or locations.
* **attribute_ruler**: manages rule-based mappings and exceptions for all token-level attributes
* **lemmatizer**: Assigns the base forms of words. For example, the lemma of “was” is “be”, and the lemma of “rats” is “rat”.


This project also uses spaCy "projects".SpaCy projects let you manage and share end-to-end spaCy workflows for different use cases and domains, and orchestrate training, packaging and serving your custom pipelines. It also makes it easy to integrate many other tools. SpaCy projects also make it easy to integrate with many other tools.https://spacy.io/usage/projects


<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Eluvio

 Eluvio's challenge in predictive modelling or analytical insights for business use cases  

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `preprocess` | Convert the data to spaCy's binary format and output the result in the corpus directory  |
| `phrasematch` | Runs some phrase matching examples from a json file(assets/phrasematches.json) |
| `dependencymatch` | Runs some dependency matching examples from a json file(assets/dependencymatches.json) |
| `VisualizePhraseResults` | It visualizes phrase matched results  |
| `VisualizeDependencyResults` | It visualizes dependency matched results  |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `all` | `preprocess` &rarr; `phrasematch` &rarr; `dependencymatch` &rarr; `VisualizePhraseResults` &rarr; `VisualizeDependencyResults` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| [`assets/Eluvio_DS_Challenge.csv`](assets/Eluvio_DS_Challenge.csv) | Local | CSV data given from Eluvio |
| [`assets/phrasematches.json`](assets/phrasematches.json) | Local | JSON-formatted input phrase matches for testing |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
### Rule-based matching

Since, we are interested in extracting information from the dataset it makes sense to use spaCy's **rule-matching**. Apart from being able to find keywords in the corpus file that gets produced during the preprocessing state. It also gives us the ability to **find relationships between tokens**, expand tokens to extract useful information. I will be testing some queries ,first some phrase matching rules then dependency matching rules. In the project I am saving the produced outputs in a json file, filtered based on upvotes where a hypothetical front-end developer could use. 

However, spaCy has integration with **visual tools** (displaCy) that allows you to see important information in the results. It can display **entity tags** ,for example it can tell you if a keyword is a country or an organization and it can also display the dependencies of a sentence. With that in mind, if someone for example wants to find what countries might be going into war ,we can query the data about war and then display entity tags only for countries. A dependency example that I tried was to find sentences that include the verb "sue" and its direct objective. If someone wants to go a step further we can even save these tokens (for example all the companies that are getting sued) by reading the value of the dictionary of the patterns with the  name of the dependency that corresponds to it.

Below are the phrase matcher test cases:

![phrasematchesjson](https://user-images.githubusercontent.com/58263228/114309656-93f3f780-9af0-11eb-8d30-63ef6ef32332.png)

#### Below are the dependency matcher test cases

![dependency matches](https://user-images.githubusercontent.com/58263228/114309692-b9810100-9af0-11eb-81df-d9385a46bb75.png)

Result when quering for barack obama:

![barack-all](https://user-images.githubusercontent.com/58263228/114309707-c9004a00-9af0-11eb-85a0-62c9f42e6ad8.png)

This query uses this configuration in scripts/visualize.py(it doesn't exclude any entity tags):
![dependency option render](https://user-images.githubusercontent.com/58263228/114312942-374b0980-9afd-11eb-80b8-1364a113a90c.png)

The "sue" example(we are only displaying organizations):

![dependency3render](https://user-images.githubusercontent.com/58263228/114312907-0b2f8880-9afd-11eb-905f-a7e16781e867.png)

It uses this configuration to display the results:

![1](https://user-images.githubusercontent.com/58263228/114313106-d6700100-9afd-11eb-8c26-4b7c88127621.png)

We can also,as mentioned before display the dependencies(test case of finding conflict and a preposition along with it):

![dependency-with-dep-render2](https://user-images.githubusercontent.com/58263228/114313156-03241880-9afe-11eb-9ea5-600f50798bdb.png)

![dependency option render](https://user-images.githubusercontent.com/58263228/114313147-facbdd80-9afd-11eb-811e-062fd0000652.png)

## Some more examples:


"Drug":
![phraserender6](https://user-images.githubusercontent.com/58263228/114313213-5007ef00-9afe-11eb-9d21-4d0d78e8c002.png)

"Banks"(displaying only organizations):
![phrase5](https://user-images.githubusercontent.com/58263228/114313228-5a29ed80-9afe-11eb-9aa4-d30504400e5f.png)

Obama query and displaying only countries:
![obama-countries](https://user-images.githubusercontent.com/58263228/114313245-70d04480-9afe-11eb-9413-ecdfd1b22191.png)

### Some other ideas include:
* find all mentions of "ministry" and determine which country's is mentioned for and its type (ex.the "French Ministry of Defense"), and then we add up the number of times it appears for each ministry.(ex.French Ministry of Defense appeared 10 times)
* protestors (british protestors,violent protestors etc) and then again find their frequencies
* find information that relates to money using the money tag of spacy
* find news about elections so then you predict future outcomes in that country. If a dictatorship falls in a region then it might be prosperous to open a business there
* CEO Names mentions
* We can also exclude results based on age
* Track news about someone or about a company for example throughout time.For example find all news related to Facebook and display them in a linear order.

However,there might be a better way to find related information like this. Writing queries like that requires us to monitor the dataset to come up with queries and we have to constantly write new queries if we want to find new information on new data.What better way is there? Unsupervised Clustering as you will see in notebook of Gensim.Spacy is still a very useful tool though if we wanted to write very specific queries based on a business' request. 
