import typer
import en_core_web_lg
import pandas as pd
from pathlib import Path
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
import spacy


def main(
        input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
        output_path: Path = typer.Argument(..., dir_okay=False),
):
    nlp = en_core_web_lg.load()

    doc_bin = DocBin()
    texts = pd.read_csv(input_path)[:10000]
    for doc in nlp.pipe(texts["title"], n_process=6):
        doc_bin.add(doc)

    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
