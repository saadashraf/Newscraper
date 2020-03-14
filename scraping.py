import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/au"

request = requests.get(url)
website = request.content

soup_website = BeautifulSoup(website , 'html5lib')
homepage_news = soup_website.find_all("h3" , class_ = "fc-item__title")

article_title = []
article_link = []
article_content = []
article_content_extended = []
article_title_extended = []

for i in range(len(homepage_news)):
    if ("coronavirus" not in homepage_news[i].find("a")["href"] and
        "covid-19" not in homepage_news[i].find("a")["href"]):
        continue
    link = homepage_news[i].find("a")["href"]
    article_link.append(link)

    article = requests.get(link)
    article_webpage  = article.content
    soup_article = BeautifulSoup(article_webpage , "html5lib")
    header = soup_article.find("h1" , class_ = "content__headline")
    print(link)
    print(header.get_text())
    article_title_extended.append(header.get_text())


    title = homepage_news[i].find_all("span")[0].get_text()
    article_title.append(title)

    content = homepage_news[i].find_all("span")[1].get_text()
    article_content.append(content)

    paragraph = soup_article.find_all("p")
    print(paragraph[0].get_text())

    print(i)




#print(homepage_news[0].find_all("span")[0].get_text())
#print(homepage_news[1].find('a')["href"])
#print(len(homepage_news))

'''for i in range(len(article_title)):
    print(article_title[i])
    print(article_content[i])
    print(article_link[i])
    print("\n")'''