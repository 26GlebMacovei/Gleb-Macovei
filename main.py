def sentence():
    sentence = input("Enter the sentence:")
    result=[]
    for capital, comma in sentence:

        if comma == ',':
            result.append(',  ')

        elif capital > 0 and sentence[capital - 1] == sentence[capital].isalpha():
            result.append(comma.upper())
        else:
            result.append(comma)


def main():
    sentence()


main()