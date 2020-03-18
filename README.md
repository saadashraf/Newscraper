# Newscraper
An application that crawls a news website(https://www.theguardian.com/au in this application) to search for news relevant to "coronavirus" or "covid-19". After crawling, it gets the article URL , author name , Title and contents of the article, then saves the data in a csv file. The article content is then passed on to get the word count for that particular instance of the application, and among those, most common 10 words are taken. These most common words are stored in a postgresql database to store.

## Files used
There are 5 python files used in the solution:
- program.py - This file is used as the main file of the solution. Run this file to execute the application.
- scraping.py - Used to scrape the articles.
- export_data.py - This file exports the gathered data into csv format.
- analytics.py - Gets the word hit count data for the articles.
- postgres_op.py - Uploads the hit count data into a postgres database.

### scraping.py
It uses beautifulsoup4 framework to scrape the website. For now, I chose The Guardian. Upon setting the url, I get a request for the website. Then use a soup object to find all the news articles.

After that, I filtered the articles based on the keywords "coronavirus" and "covid-19". Then stored the article url. From the article url, I made another request object for that url. By this, I could get into all the individual articles' webpage of interest.  The soup object created with that request allowed me to separate all the titles and store them. By similar fashion, using the same soup object, I separated the author name and the article contents.

In the end, I took all the records into a list and returned the list.

### export_data.py
It takes all the data recorded from scraping.py and analytics.py, converts them into pandas dataframe, and publishes that into csv file in the local directory. I used two separate functions for the two types of data. For now, among the two types of data exported (information and analytic), only the word hit count data is stored in a cloud postgres database.(Heroku postgres).

### analytics.py
This file takes all the article contents I got from scraping.py file. Here, I used nltk to get rid of all the redundant stop words.

In the loop, I concatenated all the articles together. Then used Counter() method to count all the occurences of all the words, cancelled the stop words and returned the 10 most common words.

### postgres_op.py
This file uploads the word hit counts into a postgres database. It takes the word count returned from analytics.py. Then it get a connection to the remote database with relevant credentials and inserts the data into the database.

### program.py
This script calls all the files above. Executing program.py performs relevant data gathering, exports the data as csv, uses the contents of the articles to get the word count and finally, uploads the word count in the cloud postgres database.

### The postgres formation
In the postgres database, I created a table called analytics with 4 columns.
- ID - Serially generated and the primary key.
- Timestamp - Automatically generated, keeps record of the time the data was inserted.
- Word - The word being counted.
- Count - Count of the word got.

I used heroku postgres as cloud postgres database.
