def count_words(content):
    # counts the number of words in the string
    return len(content.split())


def count_letters(content):
    # takes the text from the book as a string and returns the number of times each character
    # appears in the string
    # case independent
    content = content.lower()
    char_dict = dict()
    for c in content:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict


def main():
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        # print(contents)

    print(f"Word Count: {count_words(contents)}")
    print(f"{count_letters(contents)}")


main()
