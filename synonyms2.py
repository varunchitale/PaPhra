from nltk.corpus import wordnet as wn

for ss in wn.synsets('small'):
	print(ss.name(), ss.lemma_names())


