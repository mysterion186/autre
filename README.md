# github-automatisation
Le but de ce programme est d'automatiser la création d'une repo Github et de le linker avec le projet sur notre machine locale. 
Pour ça on doit utiliser un token fournit par Github pour s'identier auprès de leurs API.
On ajoute ce fichier dans le PATH de notre machine pour pouvoir y accéder partout. 
Ainsi on crée une repo git portant le nom du dossier dans lequel on se trouver.

Instruction pour l'utiliser : 
  - Taper la commande  ```pip install -r requirements.txt``` pour installer les modules nécessaires
  -  Installer chromedriver [lien](https://chromedriver.chromium.org/downloads) 
  -  Mettre à jour les differentes valeurs dans le fichier sous forme de string 
  -  créer un fichier log.json qui va avoir cette structure (au niveau du fichier tokens.py):
    
    {
        "email":"adresse mail",
        "password" : "mot de passe github",
        "username":"nom d'utilisateur github"
    }
  - Mettre le fichier ```github.sh``` dans le PATH de votre ordinateur en lui donnant les droits d'exécution
