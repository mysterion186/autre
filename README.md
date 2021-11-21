# github-automatisation
Le but de ce programme est d'automatiser la création d'un repo Github et de le linker avec le projet sur notre machine locale. 
Pour ça on doit utiliser un token fournit par Github pour s'identier auprès de leurs API.



Instruction pour l'utiliser : 
  - Taper la commande  ```pip install -r requirements.txt``` pour installer les modules nécessaires
  -  Installer chromedriver [lien](https://chromedriver.chromium.org/downloads) 
  -  Mettre à jour les differents chemin d'accès dans les fichiers :
      -  ligne 67 du fichier ```tokens.py``` : mettre le chemin d'accès de ```chromedriver``` 
      -  ligne 4 du fichier ```github.sh``` : mettre le chemin abslolue du fichier ```tokens.py```
      -  ligne 18 du fichier ```github.sh``` : mettre son nom d'utilisateur dans l'adresse url
  -  créer un fichier ```log.json``` qui va avoir cette structure (dans le même répertoire que ```tokens.py```):
    
    {
        "email":"adresse mail",
        "password" : "mot de passe github",
        "username":"nom d'utilisateur github"
    }
  - Mettre le fichier ```github.sh``` dans le PATH de votre ordinateur en lui donnant les droits d'exécution

  Après avoir fait les modifications d'au-dessus, pour pouvoir exécuter le programme il faut taper la commande : 
  ```github repo_statuts [nom_du_repo]```où  ```repos_statut```est le statut public/privé du repo ```[nom_du_repo]```est facultatif
