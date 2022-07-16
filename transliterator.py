""" transliterator.py
    Блок транслитерации. Выполняет транслитерацию символьной цепочки.
    (с) Ландаренко Н. А. (группа КЭ-103) """


def transliteration(chain):
    """ Блок транслитерации. Преобразует исходную символьную цепочку в цепочку лексем вида
    ("символ цепочки", "класс символа цепочки"). """

    lexeme_chain = []

    # Каждому символу присваивается свой класс. Если встречен неизвестный символ, возвращаем 0.
    for i in range(len(chain)):
        symbol = chain[i]
        symbol_class = []
        if str.isalpha(symbol):
            class_of_symbol = "letter"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif str.isnumeric(symbol):
            class_of_symbol = "number"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == ";":
            class_of_symbol = "semicolon"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol in "+-":
            class_of_symbol = "plus-minus"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol in "*":
            class_of_symbol = "multiplication"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == " ":
            class_of_symbol = "space"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == "(":
            class_of_symbol = "bracket1"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == ")":
            class_of_symbol = "bracket2"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == "$":
            class_of_symbol = "dollar_sign"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == ">":
            class_of_symbol = "more"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == "<":
            class_of_symbol = "less"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        elif symbol == "=":
            class_of_symbol = "equal"
            symbol_class.append(symbol)
            symbol_class.append(class_of_symbol)
        else:
            return 0

        lexeme_chain.append(symbol_class)

    return lexeme_chain


lexeme = transliteration("repeat func($ABC div min) until B<10;")
print(lexeme)
