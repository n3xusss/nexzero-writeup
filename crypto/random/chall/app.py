#!/usr/local/bin/python

import random

FLAG = open("flag.txt", "r").read()

if __name__ == "__main__":
	for _ in range(10):
		print("Take some random numbers :")
		print([random.getrandbits(32) for _ in range(99)])

		next_random = int(input("Can you guess the next one : "))
		if next_random == random.getrandbits(32):
			print(FLAG)
			exit()
	exit()
