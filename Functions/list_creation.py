import numpy as np
import pandas as pd
import re
import nltk
import itertools
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import requests
from bs4 import BeautifulSoup
import string


#Allow to find verbs in a tokenize word
def verbeSelection(x):
    '''
    Allow to find verbs in a tokenize word
    '''
    if (x[:][1] == 'VBN'):
        return True

    else: return False


def fun_technique_list(dataset,path):
    '''
    find all the verbs in a dataset of recipes
    '''
    techniqueList = []
    for j in range(len(dataset)):
        a=dataset.loc[j]['ingredients_list']
        if '|' in a:
            ingredients=a.split('|')
        else:
            ingredients=a.split(', ')

        recepie = ""
        for i, elem in enumerate(ingredients):
            regex = re.compile('[,\.!?%#*-]')
            elem=regex.sub('', elem)

            sent=pos_tag(nltk.word_tokenize(elem))

            a = list(filter(lambda x: verbeSelection(x), sent))
            if len(a)>0 and a[0][0] not in techniqueList:
                if a[0][0][-2:] == 'ed':
                    techniqueList.append(a[0][0])
    with open(path+'technique_list.txt', 'w') as f:
        for s in techniqueList:
            f.write(s + '\n')
    print('technique_list.txt has been created')


def fun_ingredients_list(path):
    '''
    extract a list of ingredient from a website
    The website is easily organise and contains one page of ingredients for each letter (except x)
    We end up with a vocabulary of ingredients of 1140 words
    '''
    ingredient =[]
    alphabet = list(string.ascii_lowercase)
    alphabet.remove('x')
    for letter in (alphabet):
        url='http://www.bbc.co.uk/food/ingredients/by/letter/'+ letter
        r = requests.get(url)
        page_body = r.text
        soup=BeautifulSoup(page_body, 'html.parser')
        stat= soup.find('ol', class_='resources foods grid-view')
        for a in stat.find_all('li',class_='resource food'):
            ingredient.append(a.get('id'))

    ingredient_list = list(map(lambda x: x.replace('_',' '), ingredient))
# ---------------- To find word that are in composed words which could be useful as single ingredient
    composed_word = list(map(lambda x: x.split(' '), ingredient_list))
    result_word_not_in_data = []
    for x in composed_word :
        if(len(x)>1):
            for i in range(len(x)):
                if(x[i] not in ingredient_list ):
                    result_word_not_in_data.append(x[i])
    (set(result_word_not_in_data))
# ---------------- We add the word from composed word manually

    ingredient_list = ingredient_list +['alfafa','almonds','apricots','beans','bechamel','berries','brie',\
    'camembert','chanterelle','chantilly','citrus','corn','emmental','kiwi','lemons','mozzarella','mushrooms',\
    'parmesan','peas','potatoes','ricotta', 'roquefort','sausage','shiitake','water','vanilla','vacherin','tuna',\
    'soy','soya','eggplant','tortilla','zucchini','yogurt','jalapeno','cilantro','chili powder','pecan','arugula',\
    'whiskey','cornstarch','cornmeal','pecan','feta','endive','cereal','sesame','chile paste','bulgur','amaretto','chili',\
    'pepperoncini','gruyere','agave','cayenne']
    with open(path+'ingredient_list.txt', 'w') as f:
        for s in ingredient_list:
            f.write(s + '\n')
    print('Ingredient_list.txt has been created')
