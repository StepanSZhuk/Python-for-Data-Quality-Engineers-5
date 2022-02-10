# Refactor homeworks from module 2 and 3 using functional approach with decomposition.

# Import the libraries
import random
import string
import re

# 1. create a list of random number of dicts (from 2 to 10)
def create_random_dict():
    random_dict = [{x: random.randint(0, 100) for x in [random.choice(string.ascii_lowercase)
                    for y in range(random.randint(1,26))]} for z in range(random.randint(2, 10))]
    return random_dict

# 2. get previously generated list of dicts and create one common dict:
def create_common_dict(random_dict):
    # creating list of keys from previously generated list of dicts
    temp_list = [key for dic in random_dict for key, value in dic.items()]
    # creating an empty one common dictionary
    common_dict = {}
    # iterating by on the list of unique keys (using set) from previously generated list of dicts
    for letter in set(temp_list):
        # creating a list of values for one letter
        values_letter = [dic[letter] for dic in random_dict if letter in dic]
        # get max value for one letter
        max_value = max(values_letter)
        # if key is only in one dict - writing a key and value to one common dictionary 'common_dict'
        if len(values_letter) == 1:
            common_dict[letter] = max_value
        # if dicts have same key, take max value, and rename key with dict number with max value
        if len(values_letter) > 1:
            # iterating by list of dictionaries
            for dic in random_dict:
                # iterating on the dictionary in the list of dictionaries
                for key, value in dic.items():
                    # checking if a searching letter and the corresponding maximum value  is in the dictionary
                    if key == letter and value == max_value:
                        # index for a searching letter and the corresponding maximum value in the list of dictionaries
                        ind_x = random_dict.index(dic) + 1
            # renaming key with dict number with max value
            new_key = letter + '_' + str(ind_x)
            # writing a new key and max value to one common dictionary 'common_dict'
            common_dict[new_key] = max_value
    return common_dict

########################################################################################################################

variable = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''
# parse text by sentences
def parse_text_by_sentences(text):
    list_sentences = variable.split(".")
    del list_sentences[-1]
    return list_sentences


# Joining all sentences to one variable
def fix_issues(list):
    fix_list_sentences = []
    for item in list:
        # normalize sentence from letter cases point of view
        item = item.strip().lower().capitalize()
        # remove all the whitespaces from the sentence
        item = " ".join(item.split())
        # Fix “iz” with correct “is”
        temp = []
        for elem in item.split(' '):
            if elem == 'iz':
                elem = elem.replace('iz', 'is')
            temp.append(elem)
        item = " ".join(temp)
        item = item.replace('Fix“iz”', 'Fix “iz”')
        # Capitalise word ": this"
        item = item.replace(': this', ': This')
        # fix word "tex"
        item = item.replace('in this tex', 'in this text')
        # adding an adjusted sentence to the intermediate list "temp_list"
        fix_list_sentences.append(item)
    return fix_list_sentences

# creating sentence with last words of each existing sentence
def sentence_last_words(list):
    additional_sentence = []
    for item in list:
        last_word = item.split(' ')
        # appending last word from sentence "item" to list "additional_sentence"
        additional_sentence.append(last_word[-1])
    # creating sentence with last words of each existing sentence
    new_sentence = " ".join(additional_sentence).capitalize()
    # adding "new_sentence" to the end of paragraph temp_list[2]
    return new_sentence

# function for adding "new_sentence" to the end of paragraph and joining all sentences to one variable
def normalize_text(fix_list,new_sentence):
    fix_list[2] = fix_list[2] + '. ' + new_sentence + '.'
    for i in range(len(fix_list)):
        if i != 2:
            fix_list[i] = fix_list[i] + '. '
    # # Joining all sentences to one variable
    normalize_sentences = "\n".join(fix_list)
    return normalize_sentences

#function for counting whitespaces in text
def count_whitespaces(text):
    count = 0
    # loop for search each index
    for i in range(0, len(text)):
        # Check each char is blank or not
        if text[i].isspace():
            count += 1
    return(print(f'\n Number of whitespace characters in "normalize_sentences" is {count}.'))
###############################################################################################
print(f'Task 2')
list_dictionaries = create_random_dict()
print(create_common_dict(list_dictionaries))
print('*'*100)

list_sentences = parse_text_by_sentences(variable)
fix_list_sentences = fix_issues(list_sentences)
additional_sentence = sentence_last_words(fix_list_sentences)
normalize_sentences = normalize_text(fix_list_sentences, additional_sentence)
# print(list_sentences)
# print(fix_list_sentences)
# print(additional_sentence)
print(f'Task 3')
print(normalize_sentences)
print(count_whitespaces(normalize_sentences))