import sys
import re

class Parser:
	SENTENCE_START_SYMBOL = '^'
	SENTENCE_END_SYMBOL = '$'

	def __init__(self, name, db, sentence_split_char = '\n', word_split_char = ''):
		self.name = name
		self.db   = db
		self.sentence_split_char = sentence_split_char
		self.word_split_char = word_split_char
		self.whitespace_regex = re.compile('\s+')

	def parse_array(self, sentences):
		depth = self.db.get_depth()

		i = 0

		for sentence in sentences:
			sentence = self.whitespace_regex.sub(" ", sentence).strip()

			list_of_words = None
			if self.word_split_char:
				list_of_words = sentence.split(self.word_split_char)
			else:
				list_of_words = list(sentence.lower())

			words = [Parser.SENTENCE_START_SYMBOL] * (depth - 1) + list_of_words + [Parser.SENTENCE_END_SYMBOL] * (depth - 1)
			
			for n in range(0, len(words) - depth + 1):
				self.db.add_word(words[n:n+depth])
			
			i += 1
			if i % 1000 == 0:
				print(i)
				sys.stdout.flush()
		
		self.db.commit()

	def parse(self, txt):
		sentences = txt.split(self.sentence_split_char)
		self.parse_array(sentences)
  
     
	def parse_synonyms(self, txt):
		pairs = txt.split(self.sentence_split_char)
		i = 0

		for pair in pairs:
			list_of_words = pair.split(",")
			if len(list_of_words) !=2:
				break

			self.db.add_synonyms(list_of_words[0], list_of_words[1])
   
			i += 1
			if i % 1000 == 0:
				print(i)
				sys.stdout.flush()
		
		self.db.commit()   


