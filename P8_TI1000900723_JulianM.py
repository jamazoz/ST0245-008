def dosdigitos(num):
    if num <= 1:
        print("1 ",end="")
        return 0
    else:
        print(num," ",end="")
        return 0 + dosdigitos(num-1)

dosdigitos(23)