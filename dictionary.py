def appellations_alphabeticall(dictionary):
    key_list = sorted(dictionary.keys())
    for key in key_list:
        print(key, end=" ")
    print('\n')


menu_tuple = (0, 1, 2, 3, 4)

dictionary = {'function': ('explanation', 'source'),
            'parameter': ('explanation', 'source'),
            'variable': ('explanation', 'source'),
            'argument': ('explanation', 'source'),
            'dictionary': ('explanation', 'source')}

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
    explanation = dictionary[appelation_search]
    print(explanation[0])

if menu == menu_tuple[3]:  # show all appellations alphabetically
    appellations_alphabeticall(dictionary)
