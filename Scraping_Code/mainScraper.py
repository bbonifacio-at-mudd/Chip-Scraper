import requests
from bs4 import BeautifulSoup
from subScraper import subScraper

class mainScraper():
    def __init__(self, main_url, directory):
        self.main_url = main_url
        self.directory = directory
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
        self.fetch_subpage_urls()

        # Process each subpage
        for url in self.subpage_urls:
            print(f"Processing {url}")
            sub_scraper = subScraper(url, self.directory)
            sub_scraper.run()
            raise Exception("Stop here")

# SubpageScraper class remains the same as before

if __name__ == '__main__':
    main_url = "http://chipguide.themogh.org/cg_state2.php?id=nv"
    directory = "Data/Chips"
    main_scraper = mainScraper(main_url, directory)
    main_scraper.run()
