from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 
  
print("swung :", lemmatizer.lemmatize("swung", 'v')) 
print("slipped :", lemmatizer.lemmatize("slipped", 'v')) 
  
# a denotes adjective in "pos" 
print("rubbing :", lemmatizer.lemmatize("rubbing", 'v'))