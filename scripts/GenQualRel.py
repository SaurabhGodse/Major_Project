import pandas as pd
import csv

f = open('stripped_equations_thermo.txt', 'r')
fRel = open("QuaRel.txt", 'a')
df = pd.read_csv('thermo_map.csv')
# print(df)

d = dict()
for i in range(len(df)):
	if df.iloc[i, 1].find(",") != -1:
		l = df.iloc[i, 1].split(",")
		for sym in l:
			d[sym.strip()] = df.iloc[i, 0]
	else:
		d[df.iloc[i, 1]] = df.iloc[i, 0]
#print(d, len(d))

s = set()
s1 = set()
for line in f:
	comma_sep = line.split(",")
	LHS = comma_sep[0]
	while LHS.find('Eq(') != -1:
		LHS = LHS.replace('Eq(', '')
	str1 = d[LHS]
	if str1.find(",") != -1:
		s1.add("synonym_of( " + str1 + " )" )	
		str1 = "\"" + str1 + "\""
	for formulas in comma_sep[1:]:
		relations = formulas.split('/')
		direct = relations[0]
		inverse = None
		
		if len(relations) > 1:
			inverse = relations[1]
		for key in d:
			if direct.find(key) != -1:
				str2 = d[key]
				if str2.find(",") != -1:
					s1.add("synonym_of( " + str2 + " )" )	
					str2 = "\"" + str2 + "\""

				#s.add((line, "q+( " + str1 + " , " + str2 + " )"))
				if str1 != str2:
					s.add("q+( " + str1 + " , " + str2 + " )")
		if inverse:
			for key in d:
				if inverse.find(key) != -1:
					str2 = d[key]
					if str2.find(",") != -1:
						str2 = "\"" + str2 + "\""
					#s.add((line, "q-( " + str1 + " , " + str2 + " )"))
					if str1 != str2:
						s.add("q-( " + str1 + " , " + str2 + " )")
		# print("D : ", direct)
		# print("I :        ", inverse)

# s = list(s)
# print(type(s[0]))
for element in s:
	# fRel.write(element[0] + "---> " + element[1] + "\n")
	fRel.write(element + "\n")

for element in s1:
	fRel.write(element + "\n")

