from bs4 import BeautifulSoup
import urllib.request
import random

def speak():
    with urllib.request.urlopen('http://www.casadobruxo.com.br/textos/reflex.htm') as raw_content:
        html_content = raw_content.read()

  #  print(html_content)

    dom = BeautifulSoup(html_content, "html.parser")

    frases = dom.find_all("p", attrs={"align": "justify"})
    r = [item.text for item in frases]
    frase = r[0].split('\n\n')
    arr = []
    for i in range(4, 111):
        arr.append(frase[i].split('"')[1])

    return random.choice(arr)


if __name__ == '__main__':
    print(speak())
