from SymTable import SymTable
from PIF import PIF
import re

separators = ['=', '<=', '>=', '->', '<<', '>>', '<', '>', ':', '\+', '\-', '\/', '\*', '{', '}', '\(', '\)',' ',
              '\t', ';' , '\.']

white_spaces = [' ', '\n', '\t', '']

reserved_words = ['for', 'while', 'if', 'else', 'int', 'char', 'string', 'Struct', 'cin', 'cout', 'return', 'true','false']
operators = ['(',')','+', '-', '*', '/', '=', '<', '<=', '==', '>=', '>']

FILE_NAME = 'date.txt'

def is_identifier(token):
    parser = re.compile('^[a-zA-Z][a-zA-Z0-9]{0,25}$')
    match = parser.match(token)
    return match


def is_constant(token):
    int_parser = re.compile('^0$|^([-+]?[1-9][0-9]*)$')
    match = int_parser.match(token)
    if match:
        return True
    string_parser = re.compile('^\"[0-9a-zA-A]*\"$')
    match = string_parser.match(token)
    if match:
        return True
    char_parser = re.compile('^\'[0-9a-zA-A]\'$')
    match = char_parser.match(token)
    return match

def clear_white_spaces(content):
    new_content = []
    for i in range(len(content) - 1):
        if content[i] in white_spaces:
            continue
        else:
            new_content.append(content[i])
    if content[len(content) - 1] not in white_spaces:
        new_content.append(content[len(content) - 1])
    return new_content


def search_line(token):
    with open(FILE_NAME) as f:
        counter = 1
        for line in f:
            if token in line:
                return counter
            counter += 1

if __name__ == '__main__':

    st = SymTable()
    pif = PIF()

    with open(FILE_NAME) as f:
        content = f.read()
        new_content = re.split("\n", content)
        temp = []
        for separator in separators:
            temp = []
            for token in new_content:
                to_be_splitted = token[:]
                if to_be_splitted in separators:
                    temp.append(to_be_splitted)
                    continue
                after_split = re.split('(' + separator + ')', to_be_splitted)
                for x in after_split:
                    temp.append(x)
            new_content = temp
        tokens = temp

    tokens = clear_white_spaces(tokens)
    for token in tokens:
        if token in reserved_words or token in operators or token in separators:
            pif.add_to_pif(token, -1)
        elif is_identifier(token):
            pos = st.add_token(token)
            pif.add_to_pif('identifier', pos)
        elif is_constant(token):
            pos = st.add_token(token)
            pif.add_to_pif('constant', pos)
        else:
            print('\n lexical error on token ' + token + ' on line ' + str(search_line(token)) + '\n')
            break

    print(st)
    print(pif)