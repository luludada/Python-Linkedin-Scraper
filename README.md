# Python-Linkedin-Scraper
Python LinkedIn Scraper (currently working 2020)
* Supports Python3. 

This scraper will take a list of linkedin profile urls in csv file. 

This scraper will extract the available data and store to a csv file:
* Profile: name, title, location, description and url
* Experiences: title, company name, location, duration, start date and end date
* Education: school name, degree name, start date and end date
* Skills: name

## Inspiration
Thanks to David Craven's [article](https://www.linkedin.com/pulse/how-easy-scraping-data-from-linkedin-profiles-david-craven/).

## Getting started

1. In order to scrape LinkedIn profiles, you need to make sure the scraper is logged-in into LinkedIn. 
2. Install [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads).
3. Install prerequisite for Python3
    ```Python
    pip3 install selenium
    pip3 install csv
    pip3 install time
    pip3 install pandas
    pip3 install BeautifulSoup
    pip3 install random
    pip3 install traceback
    ```
    
## Usage
 ```Python
 python3 linkedin-scraper.py example.csv
 ```
