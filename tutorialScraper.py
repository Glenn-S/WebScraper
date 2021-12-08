import requests
from bs4 import BeautifulSoup



# https://realpython.com/beautiful-soup-web-scraper-python/
# Tutorial code
def tutorialScraper():
    url = "https://realpython.github.io/fake-jobs/"
    page = requests.get(url)
    print(page.text)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("div", {"id": "ResultsContainer"})
    print(results.prettify())

    job_elements = results.findAll("div", class_="card-content")
    print(job_elements)

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

    python_jobs = results.findAll(
        "h2", string=lambda text: "python" in text.lower()
    )
    print(len(python_jobs))

    # list comprehension
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job_element in python_job_elements:
        # -- snip --
        links = job_element.findAll("a")
        for link in links:
            print(link.text.strip())
            link_url = link["href"]
            print(f"Apply here: {link_url}\n")