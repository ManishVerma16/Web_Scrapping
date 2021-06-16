from requests_html import HTML

with open('simple.html') as html_file:  # opening the file in read mode 
    source = html_file.read()   # reading the html file
    html = HTML(html=source)    # reading the content using HTML object

# print(html.html)    # printing the html content
# print(html.text)    # printing the text content from the html tags

# match = html.find('title') # here the find method uses css selector to find elements and return a list of elements.
# print(match)    # return list of elements
# print(match[0].html)    # print the element tag with text content
# print(match[0].text)    # print the text of html

# match = html.find('title', first=True) # here the find method uses css selector to find elements and returns the first element of list.
# print(match.html)    # print the element tag with text content
# print(match.text)    # print the text of html

# match = html.find('.footer', first=True) # here the id attribute of the tag an be selected by # sign and class ny . with tag name
# print(match.text)   


articles = html.find('div.article') # here the id attribute of the tag an be selected by # sign and class ny . with tag name

for article in articles:
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(headline)
    print(summary)
    print()