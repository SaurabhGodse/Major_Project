import csv
import pandas as pd
# # run this to generate file containing tables with 5 columns
# f1 = open('electro1.csv', 'w')
# with open('electro.csv', 'r') as f:
# 	data = csv.reader(f)
# 	for row in data:
# 		if(len(row) == 5):
# 			for i in range(5):
# 				if i == 4:
# 					if row[i].find(",") != -1:
# 						f1.write("\"" + row[i] + "\"")
# 					else:
# 						f1.write(row[i])
# 				else:
# 					if row[i].find(",") != -1:
# 						f1.write("\" " + row[i] + "\",")
# 					else:
# 						f1.write(row[i] + ",")
# 			f1.write("\n")



# 			# s = ""
# 			# for item in row:
# 				# print(item)

			
# 			# print(",".join(row))
# 			# print(len(row), " : ", row)

# f1.close()
# f.close()

### run this to generate file containing quantity name and their symbols
df = pd.read_csv("electro1.csv")

df = df.iloc[:, :2]
print(df)
df.to_csv("electro_map.csv", index = False)
for i in range(len(df)):
	if str(df.iloc[i, 0]).find("=") == -1:
		print(df.iloc[i, 0] + " : \t" + df.iloc[i, 1])
print(df.iloc[:, 0:2])