def count_words(book_contents) -> int:
    count = 0
    for w in book_contents.split():
        count += 1
    return count

def count_chars(book_contents) -> dict:
    count = {}
    for c in book_contents:
        c = c.lower()
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count


def sort_dict_by_value(d: dict) -> list:
    """
    Sorts a dictionary by its values in descending order and returns a list of dictionaries
    """
    sorted_lists = []

    for key, value in sorted(d.items(), key=lambda item: item[1], reverse=True):
        sorted_lists.append({'char': key, 'num': value})
 
    return sorted_lists
