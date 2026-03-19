

def main():



    input_sentence = input('enter a string: ')

    result = input_sentence[0]

    for i in range (1, len(input_sentence)):
        char = input_sentence[i]
        if char.isupper():
            result += ' '
            char = char.lower()
        result += char

    print(result)

main()
