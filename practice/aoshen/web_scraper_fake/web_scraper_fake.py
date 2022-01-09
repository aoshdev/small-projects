"""
Scraper of a fake python job site
https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping
"""

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# parses
soup = BeautifulSoup(page.content, "html.parser")

# 'div id' containing required data
results = soup.find(id="ResultsContainer")

# prettify
print(results.prettify())

# narrow down to the element we want
job_elements = results.find_all("div", class_="card-content")

# narrow down html using descriptive class names on some elements
# .text removes html wrapping
# .strip() removes spaces at beginning
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# extract text from html
