# github-automatisation
Le but de ce programme est d'automatiser la création d'une repo Github et de le linker avec le projet sur notre machine locale. 
Pour ça on doit utiliser un token fournit par Github pour s'identier auprès de leurs API.
On ajoute ce fichier dans le PATH de notre machine pour pouvoir y accéder partout. 
Ainsi on crée une repo git portant le nom du dossier dans lequel on se trouver.

Problème : à chaque commit pour des raisons de sécurité Github révoque le token ainsi créé, ce qui rend difficile l'automatisation car on doit obtenir un nouveau token avant chaque création de commit
(c'est très fastidieux) 
