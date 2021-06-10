from bs4 import BeautifulSoup
import requests

'''
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')  # Retrieving the html text from the provided url using request.get method. It returns status code 200.
print(html_text)
'''

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text  # Retrieving the html text from the provided url using request.get method.
# print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    published_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in published_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", '')
        skills = job.find('span', class_="srp-skills").text
        print(f'''
    Company Name: {company_name}
    Required Skills: {skills}
    Published Date: {published_date}
    ''')