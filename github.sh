# on prend 1 paramètre le statut du repo (true = privé, false = public)

pwd
my_var="$(python3 /Full/Path/To/The/File/tokens.py)" # variable qui va contenir le token 
var=$(pwd)
mydir="$(basename $PWD)"
echo "$mydir"
echo "$my_var"
curl -H "Authorization: token "$my_var" " --data '{"name":"'$mydir'","private":'$1'}' https://api.github.com/user/repos
touch .gitignore
touch readme.md
echo .DS_Store >> .gitignore
echo \#"($mydir)" >> readme.md
git init
git add readme.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/USERNAME/"$mydir".git
git push -u origin main