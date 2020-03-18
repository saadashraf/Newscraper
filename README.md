# Newscraper
An application that crawls a news website(https://www.theguardian.com/au in this application) to search for news relevant to "coronavirus" or "covid-19". After crawling, it gets the article URL , author name , Title and contents of the article, then saves the data in a csv file. The article content is then passed on to get the word count for that particular instance of the application, and among those, most common 10 words are taken. These most common words are stored in a postgresql database to store.

## Files used
There are 5 python files used in the solution:
- program.py - This file is used as the main file of the solution. Run this file to execute the application.
- scraping.py - Used to scrape the articles.
- export_data.py - This file exports the gathered data into csv format.
- analytics.py - Gets the word hit count data for the articles.
- postgres_op.py - Uploads the hit count data into a postgres database.