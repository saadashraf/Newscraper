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
It uses beautifulsoup4 framework to scrape the website. For now, I chose The Guardian. Upon setting the url, we get a request for the website. Then use a soup object to find all the news articles.

After that, I filtered the articles based on the keywords "coronavirus" and "covid-19". Then stored the article url. From the article url, I made another request object for that url. This was used to create a soup object with the webpage , and separate all the titles and store them. By similar fashion, using the same soup object, I separated the author name and the article contents.

In the end, I took all the records into a list and returned the list.

### export_data.py
It takes all the data recorded from scraping.py, converts them into a pandas dataframe, and publishes that into a csv file in the local directory. For now, I didn't use any cloud storage for storing these data.

