def input_data():
    file = open("INPUT.txt", "r")

    chain = file.read()
    return chain


def output_data(result):
    file = open("OUTPUT.txt", "w")

    file.write(result)
