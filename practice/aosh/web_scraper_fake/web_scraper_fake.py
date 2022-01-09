"""
Scraper of a fake python job site
https://realpython.com/beautiful-soup-web-scraper-python/#what-is-web-scraping
https://www.edureka.co/blog/web-scraping-with-python/

1. Parse html using BeautifulSoup
2. Find <div> element with required content
3. Look at parent(s) folder of searchable element
4. Loop and save to list
5. Output to csv
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

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
    # print(title_element.text.strip())
    # print(company_element.text.strip())
    # print(location_element.text.strip())
    # print()

# or pass function to beautiful soup method
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# taking parent x3 as great-grandparent class contains all relevant info to the job
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# lists to store loops
titles = []
companies = []
locations = []
urls = []

# loop over only the python related jobs
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    
    link_url = links[1]["href"]
    print(f"Apply here: {link_url}\n")

    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    titles.append(title_element.text.strip())
    companies.append(company_element.text.strip())
    locations.append(location_element.text.strip())
    urls.append(link_url)

# output to csv
df = pd.DataFrame({'Title':titles,'Company':companies,'Location':locations,'Link':urls})
df.to_csv(f"{os.path.dirname(__file__)}/python-jobs.csv", index=False)