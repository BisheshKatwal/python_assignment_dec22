def sort(str):

    str=sorted(str.split(","))
    str=",".join(str)
    return str

str=input("enter the string of words seperated by comma: ")

print(sort(str))