import requests
import json
import sqlite3
import pandas as pd

from urllib.request import urlopen
from flask import Flask
#app=Flask(__name__)
#@app.route('/')
api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
isbn = input("Enter 10 digit ISBN: ").strip()

# send a request and get a JSON response
resp = urlopen(api + isbn)
# parse JSON into Python as a dictionary
book_data = json.load(resp)


# create additional variables for easy querying
volume_info = book_data["items"][0]["volumeInfo"]
author = volume_info["authors"]
get_with_title=volume_info['title']
# practice with conditional expressions!
prettify_author = author if len(author) > 1 else author[0]

# display title, author, page count, publication date
# fstrings require Python 3.6 or higher
# \n adds a new line for easier reading
print(f"\nTitle: {volume_info['title']}")
print(f"Author: {prettify_author}")
print(f"Page Count: {volume_info['pageCount']}")
print(f"Publication Date: {volume_info['publishedDate']}")
print("\n***\n")

#print("get_with_title : " + get_with_title)

url = "https://imdb8.p.rapidapi.com/auto-complete"
#req=input("enter what to search:")
querystring = {"q": get_with_title}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "a8ec5bd855mshda8fd2635d17aafp1d071cjsn34f7b522f846"
}

r = requests.request("GET", url, headers=headers, params=querystring)

data = r.json()["d"]
print(data)

conn= sqlite3.connect('movies.db')
c=conn.cursor()
c.execute('''drop table movie''')
c.execute('''create table movie( id number,name text,img txt)''')

for item in data:
    ide=item["id"]
    name=item["l"]
    img=item["i"]["imageUrl"]

    c.execute('''insert into movie values(?,?,?)''',(ide,name,img))
    print("id:"  + str(ide))
    print("name:" + name)
    print("poster: " + img)
    print("\n")

conn.commit()
c.execute('''select * from movie''')
results=c.fetchall()
print(results)
df=pd.read_sql_query('select *   from movie',conn)
print(df)
conn.close()
# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
 #   app.run()


