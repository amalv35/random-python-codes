import random 

top_of_range =input("type a number boi:")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
      print("type a number largerr than this suckaaa")
      quit()
else:
   print("you should be entering numbers boi") 
   quit() 

rand_number = random.randint(0,top_of_range)
print(rand_number)
guesses =0

while True :
   guesses+=1
   check_number =input("guess a number boi:")
   if check_number.isdigit():
    check_number=int(check_number)


   else:
     print("you should be entering numbers boi") 
     continue

   if check_number== rand_number:
     print("well done boi u made uncle proud")
     break
   
   elif check_number>rand_number:
     print("you were above the number")
   else:
     print("you were below the number")
   print("better luck next time ")

print("it took you", guesses, "guesses, sighhhh.....")