#Document distance using cosine similarity

import re
from collections import Counter,defaultdict
import numpy as np

def doc_to_words_list(doc):
	# list_of_words = re.findall(r"\w+",doc)           # in general, re takes exponential time
	
	list_of_words = []
	word = ""

	for char in doc:                                   # O(len(doc)) = linear time		
		if char.isalpha():
			word += char
		elif len(word) > 0:
			list_of_words.append(word)
			word = ""

	if len(word) > 0:
		list_of_words.append(word)

	return list_of_words

def count_word_frequency(words_list):
	
	# both take O(kn) = O(len(doc)) = linear time  ;where k = number of chars in word n = number of words in list

	return Counter(words_list)               

	# d = defaultdict(int)
	# for word in words_list:
	#     d[word] += 1
	# return d

def cosine_similarity(vec1, vec2):
	#O(k1*k2)
	dot_product = np.dot(vec1, vec2)
	norm1 = np.linalg.norm(vec1)
	norm2 = np.linalg.norm(vec2)
	return dot_product / (norm1 * norm2)

def doc_distance(doc1,doc2):
	
	#O(len(doc)) = linear time
	words_list1 = doc_to_words_list(doc1) 
	words_list2 = doc_to_words_list(doc2)

	#O(len(doc)) = linear time
	vector_dict1 = count_word_frequency(words_list1)
	vector_dict2 = count_word_frequency(words_list2)
	
	# convert to word-vectors O(len(doc)) = linear time
	words  = list( set(vector_dict1.keys()) | set(vector_dict2.keys()))     #O(len(vector_dict1)) + O(len(vector_dict2))
	vec1 = [vector_dict1.get(word, 0) for word in words]        # O(k.n1) = O(len(doc1)) = linear time ;where k = number of chars in word and n1 = number of words in doc1
	vec2 = [vector_dict2.get(word, 0) for word in words]        # O(k.n2) = O(len(doc2)) = linear time ;where k = number of chars in word and n2 = number of words in doc2
	
	return cosine_similarity(vec1,vec2)


if __name__ == "__main__":
	doc1 = "my name is whatever is your name i don't care"
	doc2 = "i care about people's name whatever are their name"

	print(doc_distance(doc1,doc2))