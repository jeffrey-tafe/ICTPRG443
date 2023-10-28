import os

def prompt_text_file_path():
    path = input("Text File Path: ")
    if not is_valid_text_file(path):
        print(f"\nThat path is not valid. Terminating operation.")
        return False
    return path



def is_valid_text_file(file_path):
    return os.path.isfile(file_path) and file_path.lower().endswith('.txt')

def read_text_file(path):
    try:
        with open(path, 'r') as file:
            file_contents = file.read()
            return file_contents
    except Exception as e:
        print(f"Error: {e}")
        return False


def text_to_set(text):
    return set(text.split())


def main():
    path = prompt_text_file_path()
    if path is False:
        return

    text = read_text_file(path)
    if text is False:
        return

    set_list = text_to_set(text)
    print(set_list)

if __name__ == '__main__':
    main()