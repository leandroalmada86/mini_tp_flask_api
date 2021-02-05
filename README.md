# Mini TP - Flask API

**Avant de commencer**
Faite des recherche sur la documentation [ici](https://flask.palletsprojects.com/en/1.1.x/) ainsi que sur le web sur Flask et essayez de comprendre les concepts/questions ci-dessous:  

1. Qu'est ce que flask et comment on lance une application.

Flask est un micro framework open-source de développement web en Python. Il est classé comme microframework car il est très léger.

```ini
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask!'
```

sur la première ligne, nous importons la classe Flask.

sur la ligne 3, nous instancions la classe Flask et nous l'envoyons la variable __name__ comme paramètre.

ensuite nous utilisons le décorateur route() pour définir l'url à la quelle la méthode hello() sera accessible.

puis viens la méthode hello(), cette méthode défini la réponse à envoyer à l'utilisateur.

```console
> $ export FLASK_APP=app.py
> $ export FLASK_ENV=development
> $ flask run
```

2. Comprendre ce qu'est un code HTTP, [wikipedia sur le sujet](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP) 👀

En informatique, le code HTTP (aussi appelé code d'état) permet de déterminer le résultat d'une requête ou d'indiquer une erreur au client. Ce code numérique est destiné aux traitements automatiques par les logiciels de client HTTP.


3. A quoi sert le `if __name__ = "__main__" ` ? 
La variable __name__ varie selon le module dans lequel on se trouve durant l'exécution du programme. Dans le module principal, sa valeur sera égale à __main__. Si l'on se trouve dans un autre module importé, alors sa valeur sera égale au nom du module principal. Le test if (__name__ == __main__) permet de faire la distinction entre les deux cas. Cette condition est utilisée pour développer un module pouvant à la fois être exécuté directement mais aussi être importé par un autre module pour apporter ses fonctions. 


4. Qu’est ce qu’une route ?

En développement Web, on apelle route une URL ou un ensemble d’URLs conduisant à l’exécution d’une fonction donnée.
Dans Flask, les routes sont déclarées via le décorateur app.route, comme dans l’exemple ci-dessus.


5. A quoi servent les fichiers statiques ? Qu’est ce qu’un template ?

Ressources statiques
Une application Web ne se limite pas aux contenus HTML générés par les vues; on a également besoin de ressources statiques (CSS, images...).

Dans Flask, il est possible de stocker des fichiers dans un répertoire static, situé dans le même répertoire que le fichier Python définissant l’application.

L’URL de ces fichiers est donnée par la fonction url_for : 
```ini
url_for("static", filename="nom_du_fichier.css")
```


Un template, ou “modèle”, est un fichier dont certaines parties seront remplacées à l’exécution.

Voici un exemple minimaliste :
```ini
<p>Hello {{name}}</p>
```
Flask utilise le système de templates Jinja2, qui permet de générer n’importe quel format textuel (HTML, CSS...).

Les templates sont stockés dans un répertoire templates, situé dans le même répertoire que le fichier Python définissant l’application.

Pour appliquer un template, il suffit d’appeler la fonction flask.render_template en lui passant + le nom du template (relativ au répertoire templates), et + la liste des variables utilisées par le template :
```ini
@app.route("/hello/<n>")
def hello(n):
    return render_template("hello.html", name=n)
```


6. A quoi sert le *Jinja2* ? 
Jinja est un langage de création de modèles moderne et convivial pour Python, inspiré des modèles de Django. Il est rapide, largement utilisé et sécurisé avec l'environnement d'exécution de modèle en bac à sable en option.

Traits:

exécution en bac à sable

puissant système d'échappement HTML automatique pour la prévention XSS

héritage de modèle

compile le code Python optimal juste à temps

compilation de modèles à l'avance facultative

facile à déboguer. Les numéros de ligne des exceptions pointent directement vers la ligne correcte dans le modèle.

syntaxe configurable



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