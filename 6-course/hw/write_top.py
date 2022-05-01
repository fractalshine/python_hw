def write_top(name, score):
    with open('test2top.txt', 'a') as f:
        f.write(f"{name}:{score}\n")
