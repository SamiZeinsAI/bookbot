def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    letters = []
    for key in chars_dict:
        if key.isalpha():
            letters.append([chars_dict[key],key])
    letters.sort(reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(num_words,"words found in document\n\n")
    for freq, letter in letters:
        print("The '"+letter+"' character was found",freq," times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
def get_num_words(text):
    words = text.split()
    return len(words)
def get_chars_dict(text):
    chars = dict()
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars



main()