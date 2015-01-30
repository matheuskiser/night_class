import json
import os

dictionary_test = {}

open_file = open('my_dict.json', 'w+')
read_file = open('my_dict.json', 'r')

try:
    dictionary_test = json.load(read_file)
except ValueError, e:
    json.dump({}, open_file)

age_label = raw_input("Enter label: ")
age_value = raw_input("Enter age value: ")

dictionary_test[age_label] = age_value

json.dump(dictionary_test, open_file)

read_file.close()
open_file.close()

print dictionary_test