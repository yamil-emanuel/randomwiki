import os
import requests
from bs4 import BeautifulSoup
import webbrowser
import re
from textwrap import wrap

languages_available = {"GER":"https://de.wikipedia.org/wiki/Spezial:Zuf%C3%A4llige_Seite","POL":"https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona","IT":"https://it.wikipedia.org/wiki/Speciale:PaginaCasuale","ES":"https://es.wikipedia.org/wiki/Especial:Aleatoria","FR":"https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard","EN":"https://en.wikipedia.org/wiki/Special:Random","CH":"https://zh.wikipedia.org/wiki/Special:%E9%9A%8F%E6%9C%BA%E9%A1%B5%E9%9D%A2","RU":"https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def exit ():
    os.system('exit' if os.name=='nt' else 'exit')

class RandomArticle:
    def __init__(self,lan):
        self.lan=languages_available[lan]

    def CapturePage (self):
        page = requests.get(self.lan)
        soup = BeautifulSoup(page.content, "html.parser")
        self.article=soup
        self.url=page.url

    def Title (self):
        title=self.article.find(id="firstHeading").get_text()
        print(title,"\n")

    def ArticleCleaner(self,article):
        #Deletes all the "[Hiperlinks]" in the artcle.
        
        #Putting a space before every hiperlink "[NUMBER]". Ex--> blablabla [1].
        article=article.replace("["," [")
        article=article.split(" ")
        temp=[]
        for word in article:
            #If there is a number in the element and that element contains '[' and ']' (hiperlink) will be skipped.
            if re.search("[123456789]",word) and "[" in word and "]" in word:
                pass
            else:
            #else it will be appended to a temporal list
                temp.append(word)
        #returns a string using the temp-list's data.
        return ' '.join([str(elem) for elem in temp])
    

    def Resume (self):
        #First filter in the soup
        temp=self.article.find_all('p')
        #Second filter in the soup
        resume=temp[0].get_text()
        #Sets limit to 70 characters in a row
        resume=wrap(resume,70)

        for chunk in resume:
            #resume[-1] stands for the article's index.
            if chunk !=resume[-1]:
                #Runs the Hiperlink cleaner
                print(self.ArticleCleaner(chunk))
            else:
                #Runds the Hiperlink cleaner
                print(self.ArticleCleaner(chunk),"\n \n"+"-"*70+"\n")

    def VisitArticle (self):
        #Opens the URL using the default browser.replace(x, y)
        webbrowser.open_new(str(self.url))

def run():
    #User's selected language
    selected_language=input("\nSELECT A LANGUAGE [CH-EN-ES-FR-GER-IT-POL-RU]\n").upper()
    cls()

    while True:
        
        #Search for a random article in the selected language.
        user_lang=RandomArticle(selected_language)

        #Getting the Article's data
        RandomArticle.CapturePage(user_lang)
        RandomArticle.Title(user_lang)
        RandomArticle.Resume(user_lang)

        #User's choosen option.
        
        user_input=(str(input("SELECT AN OPTION [1,2,3] \n1)NEW ARTICLE \n2)READ THE ARTICLE \n3)EXIT\n"))).lower()
        if user_input=="3":
            cls()
            exit()
            break

        elif user_input=="2":
            cls()
            RandomArticle.VisitArticle(user_lang)
            break


        elif user_input=="1":
            cls()
            pass


"""
-opción 4 + palabra para agregar la palabra a la lista de vocabulario con la oración como ejemplo
"""

run()
