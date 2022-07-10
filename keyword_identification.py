""" keywords_identification.py
    Блок идентификации ключевых слов. устанавливает, какое из ключевых слов языка Pascal соответствует заданному
    идентификатору, либо сообщает, что заданный идентификатор не является ключевым словом языка Pascal.
    (с) Ландаренко Н. А. (группа КЭ-103) """

keywords = ["and", "array", "begin", "case", "const", "div", "do", "downto", "else", "end", "file", "for",
            "function", "goto", "if", "in", "label", "mod", "nil", "not", "of", "or", "packed", "procedure",
            "program", "record", "repeat", "set", "then", "to", "type", "until", "var", "while", "with"]


def linear_search(word):
    """ Линейный поиск. Выполняет поиск по списку ключевых слов. """

    for i in range(len(keywords)):
        if word.lower() == keywords[i]:
            return 1
    return 0


def identification(data):
    """ Блок идентификации ключевых слов. Устанавливает, какое из ключевых слов языка Pascal соответствует заданному
    идентификатору, либо сообщает, что заданный идентификатор не является ключевым словом языка Pascal. """

    for i in range(len(data)):
        if data[i][0] == "repeat" or data[i][0] == "Repeat" or data[i][0] == "REPEAT":
            data[i][1] = "keyword_repeat"
        elif data[i][0] == "until" or data[i][0] == "Until" or data[i][0] == "UNTIL":
            data[i][1] = "keyword_until"
        elif data[i][0] == "div" or data[i][0] == "Div" or data[i][0] == "DIV":
            data[i][1] = "keyword_div"
        elif data[i][0] == "mod" or data[i][0] == "Mod" or data[i][0] == "MOD":
            data[i][1] = "keyword_mod"
        else:
            if linear_search(data[i][0]) == 1:
                return 0

    return data


#lexeme = identification([['repeat', 'identifier'], ['func', 'identifier'], ['(', 'bracket1'], ['$', 'dollar_sign'],
#                         ['123D', 'hex'], ['div', 'identifier'], ['min', 'identifier'], [')', 'bracket2'],
#                         ['until', 'identifier'], ['St', 'identifier'], ['<', 'less'], ['-', 'plus-minus'],
#                         ['1', 'integer'], [';', 'semicolon']])
#print(lexeme)
