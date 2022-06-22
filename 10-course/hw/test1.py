from utils import load_candidates

candidates_list = load_candidates()

user_input = input("Input")

for d in candidates_list:
    string = d['skills']
    list = string.split(", ")
    if user_input in list:
        print(list)
