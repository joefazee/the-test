# Author Abah Joseph
# created on 23rd July 2014

################################################################################################
# DEPTH FIRST TREE TRAVERSAL
################################################################################################
# Start from the top root down to the branches before backtracking by keeping track
# of the visited nodes
#--------


########### CHARACTERS IN STRINGS ###############################################################
# Implement a function with signature find_chars(string1, string2) that takes two strings 
# and returns a string that 
# contains only the characters found in string1 a version of order N*N and one of order N."""
####################################################################################################

''' version 1 ''' 
def find_chars(string1, string2):
	output = []
	for char in string2:
		if char in string1:
			output.append(char)
	return ''.join(output)

# TEST IT
#print find_chars("Abah joseph playing around with python", "python is fun and sure, Abah joseph is here")

''' version 2 '''
# Start searching from start and stop at end with the last character included
def find_chars_start_end(string1, string2, start=0, end=0):
	string = string1[start:]
	if end != 0 and end <= (len(string1)-1):
		string = string1[start:end]
	return find_chars(string, string2)

# TEST IT
#print find_chars_start_end("abah joseph", "joseph and more extra", 4)
########################################## END ############################################







########### ARRAY COMPACTION ###############################################################
# Write a function that takes as input a sorted array and modifies the array to compact it, 
# removing duplicates.'''
#############################################################################################

'''remove duplicate from array using python set and list function'''
def remove_dulicate_from_array(array):
	return list(set(array))

# TEST IT
# print remove_dulicate_from_array([1,2,2,3,4,4,4,5,6,6,8,9,10])

'''remove duplicate from array manually '''
def remove_dulicate_from_array2(array):
	output = []
	for element in array:
		if element not in output:
			output.append(element)
	return output

# TEST IT
#print remove_dulicate_from_array2([1,2,2,3,4,4,4,5,6,6,8,9,10])
################################################ END ############################################








########### STRING TOKENIZATION #######################################################################
# Write a function, tokenize_string(input_string, delimiter_list) that returns a list of strings 
# that are separated by the delimiters. 
#
# For example: tokenize_string("How now, Mrs. Brown Cow") returns ['How', 'now', 'Mrs', 'Brown', 'Cow']
########################################################################################################

def tokenize_string(input_string, delimiter_list=' '):
	return input_string.split(delimiter_list)

# TEST IT
#print tokenize_string("How now, Mrs. Brown Cow", ' ')
################################################ END ############################################










########### ROTATING AN ARRAY #################################################################################
# Write a function that takes an array of integers and returns that array rotated by N positions. 
#
# For example, if N=2, given the input array [1, 2, 3, 4, 5, 6] the function should return [5, 6, 1, 2, 3, 4]
###############################################################################################################
from collections import deque
def rorate_array_at_n(array, n=0):
	if n <= 1: return array
	dequed = deque(array)
	dequed.rotate(n)
	return dequed
# TEST IT
# print rorate_array_at_n([1, 2, 3, 4, 5, 6], 2)










########### LEAST COMMON MULTIPLE
# The least common multiple of a set of integers is the smallest positive integer 
# that is a multiple of all of the integers in the set. 
#
# Write a function that takes an array of integers and efficiently calculates and returns the LCM.
# - find LCM of two integers
def _least_common_multiple(a,b):
    temp_var = a
    while (temp_var %b ) != 0:
        temp_var += a
    return temp_var

# find LCM of two or more integers using python reduce function
def least_common_multiple(*args):
    return reduce(_least_common_multiple, args)

# TEST IT
# print least_common_multiple(21, 35, 40, 34)









########### TEST DRIVEN DEVELOPMENT #################################################################################
# Explain the principles of test drive development.
#
# Create a test using any testing framework you wish for the following function
#
#
# PRINCIPLES OF TEST DRIVING DEVELOPMENT
#---------------------------------------
# 1. Write test first then code to make the test pass
# 2. Write acceptance test to previent software bugs
# 3. Continuous testing - write a failing test then make it pass
#
# EXAMPLE
#

import unittest 

class Tweet(object):
	def __init__(self, body=None, handle=None):
		self.body = body
		self.handle = handle

	def set_body_and_title(self):
		self.body = 'sample here'
		self.handle = '@freefazee'

class TweetTest(unittest.TestCase):

	def setUp(self):
		self.tweet = Tweet()

	def test_body_and_handle_is_none(self):
		
		self.assertEqual(self.tweet.body, None)
		self.assertEqual(self.tweet.handle, None)

	def test_body_and_title_is_true(self):
		self.tweet.set_body_and_title()
		self.assertTrue(self.tweet.body)
		self.assertTrue(self.tweet.handle)

if __name__=='__main__':
	unittest.main()