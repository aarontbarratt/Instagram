import logging
import urllib.request

logging.basicConfig(level=logging.DEBUG)

# URL = input()
# will grab the profile image if a link to a profile is supplied
# will pull the first image from a gallery
# will pull
URL = r"https://www.instagram.com/p/BxQmFKPl3tt/?utm_source=ig_web_copy_link"

CONTENT_STUB = "content=\"https://scontent"
response = ''
image_link = ''
image_links = []

export_path = r"C:\temp"
export_file_name = ''
export_file_extension = ''

request = urllib.request.Request(URL)

try:
    response = urllib.request.urlopen(request)
except ConnectionError:
    logging.error(ConnectionError)

html = response.read()
html = html.decode("utf8")
html = html.split()

for line in html:
    if CONTENT_STUB in line:
        image_link = line.strip("content=").strip("\"")
        image_links.append(image_link)

# remove all duplicated in image_links
image_links = list(dict.fromkeys(image_links))
print(image_links)

for link in image_links:
    print(link)
