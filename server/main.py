# -*- coding: utf-8 -*-
import synonyms

from pprint import pprint
import random
import re
import traceback

import nltk
from nltk.corpus import brown
from nltk import pos_tag
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import wordnet as wn
import en

import spacy
import gensim
from pycorenlp import StanfordCoreNLP


import change_voice

class Paraphrase():
	def __init__(self):

		self.text = text
		self.text = self.preprocess_text()
		self._sentences = sent_tokenize(self.text)
		self._words = [word_tokenize(sentence) for sentence in self._sentences]
		self._reference_text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
		self._pos_tagged_words = [nltk.pos_tag(sentence, tagset = '') for sentence in self._words]

		self._nlp = spacy.load('en_core_web_sm')
		self.debug = 1
		self.aggressive = False

		self.gensim_w2v_model = gensim.models.KeyedVectors.load_word2vec_format('./Models/GoogleNews-vectors-negative300.bin.gz', 
									binary=True, limit = 100000)


		self._max_index_syn = 3

	def _get_similar_phrase(self, phrase = []):
		
		if set(phrase).intersection(set(self.gensim_w2v_model.vocab)) == set(phrase):		
			syns = [(syn, score) for syn,score in self.gensim_w2v_model.most_similar(positive = phrase)
						if syn != phrase[0]]

		else:
			return ' '.join(word for word in phrase)

		if syns[0][1] < 0.5 or "'" in syn:
			return ' '.join(word for word in phrase)
		
		syn = syns[0][0]	
		return str(re.sub(r'\_', ' ', syn.lower()))
		

	def _aggressive_standards(self):
		if self.aggressive:
			self._max_index_syn = 5			


	def _print_debug(self, *arg):
		if self.debug:
			print ' '.join(x for x in arg)

	def preprocess_text(self):
		_text = self.text
		_text = re.sub(r'\’', "'", text)

		return _text.decode('utf-8')

	def get_all_synsets(self, word, pos=None):
	    for ss in wn.synsets(word):
	        for lemma in ss.lemma_names():
	            return (lemma, ss.name())


	def eligible_for_replacement(self, word, pos, next_pos = ''):
		if not re.search(r'[a-z]', word):
			return False

		if next_pos == 'IN':
			return False

		if word == 'so':
			return False

		if pos == 'CC':
			return False

		if re.search(r'[A-Z0-9\-\'\.]', word):
			return False

		if pos == 'NNS':
			return True

		if pos[:2] in ('JJ'): 		
			return True
		
		if pos in ('RB', 'RBR', 'RBS'): 		
			return True

		if pos in ('VBN', 'VBG'): 		
			return False

		if pos in ('UH'): 		
			return True

		return False


	def is_valid_syn(self, syn):
		try:
			if re.search(r'[^a-zA-Z]','', str(syn)):
				return False
			
			return True

		except:
			return False



	def get_replacement(self, word, pos, index_syn = 0):
		syn = word
		if not syn:
			return word

		if self.get_all_synsets(word = word):
			syn = self.get_all_synsets(word = word)[index_syn]

		if pos in ['NNS']:
			syn = en.noun.plural(syn)
		
		if pos == 'VBN':
			try:
				syn = en.verb.past_participle(syn)
			except:
				pass


		if word == syn and index_syn <= self._max_index_syn:
			index_syn += 1
			self.get_replacement(word = word, pos = pos, index_syn = index_syn)



		if not self.is_valid_syn(syn = syn):
			return word
		
		print word, syn

		return syn


	def format_text(self, text):
		text = re.sub(r'\s\.', '.', text)
		text = re.sub(r'\s\'', "'", text)
		text = re.sub(r'\s\,', ",", text)


		return text

		


	def paraphrase(self):
		text = self.text
		alt_text = ''
		for sentence in self._pos_tagged_words:
			alt_sent = ''
			for i,(word,pos) in enumerate(sentence):
				
				try:
					next_pos = sentence[i+1][1]
				except:
					#Reached last word of the sent
					next_pos = ''
				if self.eligible_for_replacement(word = word, pos = pos, next_pos = next_pos):	
					syn = self._get_similar_phrase(phrase = [word])
					syn = self.get_replacement(word = syn, pos = pos,)	
				else:
					syn = word
				
				alt_sent += ' ' + syn
				

			alt_text += ' ' + alt_sent[1].upper() + alt_sent[2:]
			#alt_text += change_voice.change_voice(sentence_active = alt_sent, _nlp = self._nlp )
		return self.format_text(text = alt_text)


text = open('input.txt').read()
p = Paraphrase()
p.text = text
print(p.paraphrase())