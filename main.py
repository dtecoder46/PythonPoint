slides=int(input("How many slides do you want?: "))
print()

for text_input in range(slides):
  list_option=input("Do you want a numbered list, bullet list, none, or all?")
  
  print("<slide break>\n")
  text=input("Enter the slide text: ")
  title=input("What is the slide title?: ")
  print("\n<slide break>\n")
  
  print("-------")
  print(title,"\n")
  print(text)
  print("-------")