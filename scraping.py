import requests
from bs4 import BeautifulSoup


#Scraping the news website and getting the news articles and details about them
def scraping_output():

    #The website we are scraping
    url = "https://www.theguardian.com/au"

    #get the request for the website
    request = requests.get(url)
    website = request.content

    #get a soup object and find all the news contents
    soup_website = BeautifulSoup(website , 'html5lib')
    homepage_news = soup_website.find_all("h3" , class_ = "fc-item__title")

    #lists to store informations
    article_link = []
    article_title = []
    article_author = []
    article_content = []

    #iterating through the news articles
    for i in range(len(homepage_news)):

        #checking if the news is related to coronavirus
        if ("coronavirus" not in homepage_news[i].find("a")["href"] and
            "covid-19" not in homepage_news[i].find("a")["href"]):
            continue

        #Getting the url for the article
        link = homepage_news[i].find("a")["href"]
        article_link.append(link)
        #print(link)

        #Getting the title of the article
        article = requests.get(link)
        article_webpage  = article.content
        soup_article = BeautifulSoup(article_webpage , "html5lib")
        title = soup_article.find("h1" , class_ = "content__headline")
        if title is not None:
            #print(title.get_text())
            article_title.append(title.get_text())
        else:
            article_title.append("None")

        #Getting the aithor info of the article
        paragraphs = soup_article.find_all("p")
        if paragraphs[1] is not None:
            name = paragraphs[1].get_text()
            article_author.append(name)
            #print(name)
        else:
            article_author.append("None")

        #Getting the news content
        list_of_paragraphs = []
        
        for j in range(0 , len(paragraphs)):
            if(j == 1):
                continue
            p = paragraphs[j]
            paragraph = p.get_text()
            list_of_paragraphs.append(paragraph)
            content = "\n".join(list_of_paragraphs)
        
        article_content.append(content)
        #print(content)


    #Returning all the stored results of the scraping
    return [article_link , article_title , article_author , article_content]
