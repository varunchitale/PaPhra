from nltk.corpus import wordnet as wn


def get_all_synsets(word, pos=None):
    for ss in wn.synsets(word):
        for lemma in ss.lemma_names():
            yield (lemma, ss.name())


def get_all_hyponyms(word, pos=None):
    for ss in wn.synsets(word, pos=pos):
            for hyp in ss.hyponyms():
                for lemma in hyp.lemma_names():
                    yield (lemma, hyp.name())


def get_all_similar_tos(word, pos=None):
    for ss in wn.synsets(word):
            for sim in ss.similar_tos():
                for lemma in sim.lemma_names():
                    yield (lemma, sim.name())


def get_all_antonyms(word, pos=None):
    for ss in wn.synsets(word, pos=None):
        for sslema in ss.lemmas():
            for antlemma in sslema.antonyms():
                    yield (antlemma.name(), antlemma.synset().name())


def get_all_also_sees(word, pos=None):
        for ss in wn.synsets(word):
            for also in ss.also_sees():
                for lemma in also.lemma_names():
                    yield (lemma, also.name())


def get_all_synonyms(word, pos=None):
    for x in get_all_synsets(word, pos):
        yield (x[0], x[1], 'ss')
    for x in get_all_hyponyms(word, pos):
        yield (x[0], x[1], 'hyp')
    for x in get_all_similar_tos(word, pos):
        yield (x[0], x[1], 'sim')
    for x in get_all_antonyms(word, pos):
        yield (x[0], x[1], 'ant')
    for x in get_all_also_sees(word, pos):
        yield (x[0], x[1], 'also')
