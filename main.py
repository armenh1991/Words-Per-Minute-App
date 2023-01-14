from words import word_list
import random
import time
start = time.time()


chosen_word = random.choice(word_list)
count = 0


user_input = input(f" the word is: {chosen_word} ")

while True:
    if user_input == chosen_word:
        count += 1
        word_list.remove(chosen_word)
        chosen_word = random.choice(word_list)
        user_input = input(f"the word is: {chosen_word} ")

    else:
        a = time.time()-start
        print(f" WPM: {count / a * 60}" )
        break






