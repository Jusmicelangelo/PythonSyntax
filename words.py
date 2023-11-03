def print_upper_words (list_words, must_start_with):
    for word in list_words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
