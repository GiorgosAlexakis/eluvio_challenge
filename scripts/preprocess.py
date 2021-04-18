import typer
import en_core_web_lg
import pandas as pd
from pathlib import Path
from spacytextblob.spacytextblob import SpacyTextBlob
from spacy.kb import KnowledgeBase
from spacy.util import get_words_and_spaces
from spacy.tokens import Doc, DocBin
from spacy.vocab import Vocab

def main(
        input_path: Path = typer.Argument(..., exists=True, dir_okay=False),
        output_path: Path = typer.Argument(..., dir_okay=False),
):
    nlp = en_core_web_lg.load()
    nlp.add_pipe('spacytextblob')
    doc_bin = DocBin()
    texts = pd.read_csv(input_path)
    for doc in nlp.pipe(texts["title"], n_process=8, batch_size=1000):
        doc_bin.add(doc)


    doc_bin.to_disk(output_path)
    print(f"Processed {len(doc_bin)} documents: {output_path.name}")


if __name__ == "__main__":
    typer.run(main)
