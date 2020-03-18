from collections import Counter
import re
from nltk.corpus import stopwords

#Counts and returns the number of useful words of any given document
def word_count(texts):

    #getting the stop words from nltk database
    stop_words = stopwords.words('english')
    total_texts = ""

    #appending all the texts to analyze all of them together
    for i in range(0 , len(texts)):
        article = texts[i].lower()
        total_texts = total_texts + article

    #getting the word count for the merged article sets(getting 10 most common words)
    words = re.findall('\w+' , total_texts)
    count = Counter(words).most_common()
    count = [(word , cnt) for word , cnt in count if word not in stop_words]
    count = count[0 : 10]
      
      
    return count
    