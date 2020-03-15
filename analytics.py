from collections import Counter
import re
from nltk.corpus import stopwords

#Counts and returns the number of useful words of any given document
def word_count(texts):

    stop_words = stopwords.words('english')
    word_counter = []
    
    for i in range(0 , len(texts)):
        article = texts[i].lower()
        words = re.findall('\w+' , article)
        count = Counter(words)
        count = [(word, count) for word, count in count.items() if word not in stop_words]
        word_counter.append(count)
        
    return word_counter
    