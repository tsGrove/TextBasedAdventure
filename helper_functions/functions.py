import random

def random_element_from_list(custom_list):
    random_selection = custom_list[random.randint(0, (len(custom_list) - 1))]
    return random_selection