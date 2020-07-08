from process_latex import process_sympy
from bs4 import BeautifulSoup
# topic = wikipedia.page('list of equations in classical mechanics')
# equations = BeautifulSoup(topic.html()).find_all('annotation')
f = open('electroLatexEq.txt', 'r')
f1 = open('electroEngEq.txt','w+')
c = 1
for line in f:
	# print(count, line)
	# count += 1
	print(c)
	c += 1
	text = process_sympy(line)
	if(str(text)):
		f1.write(str(text) + "\n")



# for preprocessing of english latex formulas
# f = open("thermoToEng.txt", "r")
# f1 = open("thermoToEng1.txt", "w")
# for line in f.readlines():
# 	if line.find("Eq") != -1:
# 		f1.write(line)
# 		# f1.write("\n")
# f.close()
# f1.close()