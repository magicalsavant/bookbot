def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    #print(file_contents)
    word_count, words = count_words(file_contents)
    letter_count = count_letters(file_contents)
    #print(letter_count)
    print_letter_report(letter_count)

    
def count_words(text):
    words = text.split()
    #print(len(words))
    return len(words), words

def count_letters(text):
    text = text.lower()
    letter_counts = {}
    for word in text:
        for letter in word:
            if letter not in letter_counts:
                letter_counts[letter] = 1
            else:
                letter_counts[letter]+=1
    #print(letter_counts)
    letter_counts = dict(sorted(letter_counts.items()))
    return letter_counts

def print_letter_report(letter_counts):
    letters_represented = 0
    for letter, count in letter_counts.items():
        if letter.isalpha():
            print(f"The letter '{letter}' was found {count} times")
            letters_represented+=1
    print(f"{letters_represented} letters were represented")
    
main()