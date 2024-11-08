def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_dict_list = convert_dict_to_list(chars_dict)
    
    #sort 
    chars_dict_list.sort(reverse=True, key=sort_on)

    print_report(chars_dict_list, num_words, book_path)
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
        return len(text.split())

def get_chars_dict(text):
    counts = {}
    
    for c in text:
        lowered_c = c.lower()
        if lowered_c in counts:
            counts[lowered_c]+=1
        else:
            counts[lowered_c] = 1
    return counts
    
def convert_dict_to_list(dict):
    result = []
    for c in dict:
        result.append({"name": c, "num": dict[c]})
    return result
    
def sort_on(dict):
    return dict["num"]

def print_report(list, num_words, path):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    
    for c in list:
        if c["name"].isalpha():
            print(f"The '{c["name"]}' character was found {c["num"]} times") 

    print("--- End report ---")

main()