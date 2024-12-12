def word_count(contents):
    return str(len(contents.split()))


def character_count(contents):
    a = "abcdefghijklmnopqrstuvwxyz"
    lower_contents = contents.lower()
    chars = {}
    for i in a:
        count = 0
        for j in lower_contents:
            if j == i:
                count += 1
        chars[i] = count
    return chars


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = word_count(file_contents)
        chars = character_count(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print("")

        for key in chars:
            print(f"The '{key}' character was found {chars[key]} times")

        print("--- End report ---")


main()

