glossary = {
    'indentation': 'the spaces at the beginning of a code line',
    'list': 'a collection which is ordered and changeable, allows duplicate members',
    'tuple': ' a collection which is ordered and unchangeable',
    'variable': 'containers for storing data values',
    'integer': 'a whole number, positive or negative, without decimals, of unlimited length',
    'dictionary': 'a collection which is unordered, changeable and indexed',
    'function': 'a block of code which only runs when it is called',
    'boolean': 'epresent one of two values: True or False',
    'operator': 'used to perform operations on variables and values',
    'array': 'a special variable, which can hold more than one value at a time'
}

for word, definition in glossary.items():
    print(f"{word.title()}: {definition}")
