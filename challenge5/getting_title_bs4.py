import requests
from bs4 import BeautifulSoup

url = "https://www.geeksforgeeks.org/"
reqs = requests.get(url)

soup = BeautifulSoup(reqs.text, "html.parser")

#displaying the title
print("Title of the website is:")
for title in soup.find_all("title"):
    print(title.get_text())
