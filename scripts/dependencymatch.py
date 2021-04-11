from spacy.matcher import PhraseMatcher, DependencyMatcher


def dependencymatch(term, nlp):
    matcher = DependencyMatcher(nlp.vocab)
    matcher.add("dependency", [term])
    return matcher
