# on prend 1 paramètre le statut du repo (true = privé, false = public)

pwd
my_var="$(python3 Path/to/the/file/tokens.py)" # variable qui va contenir le token 
var=$(pwd)
mydir="$(basename $PWD)"
echo "$mydir"


curl -H "Authorization: token '$my_var' " --data '{"name":"'$mydir'"}' https://api.github.com/user/repos
touch .gitignore
echo .DS_Store > .gitignore
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/NOM_UTILISATEUR/"$mydir".git
git push -u origin main