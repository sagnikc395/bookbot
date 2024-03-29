def count_words(content):
    #counts the number of words in the string 
    return len(content.split(' '))


def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        #print(contents)
    
    print(f"Word Count: {count_words(contents)}")


main()
