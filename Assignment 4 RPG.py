#COMP 163 - Introduction to Programming
#Assignment: Chapter 4 - College Life Adventure Game
#Name: Julius Wayne Devon Johnson Jr.
#GitHub Username: JJGB-HB7
#Date: 2/14/2026
#Description: 
#This game takes you through a simulation on the kinds of decisions and circumstances college students find themselves in.
#While it is aimed to be very comedic with dialogue, in real life, college is brutal if you make the wrong choices.
#AI Usage: Minimal. Only uses of AI were to help keep track of the levelling system.

#Introduction
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
current_gpa = float(input("What's your GPA? If you don't have one, you can just put 0 its ok :)"))      
if current_gpa < 0 or current_gpa > 4:
  print("Sorry but...you gotta be honest before you can play this game sooooo")
  print("GAME OVER!")
  print("Ending 1: Dishonesty is never the Policy >:(")
else:
  study_hours = int(input("How many hours do you study within the day?"))
  if study_hours < 0  or study_hours > 24:
    print("You can't study for more than 24 hours a day...thats literally impossible. For being dishonest, TAKE THIS!")
    print("GAME OVER!")
    print("Ending 1: Dishonesty is never the Policy >:(")
  else:
    social_points = int(input("On a scale from 0 to 100, how social are you?"))
    if social_points < 0 or social_points > 100:
      print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
      print("GAME OVER!")
      print("Ending 2: Can't follow simple instructions")
    else:
      stress_level = int(input("On a scale from 0 to 100, how stressed are you?"))
      if stress_level < 0 or stress_level > 100:
        print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
        print("GAME OVER!")
        print("Ending 2: Can't follow simple instructions")
      else:
        print(f"\nWell...I guess that settles everything. Here are your base stats:\n{stats}")
        upgrade_sets = study_hours // 12
        if study_hours > 12:
          print("Oh well it looks like you can upgrade your stats already!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input("Type the first class you wish to upgrade your level: ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input("Type the second class you wish to upgrade your level: ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input("Type the third class you wish to upgrade your level: ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("Upgrades complete!")
          print("Final stats:")
          print(stats)
        print("For every 12 study hours you have, you can increase your level in 3 courses by 1.\nFor every 10 levels of stress, a point will be docked at the end of every week.\nWith everything situated...LETS GET TO YOUR FIRST WEEK!")
        print(" *****   ***   *     *    *****    ****   *****")
        print("*       *   *  *     *    *       *       *    ")
        print("*       *   *  *     *    *****   * ****  *****")
        print("*       *   *  *     *    *       *    *  *    ")
        print(" *****   ***   ****  **** *****    ****   *****")
        print("By: Julius Wayne Devon Johnson Jr.\n\n\n")
        #First Week