# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:43:12 2017

@author: minushkin
"""

from .parse import Parser
from .gen import  Generator

import collections

class GenratorWithSeed(Generator):
	"""
	GenratorWithSeed have to generate phrase with predefined word in it
	"""
	
	def _get_prev_word(self, word_list):
		candidate_words = self.db.get_word_count_to_left(word_list)
		total_next_words = sum(candidate_words.values())
		i = self.rnd.randint(total_next_words)
		t=0
		for w in candidate_words.keys():
			t += candidate_words[w]
			if (i <= t):
				return w
		assert False

	def generate_to_right(self, seedWords=[], word_separator=' '):
		depth = self.db.get_depth()
		sentence = [Parser.SENTENCE_START_SYMBOL] * (depth - 1)
		end_symbol = [Parser.SENTENCE_END_SYMBOL] * (depth - 1)

		sentence.extend(seedWords)
		try:
			while True:
				tail = sentence[(-depth+1):]
				if tail == end_symbol:
					break
				word = self._get_next_word(tail)
				sentence.append(word)
		except ValueError:
				return self.generate(word_separator)
        
		return word_separator.join(sentence[depth-1:][:1-depth])

	def generate_to_left(self, seedWords=[], word_separator=' '):
		depth = self.db.get_depth()
		sentence = collections.deque()		
		start_symbol = [Parser.SENTENCE_START_SYMBOL] * (depth - 1)

		sentence.extend(seedWords)
		try:
			while True:
				head = list(sentence)[0:(depth-1)]
				if head == start_symbol:
					break
				word = self._get_prev_word(head)
				sentence.appendleft(word)
		except ValueError:
				return self.generate(word_separator)
        
		return word_separator.join(list(sentence)[depth-1:][:1-depth])

	def generate_from_center(self, seedWords=[], word_separator=' '):
		leftPart = self.generate_to_left(seedWords, word_separator)
		rightPart = self.generate_to_right(seedWords, word_separator)		
		return leftPart + word_separator + rightPart

if __name__ == '__main__':
    pass