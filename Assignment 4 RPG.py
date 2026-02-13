print("Assignment 4: Choice based RPG Adventure")
#Character creation
print("Welcome to your first week of classes! Before we begin, let's get a good description of you.")
student_name = input("What is your name?")
stats = {
  "Math" : 0,
  "Science" : 0,
  "History" : 0,
  "English" : 0,
  "Computer Science" : 0,
  "Music" : 0
        }
current_gpa = float(input("What's your GPA? If you don't have one, you can just put 0 its ok :)")          
if current_gpa < 0 or current_gpa > 4:
  print("Sorry but...you gotta be honest before you can play this game sooooo")
  print("GAME OVER!")
  print("Ending 1: Dishonesty is never the Policy >:|")
                    
study_hours = int(input("How many hours do you study within the day?"))
if study_hours < 0  or study_hours > 24:
  print("You can't study for more than 24 hours a day...thats literally impossible. For being dishonest, TAKE THIS!")
  print("GAME OVER!")
  print("Ending 1: Dishonesty is never the Policy >:|")
  
social_points = int(input("On a scale from 0 to 100, how social are you?")
if social_points < 0 or social_points > 100:
  print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
  print("GAME OVER!")
  print("Ending 2: Can't follow simple instructions")

stress_level = int(input("On a scale from 0 to 100, how stressed are you?")
if stress_level < 0 or stress_level > 100:
  print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
  print("GAME OVER!")
  print("Ending 2: Can't follow simple instructions")
