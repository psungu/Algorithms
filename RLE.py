def compress(text):
  result = ""
  counter = 1
  for i in range(len(text)):
    if not text[i]==" ":
      if i<len(text)-1 and text[i] == text[i+1]:
        counter+=1
      else:
        result+= text[i]+str(counter)
    elif i==0 or not text[i-1] == " ":
      result+= text[i]

  return result
