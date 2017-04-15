import csv


def read(filename, dictionary):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            dictionary[row[0]] = (row[1]), (row[2])
    return dictionary


def appellations_alphabeticall(dictionary):
    key_list = sorted(dictionary.keys())
    for key in key_list:
        print(key, end=" ")
    print('\n')


dictionary = {}
menu_tuple = (0, 1, 2, 3, 4)
read('names.csv', dictionary)


print('Welcomme in dictionaryfor a little programmer')
print('what can i do for you?')
print('1. search explanation by appellation')
print('2. add new definition')
print('3. show all appellations alphabetically')
print('4. show available definitions by first letter of appellation')
print('0. exit')
menu = int(input('Chose a number: '))

if menu == menu_tuple[1]:
    appelation_search = input("Write appelation: ")
    if appelation_search in dictionary:
        explanation = (dictionary[appelation_search])
        print(explanation[0], '\nsource:', explanation[1])
    else:
        print("I cant find what you are looking for")
elif menu == menu_tuple[2]:
    new_key = input("Please write definitions: ")
    new_description = input("Please write description: ")
    new_source = input("Please write source: ")
    dictionary[new_key] = new_description, new_source
    with open('names.csv', 'w', newline='') as csvfile:
        for key, value in dictionary.items():
            my_writer = csv.writer(csvfile, delimiter=',')
            my_writer.writerow([key]+[value[0]]+[value[1]])

if menu == menu_tuple[3]:  # show all appellations alphabetically
    appellations_alphabeticall(dictionary)
