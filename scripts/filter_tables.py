import pandas as pd
tables = pd.read_html("tables.html") # Returns list of all tables on page
print(tables[1])
sp500_table = tables[1]
print(sp500_table[1])
print(len(sp500_table))
for row in sp500_table:
	print(row)
