import json
import nltk
# import string
from nltk import *
import pandas as pd
# nltk.download('wordnet')
from nltk.corpus import wordnet
import pickle

verbs = ['VB', 'VBG', 'VBD', 'VBN', 'VB', 'VBP', 'VBZ']
adjectives = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']
lemmatizer = WordNetLemmatizer()
# keys = pd.read_csv("dictionary_keys.csv")
f = open("glossary.txt", "r")
key_set = set()
for key in f:
	print(key)
	key_set.add(key.strip())
print(key_set)

# for key in keys.iloc[:, 0]:
	# key_set.add(key)
# print(key_set)

def filt(x):
    return x.label()=='NP'

def alphaconv(s):
	return "".join([i for i in s if(i.isalpha())])
def tokenize_lemmitize(text, lemmitized_text, name, definition, word):
	# global key_set
	taggedText = pos_tag(text.split())
	# print("this is text : ", text)
	# print("this is tagged text : ", taggedText)
	# lemmitized_text = []
	for a, b in taggedText:
		if b in verbs:
			temp = alphaconv(lemmatizer.lemmatize(a, pos = 'v'))
			# if temp in key_set:
			# 	# print("this is temp : ", temp)
			# 	#fres.write("\n")
			# 	#fres.write(word + "\n")
			# 	#fres.write(name + "\n")
			# 	#fres.write(definition + "\n")
			# 	#fres.write("The word found in dictionary --> " + temp)
			# 	#fres.write("\n")
			# 	print(word)
			# 	print(name)
			# 	print(definition)
				# print(taggedText)
			lemmitized_text.append(temp)
		
		elif b in adjectives:
			temp = alphaconv(lemmatizer.lemmatize(a, pos = 'a'))
			# if temp in key_set:
			# 	#fres.write("\n")
			# 	#fres.write(word + "\n")
			# 	#fres.write(name + "\n")
			# 	#fres.write(definition + "\n")
			# 	#fres.write("The word found in dictionary --> " + temp)
			# 	#fres.write("\n")
			# 	# print("this is temp : ", temp)
			# 	print(word)
			# 	print(name)
			# 	print(definition)
				# print(taggedText)
			lemmitized_text.append(temp)
		else:
			temp = alphaconv(lemmatizer.lemmatize(a))
			# if temp in key_set:
			# 	#fres.write("\n")
			# 	#fres.write(word + "\n")
			# 	#fres.write(name + "\n")
			# 	#fres.write(definition + "\n")
			# 	#fres.write("The word found in dictionary --> " + temp)
			# 	#fres.write("\n")
			# 	# print("this is temp1 : ", temp)
			# 	print(word)
			# 	print(name)
			# 	print(definition)
				# print(taggedText)
			# print("this is temp : ", temp)
			lemmitized_text.append(temp)
	# return lemmitized_text



# def filtsubtree(y):
# 	return y.label() in ['VB', 'VBG', 'VBD', 'VBN', 'VB', 'VBP', 'VBZ']
# f1 = open("PhyConcepts.txt", 'w')
train_set = dict()
file_list = ["quarel-v1-train.json"]
entity_set_list = []
#fres = open("new_result.txt", "w")
for file in file_list:
	with open(file, 'r') as f:
		entity_list = []
		line_number = 1
		for line in f:
			# print("line : ", line_number)
			data = json.loads(line)
			# text = "Marcus's son took the pool ball off the pool table to play with it around the house. The son noticed that the pool ball rolled a longer distance on the marble floor than on the shag rug. The smoother surface is (A) the marble floor or (B) the shag rug"
			text = data['question']

			# f1.write("Question number : " + str(line_number) + "\n" + text + "\n")
			# f1.write("-------->" + "\n")
			# print(text)
			sentence = text.split(".")

			# myTagger = StanfordPOSTagger("/home/saurabh/Downloads/stanford-postagger-full-2018-10-16/models/english-left3words-distsim.tagger", "/home/saurabh/Downloads/stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2.jar")
			# taggedText = myTagger.tag(text.split())
			result = ""
			lemmitized_text = []
			if line_number == 3:
				print(text)

				#fres.write("Question --> \n" + text)
				#fres.write("\n\n\n")
				#fres.write("Subtrees --> \n")

			for text in sentence:

				taggedText = pos_tag(text.split())
				# print(taggedText)
				grammar = "NP: {(<JJ>*<RB>*)*(<VB>|<VBG>|<VBD>|<VBN>|<VB>|<VBP>|<VBZ>)+(<IN>*<DT>*<PRP>*<JJR>*<JJ>*<NN>*<RP>*<RBR>*<RBS>*<TO>*<RB>*)+}"
				cp = nltk.RegexpParser(grammar)
				res = cp.parse(taggedText)
				# result += str(res)
				# print(res)
				
				for subtree in res.subtrees(filter =  filt): # Generate all subtrees
					# if line_number == 3:
						#fres.write(str(subtree))
						#fres.write("\n")
					# print(subtree)
					for a, b in subtree.leaves():
						if b in verbs or b in adjectives:
							# print("--------------------------------------------------")
							# print(a, b)
							syns = wordnet.synsets(a)
							for i in syns:
								name = i.name()
								definition = i.definition()
								# print("this is name : ", name)
								# print("this is definition : ", definition)
								# print("name tokenize_lemmitize -- >")
								# if line_number == 3:
								tokenize_lemmitize(name.split(".")[0], lemmitized_text, name, definition, a)
									# print("definition tokenize_lemmitize -- >")
								tokenize_lemmitize(definition, lemmitized_text, name, definition, a)
							# print("\n\n\n")

			# f1.write(str(key_set.intersection(set(lemmitized_text))))
			# if line_number == 3:
			#fres.write("\n\nResults --> \n")
			curr_res = str(key_set.intersection(set(lemmitized_text)))
			#fres.write(curr_res)
			print(line_number)
			train_set[line_number] = curr_res

				
			# break
			# f1.write("\n\n\n")
			line_number += 1
			# break
			# if(line_number == 10):
			# 	break

# 		entity_set_list.append(set(entity_list))
print(train_set)
pickle.dump(train_set, open("train_set", "wb"))

# entity_set = set()
# for s in entity_set_list:
# 	entity_set = entity_set | s


# f = open("/mnt/dell/garima/verbs_in_quarel.txt", "w")
# for item in entity_set:
# 	f.write("%s\n"%item)
# f.close()
# <VBD>
# <VBG>
# <VBN>
# <VB>
# <VBP>
# <VBZ>

# print(alphaconv("saurabh 34234 32"))