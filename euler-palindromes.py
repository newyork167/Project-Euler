#!/usr/bin/python

# Set initial variables/lists
palindromes = []
least = 0;

# Loop through numbers decreasing from 999
for x in reversed(range(100,1000)):
	for y in reversed(range(100,1000)):
		
		# Make temp int to hold multiplication
		temp = x * y
		
		# If temp is less than least number in palindrome list skip it
		if(temp <= least):
			break
		
		# Set initial variables
		add = True
		z = 0
		
		# Loop through indexes to determine if number is palindrome
		while z < (len(str(temp)) / 2):
			if(str(temp)[z] != str(temp)[len(str(temp)) - z - 1]):
				add = False
				break
			z = z + 1
			
		# Adds palindrome to list
		if(add):
			palindromes.append(temp)
			least = temp
			break
	
# Sort palindromes and print in reversed order
palindromes.sort()	
for x in reversed(palindromes):
	print x