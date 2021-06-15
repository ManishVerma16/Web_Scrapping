from os import name
from bs4 import BeautifulSoup
import requests, csv

# source = requests.get('http://coreyms.com') # this request return a response code 200 if webpage found.
# print(source)

source = requests.get('http://coreyms.com').text # this request return a html page in response if webpage found.
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
# link = article.div.iframe['src']        # if we want to grab the value of an attribute the we can use attribute name as dictionary.

def scrape_out():

    csv_file = open('website_scrap.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])

    articles = soup.find_all('article')
    for article in articles:
        headline = article.h2.a.text
        summary = article.div.p.text
        try:   
            video_id = article.div.iframe['src'].split('/')[4]
            video_id = video_id.split('?')[0]
            video_link = f'https://www.youtube.com/watch?v={video_id}'
        except Exception as e:
            video_link = None
        print(headline)
        print()
        print(summary)
        print()
        print(video_link)
        print()

        csv_writer.writerow([headline, summary, video_link])

    csv_file.close()

if __name__ == '__main__':
    scrape_out()



