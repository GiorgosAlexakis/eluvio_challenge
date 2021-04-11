import typer
import en_core_web_lg
import pandas as pd
from pathlib import Path
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy
from spacy import displacy
import json


def main(
        value: str,
        input_path_docs: Path = typer.Argument(..., exists=True, dir_okay=False),
        input_path_keys: Path = typer.Argument(..., exists=True, dir_okay=False),
        output_path_page: Path = typer.Argument(..., dir_okay=True),

):
    with open(input_path_keys) as f:
        terms_json = json.load(f)
    nlp = en_core_web_lg.load()
    for idx in terms_json:

        terms = terms_json[idx]
        doc_bin = DocBin()
        doc_bin.from_disk(input_path_docs)
        all_docs = list(doc_bin.get_docs(nlp.vocab))
        desired_docs = []
        for term in terms:
            desired_docs.append(all_docs[term - 1])

        #options = {"ents": ["ORG"]}
        #html = displacy.render(desired_docs, style="ent", options=options, page=True)
        html = displacy.render(desired_docs, style="ent" , page=True)
        output_path = Path(str(output_path_page)+"/"+value+"render_"+idx+".html")
        output_path.open("w").write(html)


if __name__ == "__main__":
    typer.run(main)
