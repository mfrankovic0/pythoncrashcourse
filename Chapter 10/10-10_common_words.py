def wordcount(filename):
    """Input the name of a txt file and a word and it will count how many times the word appears in the text."""
    try:
        with open(filename, encoding='UTF-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exsit.")
    else:
        num = contents.lower().count(f"{word}")
        print(f"{filename} has approximately {num} appearances of the word {word}.")


filename = input("Type the text file name:")
word = input("Type in the word you want to find:")

wordcount(filename)
