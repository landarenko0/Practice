""" file.py
    Модуль работы с файлами. Считывает символьную цепочку из файла INPUT.txt и записывает результат её обработки в файл
    OUTPUT.txt.
    (с) Ландаренко Н. А. (группа КЭ-103) """


def input_data():
    """ Ввод данных. Считывание символьной цепочки. """

    file = open("INPUT.txt", "r")

    chain = file.read()
    return chain


def output_data(result):
    """ Вывод данных. """

    file = open("OUTPUT.txt", "w")

    file.write(result)
