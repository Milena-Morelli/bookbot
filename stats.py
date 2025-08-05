#Milena Way
"""
def get_book_text(book):
    with open(book) as filepath:
        return filepath.read()

def words_counter(book):
    string = get_book_text(book)
    words = string.split()
    return len(words)

def divide_letters(book):
    book_string = get_book_text(book)
    letters = [char for char in book_string.lower()]
    letter_dict = {}
    for letter in letters:
        x = 1
        if letter in letter_dict:
            x += letter_dict[letter]
        letter_dict[letter] = x
    return letter_dict

def listify(book):
    dict = divide_letters(book)
    list = []
    for key, value in dict.items():
        list.append({"char":(key), "num":(value)})
    return list

def sort_on(dict):
    return dict["num"]

def sort_two(dict):
    return dict["char"]

def sort_print(book):
    list = listify(book)
    list.sort(reverse=True, key=sort_on)
    for i in range (0, len(list)):
        num = sort_on(list[i])
        key = sort_two(list[i])
        if key.isalpha():
            print (f"{key}: {num}")

def print_final(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    letter_count = words_counter(book)
    print(f"Found {letter_count} total words")
    print("--------- Character Count -------")
    sort_print(book)
    print("============= END ===============")
"""
    
#After Boots Feedback

def get_book_text(book):
    with open(book) as filepath:
        return filepath.read()

def words_counter(book):
    whole_string = get_book_text(book)
    words = whole_string.split()
    return len(words)

def divide_letters(book):
    book_string = get_book_text(book)
    letters = [char for char in book_string.lower()]
    letter_dict = {}
    for letter in letters:
        x = 1
        if letter in letter_dict:
            x += letter_dict[letter]
        letter_dict[letter] = x
    return letter_dict

def sort_on(mini_dict):
    return mini_dict["num"]

def list_sort_print(book):
    char_dict = divide_letters(book)
    char_list = []
    for key, value in char_dict.items():
        char_list.append({"char":(key), "num":(value)})
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        if item["char"].isalpha():
            print (f"{item["char"]}: {item["num"]}")


def print_final(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    letter_count = words_counter(book)
    print(f"Found {letter_count} total words")
    print("--------- Character Count -------")
    list_sort_print(book)
    print("============= END ===============")

