""" lex.py
    Лексический блок. Преобразует цепочку лексем, полученную от транслитератора, в цепочку лексем вида
    ("символ входного языка", "класс символа входного языка").
    (с) Ландаренко Н. А. (группа КЭ-103) """


def isEmpty(letter):
    """ Проверяет, является ли лексема пустой. """

    if letter == "":
        return True
    else:
        return False


def lexical(data):
    """ Лексический блок. Преобразует цепочку лексем, полученную от транслитератора, в цепочку лексем вида
    ("символ входного языка", "класс символа входного языка"). """

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
            return 0
        elif data[i][1] == "number" and state == "integer":
            current_lexeme += data[i][0]

    if not isEmpty(current_lexeme):
        lexeme_chain.append([current_lexeme, lexeme_class])
    return lexeme_chain


lexeme = lexical([['r', 'letter'], ['e', 'letter'], ['p', 'letter'], ['e', 'letter'], ['a', 'letter'], ['t', 'letter'],
                  ['t', 'letter'], [' ', 'space'], ['f', 'letter'], ['u', 'letter'], ['n', 'letter'], ['c', 'letter'],
                  ['(', 'bracket1'], ['$', 'dollar_sign'], ['A', 'letter'], ['B', 'letter'], ['C', 'letter'],
                  [' ', 'space'], ['d', 'letter'], ['i', 'letter'], ['v', 'letter'], [' ', 'space'], ['m', 'letter'],
                  ['i', 'letter'], ['n', 'letter'], [')', 'bracket2'], [' ', 'space'], ['u', 'letter'], ['n', 'letter'],
                  ['t', 'letter'], ['i', 'letter'], ['l', 'letter'], [' ', 'space'], ['B', 'letter'], ['<', 'less'],
                  ['1', 'number'], ['0', 'number'], [';', 'semicolon']])
print(lexeme)
