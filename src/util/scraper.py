# scraper.py - Sofiane DJERBI
""" CONVENTIONS
 | On utilisera exclusivement le site nonograms.org.
"""
from nonogram import Nonogram
from requests_html import HTMLSession

class Scraper:
    """ SCRAPPER (NONOGRAMS.ORG)
    Récupère des nonogrammes en ligne et les transforme en objet Nonogram
    Variables :
        - session : Navigateur chromium de requests-html
    """
    def __init__(self):
        """ INITIALISATION
        """
        self.session = HTMLSession() # Notre "navigateur virtuel"

    def get(self, url, colors=False):
        """ CONVERTION
        Convertis un nonogramme de nonograms.org en objet Nonogram
        Variables :
            - url : Url du nonogram sur nonograms.org
            - colors : Récuperer les couleurs ? (bool)
        """
        print("Scraping Nonogram...")
        if not "nonograms.org" in url.lower():
            raise ValueError("Wrong URL, please use nonograms.org.")
        r = self.session.get(url) # On récupère le code source
        if r.status_code != 200:
            raise Exception(f"Cannot GET Nonogram URL, error: {r.status_code}")
        name = r.html.find('title')[0].text[36:-1] # Titre du nonogramme
        # Attention: La ligne suivante télécharge le driver chromium ~ 109 MO...
        r.html.render() # On execute le javascript dans un navigateur chromium
        ### TRAITEMENT DES DONNEES CI DESSOUS

        size = r.html.xpath('//div[@class = "content"]/table//tr/td[1]/text()')[0] # BeautifulSoup4
        size = size[6:].split('x')
        size = (int(size[0]), int(size[1]))
        x = size[0] # Taille en x, y
        y = size[1]
        col = r.html.xpath('//*[@class="nmtt"]/table/tbody//tr//td//div/text()')
        col = [0 if e == '\xa0' else int(e) for e in col]
        col = [col[i*x:i*x+x] for i in range(len(col)//x)] # Numpy.reshape equivalent..
        row = r.html.xpath('//*[@class="nmtl"]/table/tbody//tr//td//div/text()')
        row = [0 if e == '\xa0' else int(e) for e in row]
        row = [row[i*y:i*y+y] for i in range(len(row)//y)]
        print(f"Nonogram {name} sucessfully scrapped.")
        return Nonogram(size, row, col, name, colors)

if __name__ == "__main__":
    scraper = Scraper()
    nonogram = scraper.get("https://www.nonograms.org/nonograms/i/40285")
    print(nonogram.x, nonogram.y)
    print(nonogram.col)
    print(nonogram.row)
