#https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def validBraces(string):
  a = "[]"
  b = "{}"
  c = "()"
  while (string.find(a) != -1) or (string.find(b) != -1) or (string.find(c) != -1):
    if (string.find(a) != -1):
      string=string.replace(a,"")
    if (string.find(b) != -1):
      string=string.replace(b,"")
    if (string.find(c) != -1):
      string=string.replace(c,"")
  return not len(string)
