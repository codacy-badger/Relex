from bs4 import BeautifulSoup
import requests
import re
from spacy import displacy
import en_core_web_sm
from load import encode
nlp = en_core_web_sm.load()
def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
ny_bb = url_to_string('https://www.nytimes.com/2018/08/13/us/politics/peter-strzok-fired-fbi.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=first-column-region&region=top-news&WT.nav=top-news')
article = nlp(ny_bb)
# print(len(article.ents))
# labels = [x.label_ for x in article.ents]
# Counter(labels)
# print(Counter(labels)
sentences = [x for x in article.sents]
print(sentences)
print(sentences[20])
print("type: ", type(sentences[20]))
print('encode:', encode(str("An example string")))
displacy.render(nlp(str((sentences[20])).decode('utf-8', 'ignore')), jupyter=True, style='ent')
displacy.render(nlp(str(sentences[20]).decode('utf-8', 'ignore')), style='dep', jupyter = True, options = {'distance': 120})
