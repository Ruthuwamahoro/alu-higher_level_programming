def search_replace(my_list, search, replace):
    for element in my_list:
        if element != search:
            return element
        else:
            return replace
