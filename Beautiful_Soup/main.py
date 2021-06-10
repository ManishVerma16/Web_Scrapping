# Scrapping a sample html page


from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:   # opening the file in read mode
    content = html_file.read()              # reading the html file
    # print(content)                         # printing the content of html file

    soup = BeautifulSoup(content, 'lxml')   # reading the content using beautiful object and lxml parser
    # print(soup.prettify())                  # printing the content in readable format using prettify method
    
    '''
    # Extracting the text of h5 tags from home.html

    # tags = soup.find('h5')                  # find method is used to retrieve the  tags by spectifing in the ' '.
    courses_html_tags = soup.find_all('h5')                  # find method is used to retrieve the list of tag by spectifing in the ' '.
    # print(courses_html_tags)
    for course in courses_html_tags:            # Iterating through the list of course
        print(course.text)                      # printing the the main text

    '''

    course_card = soup.find_all('div', class_='card')   # grabbing all the div tags having class as card
    for course in course_card:
        # print(course)                                   # printing every div tag
        # print(course.h5)                                # printing the h5 tags
        # print(course.a.text)                            # printing the price

        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} cost {course_price}')