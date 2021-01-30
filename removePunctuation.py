

txt = input("text: ")


def removePunctuation(txt):
  list = [] #An empty list is created to hold char and space characters without punctuation in the String entered in the parameter.
  for s in txt:
     if  s == ".":
        continue
     elif s ==",":
        continue
     elif s == "'":
        continue
     elif s == ":":
        continue
     elif s == ";":
        continue
     elif s == "?":
        continue
     elif s == "!":
        continue
     elif s == '"':
        continue
     elif s == "(":
        continue
     elif s == ")":
        continue
     elif s == "-":
        continue
     else:
        list.append(s)

  return ''.join(list)


print(removePunctuation(txt))
