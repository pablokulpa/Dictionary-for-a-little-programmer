import csv
import sys
import os.path


# checking file existences
def checking_file(filename):
    if os.path.exists(filename) is False:
        sys.exit("Databese file doesnt exist")


# reading file and adding to dictionary
def read(filename, dictionary):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            dictionary[row[0]] = (row[1]), (row[2])
    return dictionary


# printing appelations alphabetically
def appellations_alphabeticall(dictionary):
    key_list = sorted(dictionary.keys())
    for key in key_list:
        print(key, end=" ")
    print('\n')


# adding to dictionary and saving to file
def adding(dictionary):
    new_key = input("Please write definitions: ")
    new_description = input("Please write description: ")
    new_source = input("Please write source: ")
    dictionary[new_key] = new_description, new_source
    with open('names.csv', 'w', newline='') as csvfile:
        for key, value in dictionary.items():
            my_writer = csv.writer(csvfile, delimiter=',')
            my_writer.writerow([key]+[value[0]]+[value[1]])


csvname = 'names.csv'
dictionary = {}
checking_file(csvname)
menu_tuple = (0, 1, 2, 3, 4)
read(csvname, dictionary)


# MENU
print('Welcomme in dictionaryfor a little programmer')
print('what can i do for you?')
print('1. search explanation by appellation')
print('2. add new definition')
print('3. show all appellations alphabetically')
print('4. show available definitions by first letter of appellation')
print('0. exit')
menu = int(input('Chose a number: '))

while menu not in menu_tuple:
    print("Wrong number!")
    menu = int(input('Chose a number: '))

if menu == menu_tuple[0]:
    sys.exit()

elif menu == menu_tuple[1]:
    appelation_search = input("Write appelation: ")
    if appelation_search in dictionary:
        explanation = (dictionary[appelation_search])
        print('description:%s' % explanation[0], '\nsource:%s' % explanation[1])
    else:
        print("I cant find what you are looking for")
elif menu == menu_tuple[2]:
    adding(dictionary)

elif menu == menu_tuple[3]:  # show all appellations alphabetically
    appellations_alphabeticall(dictionary)

elif menu == menu_tuple[4]:
    first_letter = input("Write first letter of appellations: ")
    while len(first_letter) > 1:
        first_letter = input("Write first letter of appellations: ")
    for keys in dictionary.keys():
        if first_letter in keys[0]:
            print(dictionary[keys][0])
