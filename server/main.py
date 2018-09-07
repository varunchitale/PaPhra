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

from pycorenlp import StanfordCoreNLP


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


		self._max_index_syn = 3

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


	def eligible_for_replacement(self, word, pos, next_pos):
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
			return True

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
					syn = self.get_replacement(word = word, pos = pos,)	
					
				else:
					syn = word
				
				alt_sent += ' ' + syn
			
			
			alt_text += ' ' + alt_sent[1].upper() + alt_sent[2:]
			#alt_text = self._change_voice(sentence_active = alt_sent)
		return self.format_text(text = alt_text)

	def _change_voice(self, sentence_active):

		doc = self._nlp(sentence_active)
		
		if not set(['nsubj', 'ROOT', 'dobj']).intersection([token.dep_ for token in doc]) == set(['nsubj', 'ROOT', 'dobj']):
			return sentence_active
		
		temp_sentence = []

		root_token = [(token.text, token.dep_) for token in doc if token.dep_ in  ('nsubj', 'aux', 'ROOT', 'dobj')]
		
		for word, dep in root_token:
			if dep == 'dobj':
				for item in doc.noun_chunks:
					if re.search(word, item.text):
						temp_sentence.append(item.text)
						break

				root_token.remove((word,dep))
				break

		for word, dep in root_token:
			if dep == 'aux':
				temp_sentence.append(word)
				root_token.remove((word,dep))

		temp_sentence.append(u'be')
		for word, dep in root_token:
			if dep == 'ROOT':
				temp_sentence.append(word)
				root_token.remove((word,dep))

		flag = 0 
		temp_sentence.append(u'by')
		for word, dep in root_token:
			if dep == 'nsubj':
				for item in doc.noun_chunks:
					if re.search(word, item.text):
						temp_sentence.append(item.text)
						break
				root_token.remove((word,dep))
				break
		#print temp_sentence
		temp_sentence2 = ' '.join(x for x in temp_sentence)
		sentence_passive = temp_sentence2
		print sentence_passive
		return sentence_passive

text = open('input.txt').read()
p = Paraphrase()
p.text = text
#print p._pos_tagged_words
print(p.paraphrase())
#print(p._change_voice())