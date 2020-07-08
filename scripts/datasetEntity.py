#this file uses stanford POS tagger to tag words in sentence

import pandas as pd
from nltk import *

f1 = open("dataEntities.txt", "w+")

files = ['/home/saurabh/Downloads/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Dev.csv', '/home/saurabh/Downloads/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Test.csv', '/home/saurabh/Downloads/ARC-V1-Feb2018-2/ARC-Challenge/ARC-Challenge-Train.csv']
for file in files:
	df = pd.read_csv(file)
	entity_list = []
	for i in range(df.shape[0]):
		text = df.loc[i, "question"]
		print(file, i)
		myTagger = StanfordPOSTagger("./stanford-postagger-full-2018-10-16/models/english-left3words-distsim.tagger", "./stanford-postagger-full-2018-10-16/stanford-postagger-3.9.2.jar")
		taggedText = myTagger.tag(text.split())
		for text in taggedText:
			if text[1] in ['NN', 'NNS', 'NNP', 'NNPS']:
				item = ''.join(e for e in text[0] if e.isalnum())
				if item not in ['A', 'B', 'C', 'D']:
					entity_list.append(item)
		entity_set = set(entity_list)
				
		for item in entity_set:
			f1.write("%s\n"%item)
