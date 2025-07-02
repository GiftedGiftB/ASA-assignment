#def return_a_dictionary_and_the_number_of_times_each_word_appeared(word):
 #   words_to_be_checked = {}
  #  for letter in word:
   #     if letter not in words_to_be_checked:
    #        words_to_be_checked[letter] = 1
     #   else:
      #      words_to_be_checked[letter] += 1
    # print(words_to_be_checked)

#def use_a_set_to_add_numbers(numbers):
   # numbers_to_add = set(numbers)
    #for number in numbers_to_add:
     #   numbers_to_add.add(number)
    #return numbers_to_add
    #print(use_a_set_to_add_numbers({1, 5, 4, 8,5,3,9,1}))

def return_the_square_of_number_that_is_divisible_by_5(number):
    if number % 5 == 0:
        return number * number
    else:
        return number % 5
        #print(number)


print(return_the_square_of_number_that_is_divisible_by_5(25))
# return_a_dictionary_and_the_number_of_times_each_word_appeared("madamme")
#use_a_set_to_add_numbers()