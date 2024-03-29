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


def print_report(content, path_name):
    # aggreagete all the words and character data into a nice report
    # that we can print to the console
    print(f"--- Begin report of {path_name} ---")
    print(f"{count_words(content)} words found in the document\n")
    res = dict()
    for char in content.lower():
        if char.isalpha():
            if char in res:
                res[char] += 1
            else:
                res[char] = 1
    ## sorting dicts by value
    res_sort = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
    for k, v in res_sort.items():
        print(f"The {k} character was found {v} times")
    print("--- End report ---")


def main():
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        # print(contents)

    # print(f"Word Count: {count_words(contents)}")
    # print(f"{count_letters(contents)}")
    path_name = "/books/frankestein.txt"
    print_report(contents, path_name)


main()
