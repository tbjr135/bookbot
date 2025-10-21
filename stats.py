def get_num_words(book_text):
    book_split = book_text.split()
    num_words = len(book_split)
    return num_words

def count_chars(book_text):
    from collections import Counter

    lower_case_book = book_text.lower()
    count = Counter(lower_case_book)

    return count

def sort_alpha_counts(char_dict):
    # 1️⃣ Filter to keep only alphabetic characters
    alpha_only = {k: v for k, v in char_dict.items() if k.isalpha()}
    
    # 2️⃣ Sort by count (value) in descending order
    sorted_items = sorted(alpha_only.items(), key=lambda item: item[1], reverse=True)
    
    # 3️⃣ Convert back to dictionary
    sorted_dict = dict(sorted_items)

    # Print each key-value pair on its own line
    for char, count in sorted_dict.items():
        print(f"{char}: {count}")
    
    return sorted_dict