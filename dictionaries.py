import json

dictionary_test = {}

with open('dictionary_test') as f:
	dictionary_test = json.load(f)

print dictionary_test['name']

dictionary_test['name'] = "Matheus"

age_label = raw_input("Enter label: ")
age_value = raw_input("Enter age value: ")

dictionary_test[age_label] = age_value

print dictionary_test

with open('dictionary_test', 'w') as f:
    json.dump(dictionary_test, f)