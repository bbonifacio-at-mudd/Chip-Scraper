# Chip Scraper Documentation

This repository is structured as follows. 
- Data: the scraped images of chips, uncropped. To see Cropped images, go to https://github.com/bbonifacio-at-mudd/Dataset-Creation/tree/main
- Scraping_Code: the code for scraping the Table Chips database. There are two main classes:
  - mainScraper.py: the main scraper that scrapes the main page for subpage urls
  - subScraper.py: sub scraper that scrapes the subpages and saves data
- Source_htmls: important htmls from the website, useful for analyzing

By only saving "Table Chips", which excludes slot tokens, pieces of paper, etc, I scraped ~4000 top-down images of Table Chips like the ones below. I crop and clean up the dataset in the Dataset-Creation repo. 
![image](https://github.com/bbonifacio-at-mudd/Chip-Scraper/assets/114462423/ef792894-1e9a-48be-b3a9-559704b4b356)


TODO:

- DONT GET IP BANNED 
- Clean up file storage, Ask Sam/George how files should be stores
- Clean up metadata storage
- 
