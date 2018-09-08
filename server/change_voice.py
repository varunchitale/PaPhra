

def change_voice(sentence_active, _nlp):

	doc = _nlp(sentence_active)
	
	if not set(['nsubj', 'ROOT', 'dobj']).intersection([token.dep_ for token in doc]) == set(['nsubj', 'ROOT', 'dobj']):
		return sentence_active
	

	root_token = [(token.text, token.dep_) for token in doc if token.dep_ in  ('nsubj', 'aux', 'ROOT', 'dobj')]
	
	'''
	temp_sentence = []
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
	'''
	sentence_passive = ' '.join(x for x,dep in root_token)
	

	return sentence_passive