from optparse import OptionParser
from random import randint

def get_args():
	parser = OptionParser()
	parser.add_option("-l", "--length", dest="length", type="int",
						help="Number of words to include in the password.",
						metavar="INT",
						default=5)
	parser.add_option("-g", "--generate", dest="num_to_gen", type="int",
						help="Number of passwords to generate.",
						metavar="INT",
						default=10)
	options, args = parser.parse_args()
	return options, args

def load_dw_dict():
	d = {}
	with open('dwlist') as f:
		for line in f:
			key, value = line.split(' ')
			d[key] = value[:-1] # remove newline char
	return d

options, args = get_args()
dw_dict = load_dw_dict()

def roll(x, y):
	return randint(x,y)

def create_rolls(n, x, y):
	rolls = []
	for i in range(n):
		rolls.append(str(roll(x,y)))
	return rolls

def get_new_pw(length):
	pw = []
	for i in range(length):
		rand = ''.join(create_rolls(5, 1, 6)) # dw takes 5 random ints, from 1-6
		pw.append(dw_dict.get(rand, ""))
	return ''.join(pw)

if __name__ == '__main__':
	for i in range(options.num_to_gen):
		print(get_new_pw(options.length))