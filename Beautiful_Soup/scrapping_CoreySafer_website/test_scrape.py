from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:      # opening the simple html file as html_file
    soup = BeautifulSoup(html_file, 'lxml') # reading the content of the html_file using beautiful soup

# print(soup) # printing the content of html_file
#print(soup.prettify()) # printing the content in the formatted or indented way.

'''
tip: the easiest way to grab the information of the tag is to access it like an attribute. But it will be good for only first attribute and not suitable for multiple tag.
'''

# title_match = soup.title.text   # accessing the title of the page
# print(title_match)

# article = soup.find('div', class_='article')  # grabbing the article from the soup
# headline = article.h2.a.text                  # accessing the text from the class article div tag
# print(headline)
# summary = article.p.text                   # grabbing the paragraph from the class article div tag
# print(summary)

articles = soup.find_all('div', class_='article')  # grabbing the all article from the soup
for article in  articles:                           # iterating through each article
    headline = article.h2.a.text
    summary = article.p.text                   
    print(headline)
    print(summary)
    print()
