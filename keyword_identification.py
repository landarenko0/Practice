def identification(data):
    keywords = ["and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for",
                "function", "goto", "if", "in", "label", "mod", "nil", "not", "of", "or", "packed", "procedure",
                "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with"]

    for i in range(len(data)):
        if data[i][0] == "repeat" or data[i][0] == "Repeat" or data[i][0] == "REPEAT":
            data[i][1] = "keyword_repeat"
        elif data[i][0] == "until" or data[i][0] == "Until" or data[i][0] == "UNTIL":
            data[i][1] = "keyword_until"
        elif data[i][0] == "div" or data[i][0] == "Div" or data[i][0] == "DIV":
            data[i][1] = "keyword_div"
        elif data[i][0] == "mod" or data[i][0] == "Mod" or data[i][0] == "MOD":
            data[i][1] = "keyword_mod"
        elif data[i][0] in keywords:
            data[i][1] = "keyword"

    return data


lexeme = identification([['repeatuntil', 'identifier'], ['repeat', 'identifier'], ['uu', 'identifier'],
                         ['until', 'identifier'], [';', 'semicolon'], ['<', 'less'], ['>', 'more'], ['=', 'equal'],
                         ['$', 'dollar_sign'], ['ab', 'hex'], ['bc', 'identifier'], ['926', 'integer'],
                         ['913', 'integer'], ['r', 'identifier'], ['myfunc', 'identifier'], ['(', 'bracket1'],
                         ['+', 'plus-minus'], ['-', 'plus-minus'], ['*', 'multiplication'], ['div', 'identifier'],
                         ['mod', 'identifier']])
print(lexeme)
