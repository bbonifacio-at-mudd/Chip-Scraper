import requests
image_url = "http://themogh.org/cg_pix/nv/s/19605.jpg"
response = requests.get(image_url)
with open('19605.jpg', 'wb') as file:
    file.write(response.content)
    print("Image downloaded successfully")

