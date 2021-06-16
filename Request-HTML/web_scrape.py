from requests_html import HTML, HTMLSession
import csv

session = HTMLSession()     # creating an object of HTMLSession
r = session.get('https://www.coreyms.com/')  # making get request to the website. It returns the HTML object


csv_file = open('web_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video link'])

articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title', first=True).text
    summary = article.find('.entry-content p', first=True).text
    try:    
        video_id = article.find('iframe', first=True).attrs['src']
        video_id = video_id.split('/')[4]
        video_id = video_id.split('?')[0]
        video_link = f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        video_link = None
    print(headline)
    print(summary)
    print(video_link)
    print()

    csv_writer.writerow([headline, summary, video_link])

csv_file.close()



'''

# another way to get the links from webpage
for link in r.html.links:
    print(link)

'''

