# module pour pouvoir utiliser selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
# module pour faire du scraping 
from bs4 import BeautifulSoup

import json,time,random, os
# module pour obtenir le chemin 
from pathlib import Path 
# module pour gérer les dates
import datetime

# fonction pour vérifier si un fichier token.txt (avec un token valide)
# existe si non le créer 
def get_token_txt(file_name="token.txt"):
    Base_Dir = str(Path(__file__).resolve().parent)
    today = datetime.datetime.now()
    # si le fichier existe 
    if os.path.isfile(Base_Dir+'/'+file_name):
        with open(Base_Dir+'/'+file_name) as f:
            a = f.readline()
        # on vérifie si la date est inférieur à 29 jours (pour régler les heures)
        date = a.split(' ')[0]
        #print(date)
        year,month,day = date.split('-')
        token_day = datetime.datetime(year=int(year),month=int(month),day=int(day))
        # cas token perimé
        #print((token_day-today).days)
        if (token_day-today).days <= 0 :
            new_token = get_token()
            with open(Base_Dir+'/'+file_name,"w") as f :
                f.write(str(today+datetime.timedelta(30))+" | "+new_token)
            return new_token
        # cas token encore valide
        else : 
            new_token = a.split(' | ')[1]
            return new_token
    else : 
        # on crée un fichier text
        new_token = get_token()
        with open(Base_Dir+'/'+file_name,"w") as f :
            f.write(str(today+datetime.timedelta(30))+" | "+new_token)
        # ajouter ce fichier dans token.txt
        return new_token


# fonction pour obtenir les identifiants de l'utilisateur
def get_id(file_name="log.json"):
    Base_Dir = str(Path(__file__).resolve().parent)
    f = open(Base_Dir+'/'+file_name)
    data = json.load(f)
    f.close()
    return [data[keys] for keys in data.keys()]

# fonction pour se connecte
def login(driver,email,mdp):
    driver.find_element_by_id('login_field').send_keys(email)
    driver.find_element_by_id('password').send_keys(mdp)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
    return driver

# fonction pour obtenir le tokens de l'utilisateur
def get_token():
    # initialisation du webdriver 
    chrome_options = Options()
    chrome_options.add_argument("--headless") # on lance le programme sans afficher la fenêtre 

    driver = webdriver.Chrome(executable_path="Path/to/your/chromedriver",options=chrome_options)

    #url pour se connecter à github et créer des tokens 
    url = "https://github.com/settings/apps"
    driver.get(url)

    email,mdp,username = get_id()   

    # équivalent pour se connecter
    driver.find_element_by_id('login_field').send_keys(email)
    driver.find_element_by_id('password').send_keys(mdp)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()

    # lien pour supprimer tous les tokens existants
    token_revoque_url = "https://github.com/settings/tokens"
    driver.get(token_revoque_url)
    
    # si des tokens existent déjà 
    try :
        # bouton pour supprimer les tokens existant
        driver.find_element_by_xpath('//*[@id="js-pjax-container"]/div[2]/div[2]/div[1]/div[1]/div/details/summary').click()
        # confirmation de suppresion des tokens
        revoke = driver.find_element_by_id('revoke-access-confirmation')
        revoke.send_keys(username)
        revoke.send_keys(Keys.ENTER)

    except NoSuchElementException : #
        print("Il n'y pas pas de token existant")
        
    # une fois connecté on va sur la page pour créer des tokens
    token_url = "https://github.com/settings/tokens/new"
    driver.get(token_url)

    driver.find_element_by_id('oauth_access_description').send_keys("Automatisation-"+str(random.randint(0,100))) # on rajoute un numéro random au cas où, pour ne pas avoir le même nom pour 2 tokens (ce qui est impossible)
    driver.find_element_by_xpath('//*[@id="new_oauth_access"]/div/dl[2]/dd/div/ul/li[1]/label/div/input').click()
    driver.find_element_by_xpath('//*[@id="new_oauth_access"]/p/button').click()
    
    html_code = driver.page_source
    soup = BeautifulSoup(html_code,'html.parser')
    token = soup.find("code",{"id":"new-oauth-token"})
    token_code = token.get_text()
    
    return token_code




print(get_token_txt())

