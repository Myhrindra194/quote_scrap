import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    dicoTag = ["love","inspirational","life","humor","books","reading","friendship","friend","truth","simile"]

    print(f"""
        Voici la liste des tags de citations disponibles: 
        {dicoTag}
        """)
    tag = (input("Entrer votre tag: ")).lower()

    print(f"""
        Veuillez patienter svp ......
        """)

    if tag in dicoTag:
        url = "https://quotes.toscrape.com/tag/"+tag+"/"

        response = requests.get(url)

        html = BeautifulSoup(response.text, 'html.parser')

        quotes = html.find_all('span', class_="text")
        authors = html.find_all('small', class_="author")

        quotesList = list()
        for quote in quotes:
            quotesList.append(quote.text)
                
        authorsList = list()
        for author in authors:
            authorsList.append(author.text)


        for quotation in zip(quotesList,authorsList):
            print(f"""{quotation[0]} {quotation[1]}
                """)
    else:
        print("Ce tag n'existe pas dans la liste des tags disponibles")




