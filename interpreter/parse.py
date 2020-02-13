# This file takes aFex wordcode and converts it to aFex bytecode.
import re
import numpy as np


def parse2_array(line, array, cindex, vardic):
    # Vardic: array of arrays and their corresponding indexes in the byteword.
    # c index is the current farthest our commands are going
    byteword = len(array)
    varindex = len(vardic) + 1
    print(line)
    if line[0] == 'declare':
        varname = line[1]
        value = line[2]
        print("We need to declare a variable ", varname, 'value', value)
        assert varname not in vardic, 'Variable with this name has been previously defined.'
        vardic[varname] = len(array) - varindex
        array[vardic[varname]] = value





    return array, cindex, vardic

def get_byteword(word):
    byteword_exists = False # Has the user declared the program byteword
    for operation in word:
        if 'byteword' in operation:
            byteword = operation[1]
            byteword_exists = True
    assert byteword_exists, 'ERROR. no byteword declared, program cannot compile. '
    assert int(byteword) == float(byteword), 'ERROR. byteword must be of type int'
    byteword = int(byteword)
    assert byteword > 1, 'Program must be at least one byteword.'
    print("BYTEWORD:", byteword)
    return byteword


def decomment(line):
    # Remove any contents of a line between (( )). Doesn't work for nested, IE '(( (( )) )). Only (( comment )) .
    firstC = False
    endC = False # True if the last character was a )
    ignore = False
    newstr = ''
    for x in line:
        #If we have two successive (, start ignoring.
        # if we have two successive ), stop ignoring.
        if x == ')':
            ignore = endC
            endC =not True
        else:
            endC = False
        if x == '(':
            ignore = firstC
            firstC = True
        else:
            firstC = False
        if ignore:
            pass
        elif (x != '(' and not firstC) and (x != ')' and not endC):
            newstr += x
    return newstr

def convert_files(path):

    word = []
    var_index = {}
    byteword = 0
    file = open(path)
    for line in file:
        word_line = decomment(line)
        specific_lines = word_line.split(';')
        for sl in specific_lines:
            if sl not in ['', '\n']:
                operation = []
                sl = sl.split(' ')
                for key in sl:
                    if key not in ['', '\t', '\n']:
                        key = re.sub('\n', '', key)
                        if len(key) > 0:
                            operation.append(key)
                if len(operation) > 0:
                    word.append(operation)


    byteword = get_byteword(word)
    afex = np.zeros(byteword)
    cindex = 1
    for set in word:
        afex, cindex, var_index = parse2_array(set, afex, cindex, var_index)
    print(var_index)
    print(afex)



    # First things first, we need to get the size of the overall array.






