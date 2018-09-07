import synonyms
from nltk.corpus import wordnet as wn
from nltk import word_tokenize, sent_tokenize

import random
import re
import traceback

from nltk.corpus import brown
from nltk import pos_tag
import nltk


class Paraphrase():
	def __init__(self):
		self.text = text
		self._sentences = sent_tokenize(self.text)
		self._words = [word_tokenize(sentence) for sentence in self._sentences]
		self._reference_text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
		self._pos_tagged_words = [nltk.pos_tag(sentence) for sentence in self._words]


	def get_all_synsets(self, word, pos=None):
	    for ss in wn.synsets(word):
	        for lemma in ss.lemma_names():
	            return (lemma, ss.name())


	def eligible_for_replacement(self, word, pos):
		#tagged_sent = [pos_tag(sent) for sent in sentences]
		if pos == 'NN':
			return True
		if pos in ('VBP', 'JJ', 'VBD'): 		
			return True
		return False


	def is_valid_syn(self, syn):
		if '_' in syn:
			return False
		return True

	def get_replacement(self, word):
		syn = word
		if self.get_all_synsets(word = word):
			syn = self.get_all_synsets(word = word)[0]

		if not self.is_valid_syn(syn = syn):
			return word
		return syn

	def paraphrase(self):
		text = self.text

		alt_text = ''
		for sentence in self._pos_tagged_words:
			for word,pos in sentence:
				if self.eligible_for_replacement(word, pos):
					
					syn = self.get_replacement(word = word)
				else:
					syn = word
				alt_text += ' ' + syn

		return alt_text

text = open('input.txt').read()
p = Paraphrase()
p.text = text
print p._pos_tagged_words
print(p.paraphrase())
