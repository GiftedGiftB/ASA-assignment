def convert_number_to_words(number):
    number_to_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
    }
    #return number_to_words[number]
    return number_to_words.get(number, "invalid number")
if __name__ == '__main__':

    number = int(input("Enter a number: "))

    number_in_word = convert_number_to_words(number)
    print(f"The number {number} is: {number_in_word}")