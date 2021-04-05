# scraper.py - Sofiane DJERBI
""" CONVENTIONS
 | On utilisera exclusivement le site nonograms.org.
 | Le code ci-dessous est hardcodé et uniquement compatible avec nonograms.org
""" # Cette partie est un peu "hardcodée"...
from nonogram import Nonogram
from requests_html import HTMLSession

class Scraper:
    """ SCRAPPER (NONOGRAMS.ORG)
    Récupère des nonogrammes en ligne et les transforme en objet Nonogram
    Variables:
        - session: Navigateur chromium de requests-html
    """
    def __init__(self):
        """ INITIALISATION
        """
        self.session = HTMLSession() # Notre "navigateur virtuel"

    def get(self, url, colors=False):
        """ CONVERSION
        Convertis un nonogramme de nonograms.org en objet Nonogram
        Variables:
            - url: Url du nonogram sur nonograms.org
            - colors: Récuperer les couleurs ? (bool)
        Retourne:
            - Un objet Nonogram
        """
        print("Scraping Nonogram...")
        if not "nonograms.org" in url.lower():
            raise ValueError("Wrong URL, please use nonograms.org.")
        r = self.session.get(url) # On récupère le code source
        if r.status_code != 200:
            raise Exception(f"Cannot GET Nonogram, error: {r.status_code}")
        name = r.html.find('title')[0].text[36:-1] # Titre du nonogramme
        # Attention: La ligne suivante télécharge le driver chromium ~ 109 MO...
        r.html.render() # On execute le javascript dans un navigateur chromium
        ### TRAITEMENT DES DONNEES CI DESSOUS

        size = r.html.xpath('//div[@class = "content"]/table//tr/td[1]/text()')[0] # BeautifulSoup4
        size = size[6:].split('x')
        size = (int(size[0]), int(size[1]))
        x = size[0] # Taille en x, y
        y = size[1]
        rcol = r.html.xpath('//*[@class="nmtt"]/table/tbody//tr//td//div/text()')
        rcol = [0 if e == '\xa0' else int(e) for e in rcol]
        col = []
        for i in range(x):
             col.append([rcol[e+i] for e in range(0, len(rcol), x)]) # Un peu compliqué mais on prend tous les elements dont l'index est i modulo len/x
        row = r.html.xpath('//*[@class="nmtl"]/table/tbody//tr//td//div/text()')
        row = [0 if e == '\xa0' else int(e) for e in row]
        row = [row[i:i+len(row)//y] for i in range(0, len(row), len(row)//y)] # Split les lignes
        print(f"Nonogram {name} sucessfully scrapped.")
        return Nonogram(size, row, col, name, colors)


if __name__ == "__main__": # Debug !
    scraper = Scraper()
    url = input("Url: ")
    nonogram = scraper.get(url)
    nonogram.save("../resources/nonograms/")
    nonogram = Nonogram()
    nonogram.load("../resources/nonograms/bee.nng")
    print(nonogram.x, nonogram.y)
    print(nonogram.col)
    print(nonogram.row)
