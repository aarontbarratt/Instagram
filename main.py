import logging
import time
import urllib.request

logging.basicConfig(level=logging.DEBUG)

# URL = input()
# will grab the profile image if a link to a profile is supplied
# will pull the first image from a gallery
# will pull 
URL = r"https://www.instagram.com/lukejinks/"

CONTENT_STUB = "content=\"https://scontent"
response = ''
image_link = ''

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
        image_link = line

image_link = image_link.strip("content=").strip("\"")

logging.info(" Image Found: " + image_link)

if "mp4" in image_link:
    export_file_extension = "mp4"
elif "jpg" in image_link:
    export_file_extension = "jpg"

export_full_path = export_path + "\\" + str(time.time()) + "." + export_file_extension

logging.info(" Export: " + export_full_path)
urllib.request.urlretrieve(image_link, export_full_path)
