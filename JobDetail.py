
class JobDetail:
    def __init__(self, job: str, company: str, link: str):
        self.job = job
        self.company = company
        self.link = link

    def print(self):
        print(self.job, self.company, self.link)
