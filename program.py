""" program.py
    Головной модуль. Вызывает остальные модули.
    (с) Ландаренко Н. А. (группа КЭ-103) """

from transliterator import transliteration
from lex import lexical
from keyword_identification import identification
from syn import syntax


def Main():
    """ Головной модуль. Вызывает остальные модули. """

    file = open("INPUT.txt", "r")
    chain = file.read()

    file = open("OUTPUT.txt", "w")

    lexeme_chain_trans = transliteration(chain)

    if lexeme_chain_trans != 0:
        print("Transliteration successful")
        lexeme_chain_lex = lexical(lexeme_chain_trans)
    else:
        print("Transliteration unsuccessful. Chain rejected")
        result = "REJECT"
        file.write(result)
        file.close()
        return 0

    if lexeme_chain_lex != 0:
        print("Lexical block is successful")
        lexeme_chain_key = identification(lexeme_chain_lex)
    else:
        print("Lexical block is unsuccessful. Chain rejected")
        result = "REJECT"
        file.write(result)
        file.close()
        return 0

    if lexeme_chain_key != 0:
        print("Keyword identification block is successful")
        result = syntax(lexeme_chain_key)
    else:
        print("Keyword identification block is unsuccessful. Chain rejected")
        result = "REJECT"
        file.write(result)
        file.close()
        return 0

    file.write(result)
    file.close()


Main()
