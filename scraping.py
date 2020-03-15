import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/au"

request = requests.get(url)
website = request.content

soup_website = BeautifulSoup(website , 'html5lib')
homepage_news = soup_website.find_all("h3" , class_ = "fc-item__title")

article_link = []
article_title = []
article_author = []
article_content = []

for i in range(len(homepage_news)):
    if ("coronavirus" not in homepage_news[i].find("a")["href"] and
        "covid-19" not in homepage_news[i].find("a")["href"]):
        continue

    #Link
    link = homepage_news[i].find("a")["href"]
    article_link.append(link)
    print(link)

    #Title
    article = requests.get(link)
    article_webpage  = article.content
    soup_article = BeautifulSoup(article_webpage , "html5lib")
    title = soup_article.find("h1" , class_ = "content__headline")
    if title is not None:
        print(title.get_text())
        article_title.append(title.get_text())

    #author
    paragraphs = soup_article.find_all("p")
    if paragraphs[1] is not None:
        name = paragraphs[1].get_text()
        print(name)

    #content
    list_of_paragraphs = []
    
    for j in range(0 , len(paragraphs)):
        if(j == 1):
            continue
        p = paragraphs[j]
        paragraph = p.get_text()
        list_of_paragraphs.append(paragraph)
        content = "\n".join(list_of_paragraphs)
    
    article_content.append(content)
    print(content)

    print(i)




#print(homepage_news[0].find_all("span")[0].get_text())
#print(homepage_news[1].find('a')["href"])
#print(len(homepage_news))

'''for i in range(len(article_title)):
    print(article_title[i])
    print(article_content[i])
    print(article_link[i])
    print("\n")'''