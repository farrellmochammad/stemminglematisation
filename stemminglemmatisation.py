from nltk.stem import PorterStemmer , WordNetLemmatizer

stemmer = PorterStemmer()
#lemmatiser = WordNetLemmatizer()
words = "Washing Bringing Catched Pain Plating Goes Groups Burned Lifting Likes Locking Disgusting Marker Maping Slept Doing Rating Cooking Cried Bleed Boxs Bones Acting"
arrayWord = words.split(" ")

for i in arrayWord:
	print(stemmer.stem(i))
	""",lemmatiser.lemmatize(i)"""
