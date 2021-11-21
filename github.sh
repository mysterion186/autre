# on prend 1 paramètre le statut du repo (true = privé, false = public)

pwd
my_var="$(python3 /Full/Path/To/The/File/tokens.py)" # variable qui va contenir le token 
var=$(pwd)
mydir="$(basename $PWD)"
# check qu'il n'y a pas de paramètres supplémentaire qui indique qu'on veut donner un nom personalisée
if [ -z "$2" ]
	then
		mydir = "$(basename $PWD)"
else
	mydir="$2"
fi
echo "$my_var"
curl -H "Authorization: token "$my_var" " --data '{"name":"'$mydir'","private":'$1'}' https://api.github.com/user/repos
touch .gitignore
echo \# "$mydir" >> readme.md
git init
touch readme.md
git add readme.md
echo .DS_Store >> .gitignore
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mysterion186/"$mydir".git
git push -u origin main