slides=int(input("How many slides do you want?: "))
print()

for text_input in range(slides):
  print("•••••••")
  text=input("Enter the slide text: ")
  title=input("What is the slide title?: ")
  print("•••••••\n")
  
  print("-------")
  print(title,"\n")
  print(text)
  print("-------")