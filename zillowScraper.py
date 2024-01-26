import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import sys
import re
class ZillowScraper():
    results = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'Cookie': 'x-amz-continuous-deployment-state=AYABeI1Uby5XvE3d37fZ+ljICW0APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxNTk1MzcxVEJNNTJaWDdPU09PAAEAAkNEABpDb29raWUAAACAAAAADPPUeZ6J+k4chJXW%2FAAwTPSQyhjvKe2iW2f7PumWWoNa166qaYRmA1BpN0YX6o+RtYnuzfo9PvKeze0qYL+GAgAAAAAMAAQAAAAAAAAAAAAAAAAAAA4XTGmPQ618IetZ%2Ftt7%2FCj%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAyKFKXqHJWf8sBIyNCwdWRt44q7DUn+VBP93jRh; zguid=24|%245f615d8f-7f11-4346-9955-3cabb6a0b6a2; _ga=GA1.2.1981000125.1674034255; zg_anonymous_id=%2279509633-51b7-4604-a3f7-565ec6601a45%22; zjs_anonymous_id=%225f615d8f-7f11-4346-9955-3cabb6a0b6a2%22; _pxvid=cf718d70-9712-11ed-8fe4-426f66587a52; _fbp=fb.1.1674034258084.322345096; _pin_unauth=dWlkPU5EUTVNVEJrWlRRdE1tUmhNQzAwWmpjeUxXSXhObVF0TVRoaE56SmhOek15T0RZMA; __pdst=055e585304c6406190998187dacb1702; __gads=ID=6213b6e26dc63218:T=1674034270:S=ALNI_MYfO9pF0AC7Qy6lVZ0Rccaq1HdVWA; _cs_c=0; optimizelyEndUserId=oeu1674166171542r0.2969864561473514; zgcus_aeuut=AEUUT_f56beeb0-9845-11ed-bc8b-7e16ac67f166; G_ENABLED_IDPS=google; _derived_epik=dj0yJnU9dkhJZjlrNUYxejJqM3ZHMXRvSGFnb1Ixc2t6OVo0Qm8mbj1FWTBTb0xTMG01bzhfME5Od1dNTFBBJm09MTAmdD1BQUFBQUdQSndyTSZybT0xMCZydD1BQUFBQUdQSndyTSZzcD0x; userid=X|3|20c381f16ffeb5b4%7C4%7CV-ggUXJ7dx6XKq0iFPybyyyYoc6AZwUOiUP37vNqH4M%3D; loginmemento=1|00d80ed866cb43fc86acfa724c86db46f13fd5a01657ce1116f3129129281485; zjs_user_id=%22X1-ZUtikzp4h8vqq1_4srxs%22; zgcus_lbut=; zgcus_aeut=169201253; zgcus_ludi=3a3f5ef2-a29d-11ed-8a79-ea4e2dd6970c-16920; g_state={"i_p":1678376692308,"i_l":4}; _cs_id=4ca7ebb8-5708-ad89-fac1-af7356ec5df8.1674166171.4.1676702336.1676702336.1.1708330171889; _hp2_id.1215457233=%7B%22userId%22%3A%224022808386978627%22%2C%22pageviewId%22%3A%224041020577465247%22%2C%22sessionId%22%3A%228836766344443842%22%2C%22identity%22%3A%22X1-ZUtikzp4h8vqq1_4srxs%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; JSESSIONID=E017D00766E7EAAA0A660EF3DFCD37FF; zgsession=1|43b1bc6e-4dca-45a2-810c-2fc198f47430; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEhrzYoccfe5Ci3Di5ndRA4%2FpWmzMLk3h7kWwbWg8nABpjkqaqRy5pewpU09TIrYNzRa94P%2F4WqtJ; _gid=GA1.2.2113148857.1684178436; pxcts=9381da9d-f355-11ed-820a-547448596744; x-amz-continuous-deployment-state=AYABeBsYNx0hRcjwtbYbIwWWxvEAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzAxNTk1MzcxVEJNNTJaWDdPU09PAAEAAkNEABpDb29raWUAAACAAAAADCFWgqeeI167%2FjnOqQAwrliKQDR3J2PFZvo%2F2JVD80sB4NMqjvkeuBNuAVKjwhO7KaE7eAFvgY1p3AvzZ+f1AgAAAAAMAAQAAAAAAAAAAAAAAAAAABgevGH1xBzE6qdGdSIQe8%2F%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAz%2FjS4ocJ27EWS7RRqy8Pt6IoWldOgmLQlqQ6xB; _gcl_au=1.1.1685604986.1684178447; DoubleClickSession=true; __gpi=UID=0000092cc513affd:T=1674034270:RT=1684178450:S=ALNI_Mavucbq-70I527_KZyUHEnskgMk6Q; _clck=5kv0pj|2|fbm|0|1230; search=6|1686770575791%7Cregion%3Dnew-york-ny%26rect%3D40.917577%252C-73.700272%252C40.477399%252C-74.25909%26disp%3Dmap%26mdm%3Dauto%26listPriceActive%3D1%26lt%3Dfsbo%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%096181%09%09%09%09%09%09; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; _gat=1; _uetsid=990f7ff0f35511edb5a42d9a25585630; _uetvid=d08838e0971211ed8fb8d5cd369bcf6e; _clsk=14hskr5|1684178584888|3|0|i.clarity.ms/collect; AWSALB=4yrJP4bat453TgKuk18w2hYFFehNv7hzAiK1Fd1Gri/pIcxNCCAgW3Yey5lja3Aq3L9TEECoQfcBa8UsE/xPgGVPyarzBpgijgg6F1Aa+S79PAMQC1YXHBRf8kVK; AWSALBCORS=4yrJP4bat453TgKuk18w2hYFFehNv7hzAiK1Fd1Gri/pIcxNCCAgW3Yey5lja3Aq3L9TEECoQfcBa8UsE/xPgGVPyarzBpgijgg6F1Aa+S79PAMQC1YXHBRf8kVK; _pxff_rf=1; _pxff_fp=1; _pxff_tm=1; _px3=2c009e903ab3122f29d1a53f83895276686432302c742db1aa13675b3c55f9bd:jdl/M0/K548RStpY0KATi00Pxpa6DtA0x5JigakK+/b5kcfhKxY/T7MKHd0oG1cr0So0eqo5omTd63c11iJ9pw==:1000:kgHybf6LVgg275qitCyH/7sOJBt4Y4AZIkLsj78QNqWXPQ/ytbQcArU9ZwuIM1k/7JKdtWBMXQHjfNWQmgYkaQqwyeq+z4sUQ/Ao7LOEtlsdrUYODC2XozGoQqpSWrxiuvOteaoC4syteDk9rJGASGrQ+rxWahYZFg3dR8hSjJwpYy9cO6h5TGqzChHe+rfijWW1Teq23ci6nOj4P65lBA==',
        'Referer': 'https://www.zillow.com/captchaPerimeterX/?url=%2fnew-york-ny%2ffsbo%2f%3fsearchQueryState%3d%257B%2522pagination%2522%253A%257B%257D%252C%2522mapBounds%2522%253A%257B%2522north%2522%253A41.0151700254506%252C%2522south%2522%253A40.3790143859455%252C%2522east%2522%253A-73.43997763085936%252C%2522west%2522%253A-74.51938436914061%257D%252C%2522regionSelection%2522%253A%255B%257B%2522regionId%2522%253A6181%252C%2522regionType%2522%253A6%257D%255D%252C%2522isMapVisible%2522%253Afalse%252C%2522category%2522%253A%2522cat2%2522%252C%2522filterState%2522%253A%257B%2522fsba%2522%253A%257B%2522value%2522%253Afalse%257D%252C%2522nc%2522%253A%257B%2522value%2522%253Afalse%257D%252C%2522cmsn%2522%253A%257B%2522value%2522%253Afalse%257D%252C%2522auc%2522%253A%257B%2522value%2522%253Afalse%257D%252C%2522fore%2522%253A%257B%2522value%2522%253Afalse%257D%252C%2522sort%2522%253A%257B%2522value%2522%253A%2522globalrelevanceex%2522%257D%257D%252C%2522isListVisible%2522%253Atrue%257D&uuid=e5441f10-f355-11ed-ba2a-25e18df9c286&vid=cf718d70-9712-11ed-8fe4-426f66587a52',
        'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36'}
    def fetch_info(self, url, params):
        time.sleep(1)
        response = requests.get(url, headers=self.headers, params=params)
        content = BeautifulSoup(response.text, 'lxml')
        content = content.prettify().encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)
        #print(content)
        #largepattern = r'"streetAddress":"(.*?)","zipcode":"(.*?)","city":"(.*?)","state":"(.*?)","latitude":(.*?),"longitude":(.*?),"price":(.*?),"bathrooms":(.*?),"bedrooms":(.*?),"livingArea":(.*?),"homeType":"(.*?)",'
        #largepattern = r'"homeInfo":({.*?})'
        #largeMatches = re.findall(largepattern, content)
        #Extract elements in largepattern into a list of
        #largeMatches = [list(largeMatch) for largeMatch in largeMatches]
        # Convert the extracted dictionaries from string to Python dict
        #largeMatches = [json.loads(match) for match in largeMatches]
        largepattern = r'"homeInfo":({.*?})'
        largeMatches = []
        
        matches = re.finditer(largepattern, content)
        
        for match in matches:
            largeMatches.append(json.loads(match.group(1)))

        print(largeMatches)

        
        
        
        
        
        
        
        #largeMatches = [match for match in largeMatches if "datePriceChanged" not in match[6]]
        #largeMatches = [match for match in largeMatches if "LOT" not in ' '.join(match)]
        # get rid of largematches when the number of bedrooms is not a float
        #largeMatches = [match for match in largeMatches if match[8].isdigit()]
        # Get rid of largematches when the addressRegion length is longer than 4
        #largeMatches = [match for match in largeMatches if len(match[3]) <= 4]
        print("LargeMatches", len(largeMatches))
        # Append each of the values to the result
        if largeMatches:
            for largeMatch in largeMatches:
                self.results.append({
                    'price': largeMatch[6],
                    'name': largeMatch[0],
                    'floorSize': largeMatch[9],
                    'streetAddress': largeMatch[0],
                    'addressLocality': largeMatch[2],
                    'addressRegion': largeMatch[3],
                    'postalCode': largeMatch[1],
                    'latitude': largeMatch[4],
                    'longitude': largeMatch[5],
                    'bedrooms': largeMatch[8],
                    'bathrooms': largeMatch[7],
                    'homeType': largeMatch[10]
                })
    def to_csv(self):
        with open('WashingtonFSBO.csv', 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.results[0].keys())
            writer.writeheader()
            writer.writerows(self.results)
    def run(self):
        for page in range(3, 4):
            print(f"Page: {page}")
            if page != 1:
                url = f'https://www.zillow.com/wa/fsbo/{page}_p/'
            else:
                url = 'https://www.zillow.com/wa/fsbo/'
            print(url)
            params = {
                "pagination": '{"currentPage": %s},"mapBounds":{"north":41.0151700254506,"south":40.3790143859455,"east":-73.43997763085936,"west":-74.51938436914061},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":false,"category":"cat2","filterState":{"fsba":{"value":false},"nc":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"fore":{"value":false},"sort":{"value":"globalrelevanceex"}},"isListVisible":true}' %page
            }
            self.fetch_info(url, params)
        self.to_csv()
if __name__ == '__main__':
    scraper = ZillowScraper()
    scraper.run()