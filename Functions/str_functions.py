import pandas as pd
import re
import nltk
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from nltk.tag import UnigramTagger
from nltk.corpus import brown
import webcolors
from nltk.stem import WordNetLemmatizer


def composedWords(x):
    if set('-').intersection(x[:][0]):
        return True

    else: return False

def quantityComposeWord(x,measure_quantity_list):

    decomposed = x.split('-')
    if (decomposed[0] in measure_quantity_list or decomposed[1] in measure_quantity_list):
        return decomposed
    else: return ' '

def usefullcomposedWords(x,measure_quantity_list):

    #We check if the word of interest is in between parenthesis
    if (set('(').intersection(x[:][0]) or set(')').intersection(x[:][0])):
        #if it's the case, we take them out
        inWord = re.sub('[(){}<>]', '', x[:][0])
        # We check if the word is a compose word, if it's the case we split it again and we check if it's a word
        # belonging to the measure quantity list
        if composedWords(x):
            decomposed = inWord.split('-')
            if (decomposed[0] in measure_quantity_list) or (decomposed[1] in measure_quantity_list[1]):
                return True
            else: return False
        # If it's not a composed word we check if it belong to the measure quantity list to keep it
        elif inWord in measure_quantity_list:
            return True
        else: return False

    else: return False


def conditionsSelection(x):

    #if set('-').intersection(x[:][0]):
    #    composedWord = x[:][0].split('-')
    #    y = pos_tag([composedWord])
    #    if composedWord[0]


    #if (x[:][1] in('JJ') and x[:][0] in (webcolors.CSS3_NAMES_TO_HEX)):
    #    return True
    if (x[:][1] not in('DT','PRP$','IN','JJ','RB','ADV','PRT','PRON','CC')):
        return True

    else: return False


def fun_covert_to_float(frac_str):

    splited_frac_str = frac_str.split(' ')

    if '/' in frac_str :
        fractionSplit = splited_frac_str[0].split('/')
        frac = float(fractionSplit[0])/float(fractionSplit[1])
        return frac
    elif bool(re.search('\.([0-9])\.',frac_str)):
        return float(re.findall('\.([0-9])\.',frac_str)[0])
    else:
        frac = float(splited_frac_str[0])
        return frac

def fun_unit_corrector(string):

    newUnit = ""
    splited_string = string.split(' ')
    dict_conver = {'teaspoon' : 5,'tablespoon' :15, 'oz': 30,'cup': 237,'pint' : 474,'quart':946, 'gallon': 3785,'dl' :100,'pound' :453,'ounce' :29,'g' : 1,'kg': 1000,  \
        'l': 1000, 'ml': 1,'mg':1,'bottle':750,'drop':0.05,'pinch':0.36,'jar':1000,'can':330,'unit':'u','gill':118}

    teaspoon = ['teaspoon','tsp','tsps','t','teaspoon']
    tablespoon = ['tablespoon' ,'T', 'tbl','tbls', 'tbs','tbsp']
    oz = ['oz', 'fl', 'fluid ounce']
    cup = ['cup', 'c']
    pint =  ['pint','p', 'pt','pts', 'fl pt']
    quart =  ['quart','q', 'qt','fl qt']
    gallon =  ['gallon', 'gal','gals']
    ml = ['ml', 'milliliter', 'millilitre', 'cc','mL']
    l = ['l', 'liter', 'litre', 'L']
    dl = ['dl','deciliter','decilitre','dL']
    pound = ['pound','lb','lbs']
    ounce = ['ounce','oz']
    mg = ['mg','milligram','milligramme']
    kg = ['kg', 'kilogramme','kilogram']
    g = ['g','gram','gramme']
    unit = ['unit','stalk','package']
    other_indic=['bottle','pinch','jar','can','drop','gill']

    unit_list = [teaspoon, tablespoon, oz, cup, pint, pint, quart, gallon, ml, l, dl, pound, ounce, mg, kg, g]


    #if (len(splited_string) == 1 and splited_string[0] == ''):
    #    return ''

    for lists in unit_list:
        for i,x in enumerate(splited_string):
            if x in lists:
                newUnit = lists[0]
                gram_value = float(dict_conver[newUnit]) * fun_covert_to_float(splited_string[abs(i-1)])
                return gram_value
            if x in other_indic:
                gram_value = float(dict_conver[x]) * fun_covert_to_float(splited_string[abs(i-1)])
                return gram_value
            if x in unit:
                return splited_string[abs(i-1)]+' u'

    return 0


def fun_extract_ingredients(one_receipe,ingredients_list,techniques_list,units_list,to_gram=True):
    ''' Function extractiing all ingredients, quantities and possiblity technics of cooking

    '''
    lemmatizer = WordNetLemmatizer()
    if '|' in one_receipe:
        ingredients=one_receipe.split('|')
    else:
        ingredients=one_receipe.split(', ')

    dic_ingre={}
    dic_tec={}
    wasted_ingr=[]
    wasted_number=0
    for elem in ingredients:
        #split in words
        elem=elem.replace('-',' ')
        elem_list=elem.split(' ')
        #avoid special characters appearing in some recipes:
        if '&#' in elem:
            continue
        #keep only alphanumerics in each words
        elem_list=[re.sub('[^0-9a-zA-Z/. ]+', '', x) for x in elem_list]
        #keep only the root of the word
        check = [lemmatizer.lemmatize(token) for token in elem_list]
        #split str of string with stuck digit : '2cups': '2','cups'
        check=sum([re.findall(r'[A-Za-z]+|[\d./]+', x) for x in check],[])
        techniques=[]
        units=[]
        one_ingr=None
        no_unit=True
        no_number=True
        check = list(filter(None, check))
        for word in check:
            if word in techniques_list:#check if it belongs to our technics list
                techniques.append(word)
            elif word in ingredients_list:#check if it belongs to our ingredient list
                one_ingr=word
            elif bool(re.search(r'\d',word)) and (no_number):#check if it belongs to our unit list or is alphanumeric
                units.append(word)
                no_number=False
            elif (word in units_list) and (no_unit):
                units.append(word)
                no_unit=False
        for biword in nltk.bigrams(check): # check if we have a biword ingredient
            if ' '.join(biword) in ingredients_list:
                one_ingr=' '.join(biword)
        if one_ingr==None :      # check if we have no ingredient : avoid this element of recipe
            wasted_number=wasted_number+1
            wasted_ingr.append(' '.join(check))
            continue
        if(len(' '.join(units))==0):  # fill with a special unit if we are dealing with no quantity
            units.append('1')
            units.append('unit')
        elif no_unit:
            units.append('unit')
        elif no_number:
            units.append('1')


        units=' '.join(units)
        if to_gram:
            units=fun_unit_corrector(units)

        dic_ingre[one_ingr]=units
        dic_tec[one_ingr]=' '.join(techniques)

    return dic_ingre,dic_tec,wasted_ingr,wasted_number
