import tutorialScraper
import linkedInScraper
import dotenv
import os

# https://realpython.com/beautiful-soup-web-scraper-python/


# Tutorial based code. Write a real web scraper now
def main():
    dotenv.load_dotenv("./.env")
    test = os.getenv("TEST")
    print(test)

    # tutorialScraper.scrape()
    linkedInScraper.scrape()


if __name__ == '__main__':
    main()
