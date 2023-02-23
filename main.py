slides=int(input("How many slides do you want?: "))
print()

for text_input in range(slides):
  if text_input>0:
    print("\n<slide break>\n")
  text=input("Enter the slide text: ")
  title=input("\nWhat is the slide title?: ")
  print("\n<slide break>\n")
  
  print("-------")
  print(title,"\n")
  print(text)
  print("-------")