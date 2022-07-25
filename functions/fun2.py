# function to count the no. of vowels 

from unittest import result


def vowel_counter(sentence):
    result={}

    for vowel in "aeiou":
        result[vowel]= sentence.lower().count(vowel)
    return result

if __name__ == "__main__":
    msg = "This is a test"
    print(vowel_counter(msg))