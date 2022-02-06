variable = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# initialize empty lists
temp_list = []
additional_sentence = []
# creating list of sentences from "variable". Delimiter - "."
list_sentences = variable.split(".")
# delete empty string
del list_sentences[-1]
# iterating by elements from list of sentences "list_sentences"
for item in list_sentences:
    # normalize sentence from letter cases point of view
    item = item.strip().lower().capitalize()
    # remove all the whitespaces from the sentence
    item = " ".join(item.split())
    # Fix “iz” with correct “is”
    item = item.replace(' iz ', ' is ')
    # adding whitespace
    item = item.replace('Fix“iz”', 'Fix “iz”')
    # fix word "tex"
    item = item.replace('in this tex', 'in this text')
    # Capitalise word ": this"
    item = item.replace(': this', ': This')
    # spliting sentence "item" by elements
    last_word = item.split(' ')
    # appending last word from sentence "item" to list "additional_sentence"
    additional_sentence.append(last_word[-1])
    # adding '. ' to the end of sentence "item"
    item = item + '.'
    # adding an adjusted sentence to the intermediate list "temp_list"
    temp_list.append(item)

# creating sentence with last words of each existing sentence
new_sentence = " ".join(additional_sentence).capitalize()
# adding "new_sentence" to the end of paragraph temp_list[2]
temp_list[2] = temp_list[2] + ' ' + new_sentence + '.'
# Joining all sentences to one variable
normalize_sentences = "\n".join(temp_list)
print(normalize_sentences)
###################################################################################################

count = 0
# loop for search each index
for i in range(0, len(normalize_sentences)):
    # Check each char is blank or not
    if normalize_sentences[i].isspace():
        count += 1
print(f'\nNumber of whitespace characters in "normalize_sentences" is {count}.')