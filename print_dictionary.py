def print_dict(n):

    i=1
    dict= {}
    while(i<n+1):
        dict.update({i:i**2})
        i=i+1
    print (dict)


n=int(input("Enter a value for n upto whose square is to be added: "))
print_dict(n)