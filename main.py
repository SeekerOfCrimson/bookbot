def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    print(f"Let the report of {book_path} commence!")
    print(f"{num_words} words found in the document")
    for char in char_dict:
        print(f"The letter {char} was found {char_dict[char]} times.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_char_dict(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in char_dict:
                char_dict[char] +=1
            else:
                char_dict[char] = 1
        else:
            pass
    return char_dict

main()