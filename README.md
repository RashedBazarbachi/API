# API 
Ce projet a pour but de détérminer, selon le choix de l'utilisateur, des films qui ont été interprétés en films. Nous avons utilisé 3 files: 

1. ISBN: le code qui utilise l'API des livres. 
Dans ce programme nous parcourons l'API des livres dans laquelle nous pouvons accéder à partir de ce lien : https://www.googleapis.com/books/v1/volumes?q=isbn. On rentre alors l'ISBN d'un film pour récupérer les informations qui nous permettent de retrouver le livre souhaité (volum info, qui contient: le titre, le nombre de pages et, date de publication et le nom de l'auteur) 

2. movies: le code qui utlise l'API des films.
Dans ce programme nous utilisons une API qui n'est pas totalment gratuite, nous aurons besoin d'une clé pour pouvoir y accéder (avec ce code : 
' headers = {
 'x-rapidapi-host': "imdb8.p.rapidapi.com",
4
    'x-rapidapi-key': "a8ec5bd855mshda8fd2635d17aafp1d071cjsn34f7b522f846" '
en utilisant cet adresse pour accéder à l'API en question : 'imdb8.p.rapidapi.com'. 
'url = "https://imdb8.p.rapidapi.com/auto-complete"
req=input("enter what to search:")
querystring = {"q": req}' Ce code nous permet d'entrer le nom du livres que nous voulons trouver dans l'API films.
Ensuite nous utilisons la fonction GET() pour pouvoir récupérer toutes les informations du film réalisé à partir d'un livre : 
'r = requests.request("GET", url, headers=headers, params=querystring)
data = r.json()["d"]
print(data)
for item in data:
    ide=item["id"]
    name=item["l"]
    img=item["i"]["imageUrl"]
    print("id:"  + str(ide))
    print("name:" + name)
    print("poster: " + img)
    print("\n") '

3. Book-Movies : le code qui lie entre les deux dernier files
Enfin, Ce programme prend la sortie du programme ISBN pour le mettre en entrée dans la programme MOVIES pour récupérer les livres qui ont été interprétés en films (ceux qui ont étés retrouver dans l'API films) et les mettre dans une base de donnée en utilisons Sqlite3​.


Vous retrouverez la base de données utilisée dans les fichier du Git Hub et tout les programmes.


