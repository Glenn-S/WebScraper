import requests
from bs4 import BeautifulSoup
from JobDetail import JobDetail


def scrape():
    base_url = "https://www.linkedin.com/jobs"
    location = "location=Calgary"

    job_listings = []

    while True:
        try:
            page_num = 0
            query = f"search?keywords=Software%20development&{location}&pageNum={page_num}"
            page = requests.get(base_url + f"/{query}")

            soup = BeautifulSoup(page.content, "html.parser")

            results = soup.find("ul", class_="jobs-search__results-list")

            jobs_list = results.findAll("div", class_="base-card")

            for job_item in jobs_list:
                link = job_item.find("a", class_="base-card__full-link")["href"]
                job_title = job_item.find("h3", class_="base-search-card__title")
                company_name = job_item.find("h4", class_="base-search-card__subtitle")
                job_detail = JobDetail(job=job_title.text.strip(), company=company_name.text.strip(), link=link)
                job_listings.append(job_detail)

            page_num += 1
        except Exception as ex:
            print(ex)
            break

    return job_listings
