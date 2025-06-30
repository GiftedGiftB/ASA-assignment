def return_a_dictionary_and_the_number_of_times_each_word_appeared(word):
    words_to_be_checked = {}
    for letter in word:
        if letter not in words_to_be_checked:
            words_to_be_checked[letter] = 1
        else:
            words_to_be_checked[letter] += 1
    print(words_to_be_checked)






return_a_dictionary_and_the_number_of_times_each_word_appeared("madamme")