from EmailClient import send_email
import linkedInScraper
import dotenv
import os


# TODO Now that the initial code has been figured out, modify to
# add in some testing, make more robust and decouple.
def main():
    dotenv.load_dotenv("./.env.local")
    send_grid = os.getenv('SENDGRID_API_KEY')
    print(send_grid)

    results = linkedInScraper.scrape()

    from_email = os.getenv('FROM_EMAIL')
    to_email = os.getenv('TO_EMAIL')

    html_results = process_results(results)
    print(html_results)

    send_email(
        send_from=from_email,
        send_to=to_email,
        subject='LinkedIn Job Postings',
        body=html_results,
        api_key=send_grid)


def process_results(results):
    message = "<html><body>"
    message = message + "<h1>Hello Glenn, here are your job results for the day</h1>"

    message = message + "<ul>"
    for result in results:
        job = result.job
        company = result.company
        link = result.link
        message = message + f"<li style=\"padding:10px 0px;\"><strong>{company}</strong><a style=\"display:inline-block;padding-left:5px;\" href=\"{link}\">{job}</a></li>"
        # print(job, company, link)
    message = message + "/ul"

    message = message + "</body></html>"
    return message


if __name__ == '__main__':
    main()
