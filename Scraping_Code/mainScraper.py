import requests
from bs4 import BeautifulSoup
from subScraper import subScraper

class mainScraper():
    def __init__(self, main_url):
        self.main_url = main_url
        self.subpage_urls = []

    def fetch_subpage_urls(self):
        response = requests.get(self.main_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('cg_chip2.php'):
                    full_url = f'http://chipguide.themogh.org/{href}'
                    self.subpage_urls.append(full_url)
        else:
            print(f"Failed to fetch main page. Status code: {response.status_code}")

    def run(self):
        # Fetch all subpage URLs
        print("fetching subpage urls")
        self.fetch_subpage_urls()
        print("urls fetched")

        # Process each subpage
        for index, url in enumerate(self.subpage_urls):
            print(f"Processing {url}")
            sub_scraper = subScraper(url, f"Data/Chips/{index}")
            sub_scraper.run()

if __name__ == '__main__':
    main_url = "http://chipguide.themogh.org/cg_state2.php?id=nv"
    main_scraper = mainScraper(main_url)
    main_scraper.run()
