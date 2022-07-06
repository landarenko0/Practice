from transliterator import transliteration
from lex import lexical
from keyword_identification import identification
from syn import syntax
import file


def Main():
    chain = file.input_data()

    lexeme_chain_trans = transliteration(chain)

    if lexeme_chain_trans != 0:
        print("Transliteration successful")
        lexeme_chain_lex = lexical(lexeme_chain_trans)
    else:
        print("Transliteration unsuccessful. Chain rejected")
        result = "REJECT"
        file.output_data(result)
        return 0

    if lexeme_chain_lex != 0:
        print("Lexical block is successful")
        lexeme_chain_key = identification(lexeme_chain_lex)
    else:
        print("Lexical block is unsuccessful. Chain rejected")
        result = "REJECT"
        file.output_data(result)
        return 0

    if lexeme_chain_key != 0:
        print("Keyword identification block is successful")
        result = syntax(lexeme_chain_key)
    else:
        print("Keyword identification block is unsuccessful. Chain rejected")
        result = "REJECT"
        file.output_data(result)
        return 0

    file.output_data(result)


Main()
