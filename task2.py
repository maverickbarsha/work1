def Convert(string):
    li = list(string.split(" "))
    return li
str1=input('enter string')
L=(Convert(str1))
L=L[-1::-1]
print(L)
output=' '.join(L)
print(output)
