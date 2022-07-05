def isEmpty(letter):
    if letter == "":
        return True
    else:
        return False


def lexical(data):
    lexeme_chain = []
    current_lexeme = ""
    lexeme_class = ""
    state = "space"
    for i in range(len(data)):
        if data[i][1] == "letter" and state == "space":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += data[i][0]
            if lexeme_class == "dollar_sign":
                lexeme_class = "hex"
            else:
                lexeme_class = "identifier"
            state = "identifier"
        elif data[i][1] == "number" and state == "space":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += data[i][0]
            if lexeme_class == "dollar_sign":
                lexeme_class = "hex"
                state = "identifier"
            else:
                lexeme_class = "integer"
                state = "integer"
        elif data[i][1] == "semicolon":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += ";"
            lexeme_class = "semicolon"
            state = "space"
        elif data[i][1] == "plus-minus":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += data[i][0]
            lexeme_class = "plus-minus"
            state = "space"
        elif data[i][1] == "multiplication":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += "*"
            lexeme_class = "multiplication"
            state = "space"
        elif data[i][1] == "space":
            state = "space"
        elif data[i][1] == "bracket1":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += "("
            lexeme_class = "bracket1"
            state = "space"
        elif data[i][1] == "bracket2":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += ")"
            lexeme_class = "bracket2"
            state = "space"
        elif data[i][1] == "dollar_sign":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += "$"
            lexeme_class = "dollar_sign"
            state = "space"
        elif data[i][1] == "more":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += ">"
            lexeme_class = "more"
            state = "space"
        elif data[i][1] == "less":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += "<"
            lexeme_class = "less"
            state = "space"
        elif data[i][1] == "equal":
            if not isEmpty(current_lexeme):
                lexeme_chain.append([current_lexeme, lexeme_class])
            current_lexeme = ""
            current_lexeme += "="
            lexeme_class = "equal"
            state = "space"
        elif (data[i][1] == "letter" or data[i][1] == "number") and state == "identifier":
            current_lexeme += data[i][0]
        elif data[i][1] == "letter" and state == "integer":
            return False
        elif data[i][1] == "number" and state == "integer":
            current_lexeme += data[i][0]

    return lexeme_chain


lexeme = lexical([[' ', 'space'], [' ', 'space'], ['r', 'letter'], ['e', 'letter'], ['p', 'letter'], ['e', 'letter'],
                  ['a', 'letter'], ['t', 'letter'], ['u', 'letter'], ['n', 'letter'], ['t', 'letter'], ['i', 'letter'],
                  ['l', 'letter'], [' ', 'space'], ['r', 'letter'], ['e', 'letter'], ['p', 'letter'], ['e', 'letter'],
                  ['a', 'letter'], ['t', 'letter'], [' ', 'space'], ['u', 'letter'], ['u', 'letter'], [' ', 'space'],
                  [' ', 'space'], [' ', 'space'], [' ', 'space'], ['u', 'letter'], ['n', 'letter'], ['t', 'letter'],
                  ['i', 'letter'], ['l', 'letter'], [' ', 'space'], [';', 'semicolon'], [' ', 'space'], ['<', 'less'],
                  ['>', 'more'], ['=', 'equal'], [' ', 'space'], ['$', 'dollar_sign'], [' ', 'space'], [' ', 'space'],
                  ['a', 'letter'], ['b', 'letter'], [' ', 'space'], [' ', 'space'], ['b', 'letter'], ['c', 'letter'],
                  [' ', 'space'], ['9', 'number'], ['2', 'number'], ['6', 'number'], [' ', 'space'], ['9', 'number'],
                  ['1', 'number'], ['3', 'number'], [' ', 'space'], ['r', 'letter'], [' ', 'space'], ['m', 'letter'],
                  ['y', 'letter'], ['f', 'letter'], ['u', 'letter'], ['n', 'letter'], ['c', 'letter'],
                  ['(', 'bracket1'], ['+', 'plus-minus'], ['-', 'plus-minus'], ['*', 'multiplication'], [' ', 'space'],
                  ['d', 'letter'], ['i', 'letter'], ['v', 'letter'], [' ', 'space'], ['m', 'letter'], ['o', 'letter'],
                  ['d', 'letter'], [')', 'bracket2'], [' ', 'space'], [' ', 'space']])
print(lexeme)
