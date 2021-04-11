from spacy.matcher import PhraseMatcher


def phrasematch(term, nlp):
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(text) for text in term]
    matcher.add("TerminologyList", patterns)
    return matcher
