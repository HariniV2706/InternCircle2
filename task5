import requests

k="11427720142b65d06889059819a14d14"
c=input("Enter city: ")

u="https://api.openweathermap.org/data/2.5/weather"
p={"q":c,"appid":k,"units":"metric"}

try:
    r=requests.get(u,params=p,timeout=10)
    d=r.json()

    if r.status_code!=200:
        print("City not found")
    else:
        print("City:",d["name"])
        print("Temperature:",d["main"]["temp"],"C")
        print("Humidity:",d["main"]["humidity"],"%")
        print("Weather:",d["weather"][0]["description"])

except requests.RequestException:
    print("Network error")
except KeyError:
    print("Invalid response")
