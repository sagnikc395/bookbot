import os


def word_count(text: str) -> int:
    """
    takes the text from the book as a string and returns
    the number of words in the string
    """
    words = text.split()
    return len(words)


def character_count(text: str) -> dict:
    """
    takes the text from the book as a string, and returns the number
    of times each character appears in the string
    """
    char_count = {}
    text = text.lower()
    for char in text:
        if char not in char_count and char.islower():
            char_count[char] = 1
        elif char.islower():
            char_count[char] += 1
    return char_count


def print_report(file_path, word_count: int, char_count: dict) -> None:
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    for char in char_count:
        print(f"The '{char}' character was found {char_count[char]} times")


with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
# print(file_contents)

file_path = os.path.basename("./books/frankenstein.txt")
print(word_count(file_contents))
print(character_count(file_contents))

print_report(file_path, word_count(file_contents), character_count(file_contents))
