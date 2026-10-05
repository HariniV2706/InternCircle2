import requests
from bs4 import BeautifulSoup
import json

u="https://quotes.toscrape.com/"
try:
    r=requests.get(u,timeout=10)
    r.raise_for_status()
    s=BeautifulSoup(r.text,"html.parser")
    d=[]

    for q in s.select(".quote"):
        t=q.select_one(".text").get_text(strip=True)
        a=q.select_one(".author").get_text(strip=True)
        d.append({"quote":t,"author":a})

    with open("quotes.json","w") as f:
        json.dump(d,f,indent=2)

    print("Quotes saved")
    for x in d:
        print(x["author"],":",x["quote"])

except requests.RequestException:
    print("Unable to fetch data")
except Exception:
    print("Something went wrong")
