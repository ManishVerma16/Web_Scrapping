from requests_html import HTML

with open('simple.html') as html_file:  # opening the file in read mode 
    source = html_file.read()   # reading the html file
    html = HTML(html=source)    # reading the content using HTML object
    html.render()       # rendering the dynamic data from web page

match = html.find('#footer', first=True)
print(match.html)

