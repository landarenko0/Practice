""" keywords_identification.py
    Блок идентификации ключевых слов. устанавливает, какое из ключевых слов языка Pascal соответствует заданному
    идентификатору, либо сообщает, что заданный идентификатор не является ключевым словом языка Pascal.
    (с) Ландаренко Н. А. (группа КЭ-103) """

keywords = ["and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for",
            "function", "goto", "if", "in", "label", "mod", "nil", "not", "of", "or", "packed", "procedure",
            "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with"]


def linear_search(word):
    """ Линейный поиск. Выполняет линейный поиск по списку ключевых слов. """

    for i in range(len(keywords)):
        if word == "repeat" or word == "Repeat" or word == "REPEAT":
            return 1
        elif word == "until" or word == "Until" or word == "UNTIL":
            return 2
        elif word == "div" or word == "Div" or word == "DIV":
            return 3
        elif word == "mod" or word == "Mod" or word == "MOD":
            return 4
        elif word.lower() == keywords[i]:
            return 0


def identification(data):
    """ Блок идентификации ключевых слов. Устанавливает, какое из ключевых слов языка Pascal соответствует заданному
    идентификатору, либо сообщает, что заданный идентификатор не является ключевым словом языка Pascal. """

    for i in range(len(data)):
        if linear_search(data[i][0]) == 1:
            data[i][1] = "keyword_repeat"
        elif linear_search(data[i][0]) == 2:
            data[i][1] = "keyword_until"
        elif linear_search(data[i][0]) == 3:
            data[i][1] = "keyword_div"
        elif linear_search(data[i][0]) == 4:
            data[i][1] = "keyword_mod"
        elif linear_search(data[i][0]) == 0:
            return 0

    return data


#lexeme = identification([['repeat', 'identifier'], ['func', 'identifier'], ['(', 'bracket1'], ['$', 'dollar_sign'],
#                         ['123D', 'hex'], ['div', 'identifier'], ['min', 'identifier'], [')', 'bracket2'],
#                         ['until', 'identifier'], ['St', 'identifier'], ['<', 'less'], ['-', 'plus-minus'],
#                         ['1', 'integer'], [';', 'semicolon']])
#print(lexeme)
