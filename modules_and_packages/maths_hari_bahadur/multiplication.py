def multiply(*args):
    if len(args)==0:
        return "Can't multiply empty things, can I ?"
    value=1
    for num in args:
        value = num * value
    return value
    
