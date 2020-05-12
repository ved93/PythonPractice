# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string.
# If there are two or more words that are the same length, return the first word from the string with that length.
# Ignore punctuation and assume sen will not be empty.


def longest_word(sen):
    word_list = sen.split()
    max_len = 0
    for word in word_list:
        word = "".join(c for c in word if word.isalpha())
        if max_len < len(word):
            max_len = len(word)
            max_len_word = word

    return max_len_word


print(longest_word(input()))
