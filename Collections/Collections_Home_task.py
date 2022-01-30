# Import the library 'random' and 'string'
import random
import string

# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]

# Create list of dictionaries using 'random.randint' and dictionary comprehension
random_dict = [
    # creating random numbers of keys in range(1, 3) for one dictionary and populating randoms keys using
    # random.choice(string.ascii_lowercase)) and randoms values using random.randint(0, 100).
    {x: random.randint(0, 100) for x in [random.choice(string.ascii_lowercase) for y in range(random.randint(1, 3))]}
    # creating random number of dicts (from 2 to 10)
    for z in range(random.randint(2, 10))]

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

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
# print the result of the one common dictionary
print(common_dict)
