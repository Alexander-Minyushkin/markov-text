# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:43:12 2017

@author: minushkin
"""

from parse import Parser
from gen import  Generator

class GenratorWithSeed(Generator):
    """
    GenratorWithSeed have to generate phrase with predefined word in it
    """
    
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

if __name__ == '__main__':
    pass