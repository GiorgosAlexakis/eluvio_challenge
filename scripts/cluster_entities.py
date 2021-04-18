from pathlib import Path

import en_core_web_lg
import pandas as pd
import typer
from spacy.tokens import DocBin
from textblob import TextBlob


class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""

    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

    def __iadd__(self, some_value):
        return some_value


def main(
        input_path_docs: Path = typer.Argument(..., exists=True, dir_okay=False),
        output_path_pages: Path = typer.Argument(..., dir_okay=True),
):
    nlp = en_core_web_lg.load()
    vocab = nlp.vocab

    doc_bin = DocBin()
    doc_bin.from_disk(input_path_docs)
    docs = list(doc_bin.get_docs(nlp.vocab))

    dict = AutoVivification()

    """
    supported ent types: 
    CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
    
    Let's try EVENT,FAC,GPE,LAW,LOC,ORG,PERSON,PRODUCT


    """
    ent_types = ['EVENT', 'FAC', 'GPE', 'LAW', 'LOC', 'ORG', 'PERSON', 'PRODUCT']
    # INITIALIZE
    for doc in docs:
        for e in doc.ents:
            if e.label_ in ent_types:
                dict[e.label_][e.text]['times mentioned'] = 0
                dict[e.label_][e.text]['Neutral sentiment posts'] = 0
                dict[e.label_][e.text]['Positive sentiment posts'] = 0
                dict[e.label_][e.text]['Negative sentiment posts'] = 0

    for doc in docs:
        blob = TextBlob(doc.text)
        polarity = blob.sentiment_assessments.polarity

        for e in doc.ents:
            if e.label_ in ent_types:
                dict[e.label_][e.text]['times mentioned'] += 1

                if polarity == 0:

                    dict[e.label_][e.text]['Neutral sentiment posts'] += 1

                elif polarity > 0:

                    dict[e.label_][e.text]['Positive sentiment posts'] += 1

                else:

                    dict[e.label_][e.text]['Negative sentiment posts'] += 1

    for term in dict:
        df = pd.DataFrame(dict[term]).transpose()
        df = df.sort_values(by=['times mentioned'], ascending=False)

        html = df.to_html()
        output_path = Path(str(output_path_pages) + "/" + term + "_render_" + ".html")
        output_path.open("w").write(html)


if __name__ == "__main__":
    typer.run(main)
