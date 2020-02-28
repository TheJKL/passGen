#!/usr/bin/python3
import random

#word and symbol list limit
with open("passWordlist.txt") as file:
	wordlist = file.readlines()





def getPass(n, min = 0, max = 100,numMax = 99,seperator = "_",symbols = ["(","#",")","%","^"]):
	if min == 0: min = n*4
	passw = ""
	for _ in range(n-1):
		passw += f"{seperator}{random.choice(wordlist).strip()}"
	passw += f"{random.choice(wordlist).strip().capitalize()}{random.choice(symbols)}{random.randint(1,numMax)}"
	l = len(passw)
	if l >= min and l <= max:
		return passw
	else:
		return getPass(n,min,max)


print(getPass(4,max = 30))
