import requests
from bs4 import BeautifulSoup


def scrape():
    base_url = "https://www.linkedin.com/jobs"
    searchCriteria = "search"
    location = "location=Canada"

    position = 1
    pageNum = 0

    while pageNum < 5:

        query = f"{searchCriteria}?{location}&pageNum={pageNum}"
        page = requests.get(base_url + f"/{query}")

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find("ul", class_="jobs-search__results-list")
        # jobs_list = results.findAll("div", "base-search-card__info")

        developer_jobs = results.findAll(
            "h2", string=lambda text: "developer" in text.lower()
        )
        print(len(developer_jobs))

        jobs_list = results.findAll("div", class_="base-card")

        for job_item in jobs_list:
            link = job_item.find("a", class_="base-card__full-link")["href"]
            job_title = job_item.find("h3", class_="base-search-card__title")
            company_name = job_item.find("h4", class_="base-search-card__subtitle")
            print(job_title.text.strip())
            print(company_name.text.strip())
            print(link)
            print("------------------------------------------------")

        pageNum += 1
        print(len(jobs_list))
