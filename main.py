'''
a module for an easy navigation among json file objects
'''
import sys
import json


def read_file(path: str) -> dict:
    '''
    simple read function, reads json file and returns in as dictionary
    '''
    with open(path, mode="r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def main(path: str):
    '''
    the main functoin for this module
	returns the final result you find by navigating in json file
	works until the object you choose is not list or dict 
    '''
    data = read_file(path)
    while True:
        if isinstance(data, dict):
            data = get_dict_objects(data)
        if isinstance(data, list):
            data = get_list_objects(data)
        else:
            print(data)
            return data

def get_dict_objects(data: dict):
    '''
    a function to get objects from dictionary
    returns the object from dictionary you choose
    '''
    print("\n\nthis is an object\nplease type a property you want to get")
    for key in data.keys():
        print(key)
    my_key = input()
    try:
        return data[my_key]
    except KeyError:
        print("wrong key, please try adain")
        sys.exit()


def get_list_objects(data: list):
    '''
    a function to get objects from list
    returns the object from list you choose
    '''
    try:
        answer = input(f"\n\nthis is a list\nplease type number 1-{len(data)} \
to get an element of that number")
        return data[int(answer)-1]
    except IndexError:
        print("wrong_index, please try again")
        sys.exit()


if __name__ == "__main__":
    main("Obama_friends.json")
