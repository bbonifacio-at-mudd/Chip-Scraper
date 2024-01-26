import requests
from bs4 import BeautifulSoup
import csv
import os

class subScraper():
    def __init__(self, url, directory):
        self.results = []
        self.headers = {}
        self.url = url
        self.directory = directory

    def fetch_info(self, params):
        # Request info with self.url
        response = requests.get(self.url, headers=self.headers, params=params)

        if response.status_code == 200:
            # Parse the HTML content
            content = BeautifulSoup(response.content, 'html.parser')

            # DATA IS STORED IN TABLES that are class 'chips'
            # Find all 'table' elements with class 'chips'
            chip_tables = content.find_all('table', class_='chips')

            for table in chip_tables:
                # Extracting image URLs
                image_tags = table.find_all('td', class_='chippics')
                image_urls = [img.find('img')['src'] for img in image_tags if img.find('img')]

                # Extracting chip info
                chip_info_tag = table.find('td', class_='chipinfo')
                chip_info = chip_info_tag.get_text(separator=' ', strip=True) if chip_info_tag else ""

                # Add to results
                self.results.append({
                    'image_urls': image_urls,
                    'chip_info': chip_info
                })

        else:
            print(f"Failed to fetch page. Status code: {response.status_code}")

    def to_csv(self):
        # Make directory if it doesn't exist
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        with open(os.path.join(self.directory, 'chipInfo.csv'), 'w+', newline='') as csv_file:
            fieldnames = ['image_urls', 'chip_info']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for result in self.results:
                writer.writerow(result)

    def download_images(self):
        # Create directory if it doesn't exist
        folder_name = self.directory
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Parse through image urls and downlad them
        for result in self.results:
            for img_url in result['image_urls']:
                response = requests.get(img_url)
                if response.status_code == 200:
                    file_path = os.path.join(folder_name, img_url.split('/')[-1])
                    with open(file_path, 'wb') as file:
                        file.write(response.content)

    def run(self):
        # Step 1: Get the info from the main page
        self.fetch_info(None)
        # Step 2: Save the results to CSV
        self.to_csv()
        # Step 3: Download images
        self.download_images()


if __name__ == '__main__':
    url = "http://chipguide.themogh.org/cg_chip2.php?id=NVNL11&v=1721189917"
    directory = "Data/101 Club"
    scraper = subScraper(url, directory)
    scraper.run()
