# coding: utf-8
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from spacy import load
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
import pandas as pd
nlp = load('en_core_web_sm')
nlp.add_pipe(WordnetAnnotator(nlp.lang))
token = nlp('Calculator.')[0]
token._.wordnet.synsets()
meaning1, meaning2 = token = nlp('Calculator.')[0]
meaning1, meaning2 = token._.wordnet.synsets()
meaning1
meaning1.name()
meaning1.lemmas()
meaning2.lemmas()
token._.wordnet.wordnet_domains()
nlp('mathematics')[0]._.wordnet.wordnet_domains()
'science' in _
nlp('pure_science')[0]._.wordnet.wordnet_domains()
nlp('science')[0]._.wordnet.wordnet_domains()
wnet = nlp('science')[0]._.wordnet
wnet.wordnet_synsets_for_domain()
wnet.lemmas()
token = nlp('human')[0]
token._.wordnet.lemmas()
token._.wordnet.synsets()
[c.lemmas() for c in token._.wordnet.synsets()]
syn =token._.wordnet.synsets()
x = syn[0]
x
x.common_hypernyms()
man = nlp('man')[0]
woman = nlp('woman')[0]
man._.wordnet.synsets()
man_syn = man._.wordnet.synsets()[0]
woman_syn = woman._.wordnet.synsets()[0]
man_syn
woman_syn
man_syn.common_hypernyms(woman_syn)
man_syn.entailments()
get_ipython().run_line_magic('pinfo', 'man_syn.entailments')
man_syn.examples()
man_syn.hypernyms()
woman_syn.hypernyms()
man_syn.hyponyms()
woman_syn.hyponyms()
get_ipython().run_line_magic('pinfo', 'man_syn.jcn_similarity')
get_ipython().run_line_magic('pinfo', 'man_syn.lemmas')
man_syn.lemmas()
get_ipython().run_line_magic('pinfo', 'man_syn.similar_tos')
man_syn.similar_tos()
while True:
    x = man_syn.hypernyms()[0]
    print(x)
    x = x.hypernyms()[0]
    
x = man_syn
while True:
    print(x)
    x = x.hypernyms()[0]
    
x
x.hypernyms()
x = man_syn
while True:
    print(x)
    x = x.hyponyms()[0]
    
while True:
    print(x)
    i = 0
    try:
        x = x.hyponyms()[i]
    except IndexError:
        i += 1
        x = x.hyponyms()[i]
        
while True:
    print(x)
    try:
        i = 0
        x = x.hyponyms()[i]
    except IndexError:
        i += 1
        x = x.hyponyms()[i]
        
        
