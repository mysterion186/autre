# on prend 1 paramètre le statut du repo (true = privé, false = public)

pwd
var=$(pwd)
mydir="$(basename $PWD)"
echo "$mydir"

curl -H "Authorization: token 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 " --data '{"name":"'$mydir'"}' https://api.github.com/user/repos
touch .gitignore
echo .DS_Store > .gitignore
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mysterion186/"$mydir".git
git push -u origin main