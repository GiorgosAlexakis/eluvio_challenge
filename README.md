fefe
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
