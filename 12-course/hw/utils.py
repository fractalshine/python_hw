import json


def load_json():
    """Выгружаем посты в список из файла"""

    with open('posts.json', encoding='utf-8') as f:
        raw_json = f.read()

    post_list = json.loads(raw_json)

    return post_list


# function to add to JSON
def write_json(new_data, filename='posts.json'):
    with open(filename, 'r+', encoding='utf-8') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, ensure_ascii=False,
                  indent=2)

    # python object to be appended

