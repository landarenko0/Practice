""" syn.py
    Синтаксический блок. Устанавливает, соответствует ли символьная цепочка заданным формулам Бэкуса-Наура.
    (с) Ландаренко Н. А. (группа КЭ-103) """


def syntax(data):
    """Синтаксический блок. Устанавливает, соответствует ли символьная цепочка заданным формулам Бэкуса-Наура. """

    state = "start"
    i = 0
    accept = True

    while i < len(data):
        if data[i][1] == "keyword_repeat" and state == "start":
            state = "repeat"
        elif data[i][1] == "identifier" and state == "repeat":
            state = "name1"
        elif data[i][1] == "bracket1" and state == "name1":
            state = "bracket1"
        elif data[i][1] == "dollar_sign" and state == "bracket1":
            state = "dollar_sign"
        elif data[i][1] == "hex" and state == "dollar_sign":
            state = "hex"
            hex = data[i][0]
            # Проверка шестнадцатеричного числа.
            for j in range(len(data[i][0])):
                if hex[j] in "0123456789ABCDFabcdf":
                    continue
                else:
                    accept = False
                    break
        elif (data[i][1] == "plus-minus" or data[i][1] == "multiplication" or data[i][1] == "keyword_div" or data[i][1] == "keyword_mod") and state == "hex":
            state = "arythm_sign"
        elif data[i][1] == "identifier" and state == "arythm_sign":
            state = "name2"
        elif data[i][1] == "bracket2" and state == "name2":
            state = "bracket2"
        elif data[i][1] == "keyword_until" and state == "bracket2":
            state = "until"
        elif data[i][1] == "identifier" and state == "until":
            state = "name3"
        elif data[i][1] == "more" and state == "name3":
            state = "more_sign"
        elif data[i][1] == "less" and state == "name3":
            state = "less_sign"
        elif data[i][1] == "equal" and state == "name3":
            state = "equal_sign"
        elif data[i][1] == "plus-minus" and state == "more_sign":
            state = "sign"
        elif data[i][1] == "equal" and state == "more_sign":
            state = "equal_sign"
        elif data[i][1] == "integer" and state == "more_sign":
            state = "integer"
        elif data[i][1] == "plus-minus" and state == "less_sign":
            state = "sign"
        elif data[i][1] == "more" and state == "less_sign":
            state = "equal_sign"
        elif data[i][1] == "equal" and state == "less_sign":
            state = "equal_sign"
        elif data[i][1] == "integer" and state == "less_sign":
            state = "integer"
        elif data[i][1] == "plus-minus" and state == "equal_sign":
            state = "sign"
        elif data[i][1] == "integer" and state == "equal_sign":
            state = "integer"
        elif data[i][1] == "integer" and state == "sign":
            state = "integer"
        elif data[i][1] == "semicolon" and state == "integer":
            state = "semicolon"
        elif state == "semicolon":
            accept = False
            break
        else:
            accept = False
            break

        i += 1

    if accept and state == "semicolon":
        return "ACCEPT"
    else:
        return "REJECT"


#result = syntax([['repeat', 'keyword_repeat'], ['func', 'identifier'], ['(', 'bracket1'], ['$', 'dollar_sign'],
#                 ['123D', 'hex'], ['div', 'keyword_div'], ['min', 'identifier'], [')', 'bracket2'],
#                 ['until', 'keyword_until'], ['St', 'identifier'], ['<', 'less'], ['-', 'plus-minus'],
#                 ['1', 'integer'], [';', 'semicolon']])
#print(result)
