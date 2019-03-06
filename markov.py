from markov import Db
from markov import Generator
from markov import GenratorWithSeed
from markov import Parser
from markov import Sql
from markov import Rnd
import sys
import sqlite3
import codecs

SENTENCE_SEPARATOR = '\n'
WORD_SEPARATOR = ' '

if __name__ == '__main__':
	args = sys.argv
	usage = 'Usage: %s (parse <name> <depth> <path to txt file>|syn <name> <synonyms file>|gen <name> <count>|seed <name> <"seed words"> <count>)' % (args[0], )

	if (len(args) < 3):
		raise ValueError(usage)

	mode  = args[1]
	name  = args[2]
	
	if mode == 'parse':
		if (len(args) != 5):
			raise ValueError(usage)
		
		depth = int(args[3])
		file_name = args[4]
		
		db = Db(sqlite3.connect(name + '.db'), Sql())
		db.setup(depth)
		
		txt = codecs.open(file_name, 'r', 'utf-8').read()
		Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse(txt)
  
	elif mode == 'syn':
		if (len(args) != 4):
			raise ValueError(usage)
		
		file_name = args[3]
		
		db = Db(sqlite3.connect(name + '.db'), Sql())
		
		txt = codecs.open(file_name, 'r', 'utf-8').read()
		Parser(name, db, SENTENCE_SEPARATOR, WORD_SEPARATOR).parse_synonyms(txt)
  
	elif mode == 'gen':
		count = int(args[3])
		db = Db(sqlite3.connect(name + '.db'), Sql())
		generator = Generator(name, db, Rnd())
		for i in range(0, count):
			print(generator.generate(WORD_SEPARATOR))

	elif mode == 'seed':
		seed_word = args[3]        
		count = int(args[4])
		db = Db(sqlite3.connect(name + '.db'), Sql())
		generator = GenratorWithSeed(name, db, Rnd())
		for i in range(0, count):
			print(generator.generate_from_center(seed_word.split(WORD_SEPARATOR), WORD_SEPARATOR))
			print('\n')
	
	else:
		raise ValueError(usage)