from nltk.stem import PorterStemmer , WordNetLemmatizer

stemmer = PorterStemmer()
lemmatiser = WordNetLemmatizer()
sentences = " I have studied computer science for three years I have been learning about manage data That thing is a very interesting for me"
arrayWord = sentences.split(" ")

"""emmatiser = WordNetLemmatizer()

print("Stem %s: %s" % ("studying", stemmer.stem("studying")))
print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying")))
print("Lemmatise %s: %s" % ("studying", lemmatiser.lemmatize("studying", pos="v")))
"""

for i in arrayWord:
	print(stemmer.stem(i),lemmatiser.lemmatize(i))

