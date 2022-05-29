thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)


print("========")
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)