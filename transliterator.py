def transliteration(chain):
    lexeme_chain = []

    for i in range(len(chain)):
        symbol_class = []
        if str.isalpha(chain[i]):
            class_of_symbol = "letter"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif str.isnumeric(chain[i]):
            class_of_symbol = "number"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == ";":
            class_of_symbol = "semicolon"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] in "+-":
            class_of_symbol = "plus-minus"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] in "*":
            class_of_symbol = "multiplication"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == " ":
            class_of_symbol = "space"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == "(":
            class_of_symbol = "bracket1"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == ")":
            class_of_symbol = "bracket2"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == "$":
            class_of_symbol = "dollar_sign"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == ">":
            class_of_symbol = "more"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == "<":
            class_of_symbol = "less"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        elif chain[i] == "=":
            class_of_symbol = "equal"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)
        else:
            class_of_symbol = "error"
            symbol_class.append(chain[i])
            symbol_class.append(class_of_symbol)

        lexeme_chain.append(symbol_class)

    return lexeme_chain


lexeme = transliteration("  repeatuntil repeat uu    until ; <>= $  ab  bc 926 913 r myfunc(+-* div mod)  ")
print(lexeme)
