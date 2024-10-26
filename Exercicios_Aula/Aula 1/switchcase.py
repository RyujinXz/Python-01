value = 3 

match value:
    case 1: 
        Result = "one"
    case 2:
        Result ="two"
    case 3: 
        Result = "tree"
    case _:
        Result = "default"

print(Result)
