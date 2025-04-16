
from bs4 import BeautifulSoup
import requests
from Course import Course 
import json
import ipdb

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        # more code coming soon!
        doc = BeautifulSoup(requests.get(
            "http://learn-co-curriculum.github.io/site-for-scraping/courses").text, 'html.parser')
        # ipdb.set_trace()
        return doc

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        for course in self.get_courses():

            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses
    def print_courses(self):
        for course in self.make_courses():
            print(course)

