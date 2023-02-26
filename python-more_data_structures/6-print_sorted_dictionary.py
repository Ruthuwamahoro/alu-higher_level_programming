def print_sorted_dictionary(a_dictionary):
    dictionary=sorted(a_dictionary.keys())
    for dict in dictionary:
        print("{}:{}".format(dict,dictionary[dict]))
