import requests
from flask import Flask
app=Flask(__name__)
#@app.route('/')

url = "https://imdb8.p.rapidapi.com/auto-complete"
req=input("enter what to search:")
querystring = {"q": req}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "a8ec5bd855mshda8fd2635d17aafp1d071cjsn34f7b522f846"
}
r = requests.request("GET", url, headers=headers, params=querystring)
data = r.json()["d"]
print(data)
for item in data:
    ide=item["id"]
    name=item["l"]
    img=item["i"]["imageUrl"]
    print("id:"  + str(ide))
    print("name:" + name)
    print("poster: " + img)
    print("\n")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()


