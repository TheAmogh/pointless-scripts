import random
import string
import time
import argparse


parser = argparse.ArgumentParser(prog='print_random_characters', description='Dummy logs output')
parser.add_argument('-l', '--length', type=int, default=1000)
parser.add_argument('-s', '--speed', type=float, default=20)
args = parser.parse_args()

PRINTABLE = string.printable[:-2]
LENGTH = args.length
SPEED = args.speed

def getRandomChar():
	return PRINTABLE[random.randint(0, len(PRINTABLE)-1)]

''' Get random length between 2 and 20'''
def getRandomLength():
	return random.randint(2, 20)

def getRandomChunk():
	return random.choices(PRINTABLE, k=getRandomLength())

def getRandomDelay():
	return abs(random.gauss(mu=0, sigma=1)) / SPEED

for _ in range(LENGTH):
	print(''.join(getRandomChunk()), end='')
	time.sleep(getRandomDelay())