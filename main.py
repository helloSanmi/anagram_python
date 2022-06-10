# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):

    if sorted(word.lower()) == sorted(anagram.lower()):
        print('Program return True')
        return True

    print('Program return False')
    return False


user_input = input('Enter first word: ')
user_input_second = input('Enter second wor: ')

find_anagram(user_input, user_input_second);
