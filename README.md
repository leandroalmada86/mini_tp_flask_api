# Mini TP - Flask API

**Avant de commencer**
Faite des recherche sur la documentation [ici](https://flask.palletsprojects.com/en/1.1.x/) ainsi que sur le web sur Flask et essayez de comprendre les concepts/questions ci-dessous:  

1. Qu'est ce que flask et comment on lance une application. 
2. Comprendre ce qu'est un code HTTP, [wikipedia sur le sujet](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀
3. A quoi sert le `if __name__ = "__main__" ` ? 
4. Qu’est ce qu’une route ?
5. A quoi servent les fichiers statiques ? Qu’est ce qu’un template ?
6. A quoi sert le *Jinja2* ? 


**Quickstart** 

Ecrire une application flask suivant le modele ci-dessus avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello BG"
* une route qui renvoie "hello name", ou name est une variable string 
	* on devra donc trouver "hello name" à la route (http:localhost:5000/ma_route/name) avec la possibilité de changer la variable name. 
* refaite la meme chose en ajoutant un template 


**Contexte**

Vous avez répondu à l'appel d'offre d'une mairie qui consiste à digitaliser la bibliothèque de la commune. Il faudra pour cela proposer un "catalogue" en ligne de leur ressources et donner la possibilité au utilisateur du site de faire des recherches de livre. On supposera que la bibliothèque nous met à disposition ces livres via un fichier `.json` ci-dessous. 
Vous devez donc construire une api (application flask) avec les éléments suivants :

* Une home page à la racine de votre application (/) avec un titre "hello my app"
* instancier une variable `book` dans votre aopplication tel que : 
```
book=[
	{
		'id':1,
		'titre' : 'un titre',
	},
	{
		'id':2,
		'titre': 'un autre titre random',
	}
]
```
* faite une route `/api/books` avec une méthode `GET` qui retourne cette variable sous forme de json 
* faite une route qui retourne un book selon son `id` 
* faite une route qui retourne un book selon son titre 
* chager le fichier [books.json](https://drive.google.com/file/d/1UdRCm5d5UAPnfjGes_rHZl2kDQ9NNAsG/view?usp=sharing) et faite de même avec ce fichier
* **(bonus 1)** écrire un template pour le résultat de la recherche
* **(bonus 2)** Coder un site type vitrine/portfolio en flask et le déployer avec github pages