from random import randint


def read_text_file(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [item.replace('\\n', '\n')[:-1] for item in file.readlines() if item]

def get_random_str_from_array(str_array: list):
    id = randint(0, len(str_array)-1)
    return str_array[id]


# def read_text_file(file_path):
#     file_content = []
#     with open(file_path, 'r', encoding='utf-8') as file:
#         file_content = file.readlines()
#     return [item.replace('\\n', '\n')[:-1] for item in file_content if item]