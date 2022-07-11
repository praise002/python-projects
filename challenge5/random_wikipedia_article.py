"""
The %s operator is put where the string is to be specified.
The number of values you want to append to a string should be
equivalent to the number specified in parentheses after the % operator at the end of the string value.
"""

import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title}\nDo you want to view it?(Y/N) ")
    ans = input().lower()
    if ans == "y":
        url = f"https://en.wikipedia.org/wiki/{title}"
        webbrowser.open(url)
        break
    elif ans == "n":
        print("Try again")
        continue
    else:
        print("Wrong choice!")
        break

