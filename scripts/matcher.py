from spacy.matcher import PhraseMatcher, DependencyMatcher
import numpy as np
import pandas as pd
import typer
import en_core_web_lg
from pathlib import Path
from spacy.tokens import Doc, DocBin
from helper import read_lines_from_list
import json
import dependencymatch
import phrasematch


def main(
        value: str,
        input_path_csv: Path = typer.Argument(..., exists=True, dir_okay=False),
        input_path_docs: Path = typer.Argument(..., exists=True, dir_okay=False),
        input_path_json: Path = typer.Argument(..., exists=True, dir_okay=False),
        output_path_keys: Path = typer.Argument(..., dir_okay=False),
        output_path_texts: Path = typer.Argument(..., dir_okay=False)):
    with open(input_path_json) as f:
        terms_json = json.load(f)

    output_terms_json = {}
    output_terms_keys = {}
    i = 0

    while i < len(terms_json):
        print(value + " match " + "started test case num: " + str(i + 1))
        term = terms_json[str(i + 1)]
        nlp = en_core_web_lg.load()

        doc_bin = DocBin()
        doc_bin.from_disk(input_path_docs)

        docs = list(doc_bin.get_docs(nlp.vocab))
        if value == "phrase":
            matcher = phrasematch.phrasematch(term, nlp)
        else:
            matcher = dependencymatch.dependencymatch(term, nlp)
        values = []
        idx = 0

        dtype = [('title', object), ('up_votes', int), ('down_votes', int), ('over_18', bool), ('author', object)]
        l = []
        for doc in docs:

            matches = matcher(doc)
            for match in matches:

                if matches is not None:
                    l.append(idx + 1)

            idx += 1

        texts = read_lines_from_list(input_path_csv, l)

        for j in range(len(texts) - 1):
            values.append((texts[4][j], texts[2][j], texts[3][j], texts[5][j],
                           texts[6][j]))

        results = np.array(values, dtype=dtype)
        sorted_results = np.sort(results, order=["up_votes"])

        output_terms_json[str(i + 1)] = sorted_results[::-1].tolist()
        output_terms_keys[str(i + 1)] = l

        print(value + " match " + "finished test case num: " + str(i + 1))
        i += 1

    with open(output_path_keys, 'w') as f:
        json.dump(output_terms_keys, f)
        f.truncate()

    with open(output_path_texts, 'w') as f:
        json.dump(output_terms_json, f)
        f.truncate()
    print("Finished processing  " + value + " matches", "\n")


if __name__ == "__main__":
    typer.run(main)
