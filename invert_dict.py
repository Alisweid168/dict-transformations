def invert_dictionary(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict

employee_scores = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
print(invert_dictionary(employee_scores))