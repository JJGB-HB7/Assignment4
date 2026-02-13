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
import random
print("Welcome to your first week of classes! Before we begin, let's get a good description of you.")
student_name = input("What is your name?")
stats = {
  "Math" : 0,
  "Science" : 0,
  "History" : 0,
  "English" : 0,
  "Computer Science" : 0,
  "Music" : 0,
  "Stress": 0,
  "Social": 0,
  "Study Points": 0
        }
current_gpa = float(input("What's your GPA? If you don't have one, you can just put 0 its ok :)"))      
if current_gpa < 0 or current_gpa > 4:
  print("Sorry but...you gotta be honest before you can play this game sooooo")
  print("GAME OVER!")
  print("Ending 1: If you're gonna lie, at least make it make sense >:(")
else:
  study_hours = int(input("How many hours do you study within the day?"))
  if study_hours < 0  or study_hours > 24:
    print("You can't study for more than 24 hours a day...thats literally impossible. For being dishonest, TAKE THIS!")
    print("GAME OVER!")
    print("Ending 1: If you're gonna lie, at least make it make sense >:(")
  else:
    social_points = int(input("On a scale from 0 to 100, how social are you?"))
    if social_points < 0 or social_points > 100:
      print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
      print("GAME OVER!")
      print("Ending 2: Can't follow simple instructions")
    else:
      stats["Social"] += social_points

      stress_level = int(input("On a scale from 0 to 100, how stressed are you?"))
      if stress_level < 0 or stress_level > 100:
        print("I said on a scale FROM 0 TO 100! You can't follow instructions? HOW'D YOU GET INTO COLLEGE??")
        print("GAME OVER!")
        print("Ending 2: Can't follow simple instructions")
      else:
        stats["Stress"] += stress_level

        print(f"\nWell...I guess that settles everything. Here are your base stats:\n{stats}")
        upgrade_sets = study_hours // 12
        if study_hours >= 12:
          print("Oh well it looks like you can upgrade your stats already!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input(f"Type the first class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input(f"Type the second class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input(f"Type the third class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("\nUpgrades complete!")
          print("Final stats:")
          print(stats)
        if study_hours >= 12:
          print("\nOh dang! I guess you have another upgrade. Look at you having a headstart!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input(f"Type the first class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input(f"Type the second class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input(f"Type the third class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("\nUpgrades complete!")
          print("Final stats:")
          print(stats)
        print("\nFor every 12 study hours you have, you can increase your level in 3 courses by 1.\nIf you have a max amount of stress, you'll need to rest or else you may damage your mind.\nA point will be docked in one random class at the end of every week if your level of stress exceeds 100.\nHowever, having a lot of social skills may help you with future endevors. You never know...\n\nWith everything situated...LETS GET TO YOUR FIRST WEEK!\n")
        print("-----------------------------------------------")
        print(" *****   ***   *     *    *****    ****   *****")
        print("*       *   *  *     *    *       *       *    ")
        print("*       *   *  *     *    *****   * ****  *****")
        print("*       *   *  *     *    *       *    *  *    ")
        print(" *****   ***   ****  **** *****    ****   *****")
        print("-----------------------------------------------")
        print("By: Julius Wayne Devon Johnson Jr.\n\n\n")
        #First Week
        print("---------------------------------------------------")
        print(" *          *    *****    *****    *    *      **  ")
        print(" *    **    *    *        *        *   *     *  *  ")
        print(" *  *   *   *    *****    *****    * *          *  ")
        print(" * *      * *    *        *        *   *        *  ")
        print(" *          *    *****    *****    *    *     *****")
        print("---------------------------------------------------")
        print("\nIt's monday and you have five classes with a lot of them being back-to-back.\nSounds like a terrible way to start your first day.")
        print("Maybe it might be better to skip one or two classes...you're not doing anything in there anyways. But that might leave a bad imprint...\n")
        print("--------------------------------------------------------------------------------------------")
        print("1: Just thug through the day. It wouldn't be a great first impression if I missed my classes | +4 Study Points | +10 Stress | +1 Social |")
        print("2: Maybe I'll skip one or two classes. Its the first day. We aren't doing anything in a lot of them anyways. | +2 Study Points | +5 Stress | +3 Social |")
        print("3: Screw my classes, FIRST DAY ON CAMPUS BABYYYYY!!!! | +0 Study Points | -5 Stress | +7 Social |")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print("So you went to all your classes. You thugged it out and made it through most of your day.\nYou may be tired but at least you showed up\nNot many people do that")
          stats["Study Points"] += 4
          stats["Stress"] += 10
          stats["Social"] += 1
        elif mainchoice == 2:
          print("So you decided to skip some of them early morning classes.\nWe get it...aint nobody trying to be in class at no 8AM.\nBut you still made sure to show up to the afternoon classes. ")
          stats["Study Points"] += 2
          stats["Stress"] += 5
          stats["Social"] += 3
        elif mainchoice == 3:
          print("So you just decided to forget your classes.\nIsn't that...what you came to college for though?\nEh its your story.\nCan't tell you how to live it.")
          stats["Study Points"] += 0
          stats["Stress"] -= 5
          stats["Social"] += 7
        else:
          print("Since you didn't pay attention to the instructions, we'll just say you couldn't get outta bed today.\nMakes sense.\nThat bed is comfortable.\nBut Imma still give you a punishment")
          stats["Study Points"] -= 2
          stats["Stress"] -= 10
          stats["Social"] += 0
        print(stats)
        upgrade_sets = study_hours // 12
        if study_hours >= 12:
          print("Oh well it looks like you can upgrade your stats already!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input(f"Type the first class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input(f"Type the second class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input(f"Type the third class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("\nUpgrades complete!")
          print("Final stats:")
          print(stats)
        print("\nWell the first day is always the lightest. No worries\n")
        print("Its Wednesday night and you're hearing about a function thats supposed to be happening. Sounds fun. There's no assignments at the moment.")
        print("--------------------------------------------------------------------------------------------")
        print("1: Just go get some rest | +0 Study Points | -20 Stress | +0 Social |")
        print("2: LETS GO TO THE FUNCTION YEAAAA BABYYYYYY!!! | +0 Study Points | -15 Stress | +10 Social |")
        print("3: Even though I don't have assignments, imma do some studying. Maybe I'll go to the library... | +3 Study Points | +2 Stress | +0 Social |")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print("So you went to sleep. Very understandable. You were pretty tired from classes.")
          stats["Study Points"] += 0
          stats["Stress"] -= 20
          stats["Social"] += 0
        elif mainchoice == 2:
          print("So you went to the function.\nI feel you.\nHave fun! This is college after all!")
          stats["Study Points"] += 0
          stats["Stress"] -= 15
          stats["Social"] += 10
        elif mainchoice == 3:
          print("So you decided to go to the library.\nGlad you're taking initiative!")
          stats["Study Points"] += 3
          stats["Stress"] += 2
          stats["Social"] += 0
        else:
          print("Since you didn't pay attention to the instructions, we'll just say you still couldn't get outta bed today.\nMakes sense.\nThat bed is...still comfortable.\nBut Imma still give you a punishment")
          stats["Study Points"] -= 4
          stats["Stress"] -= 10
          stats["Social"] += 0
        print(stats)
        upgrade_sets = study_hours // 12
        if study_hours >= 12:
          print("Oh well it looks like you can upgrade your stats already!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input(f"Type the first class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input(f"Type the second class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input(f"Type the third class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("\nUpgrades complete!")
          print("Final stats:")
          print(stats)
        print("\nThere will always be more functions in store for you.\n")
        print("Its Friday. Do you go to your 9AM Computer Science class?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah")
        print("2: Yeah")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print("You definitely should've...because he just gave out a random syllabus quiz and since you weren't there, thats a 0 in the gradebook")
          stats["Study Points"] -= 6
          stats["Stress"] += 10
          stats["Social"] -= 5
        elif mainchoice == 2:
          print("Well thats good because you're just in time for a surprise syllabus quiz.")
          if stats["Computer Science"] >= 1:
            print("It was lightwork for you anyways")
            stats["Study Points"] += 8
            stats["Stress"] -= 15
          else:
            print("Pick a number between 1 and 5")
            pass_or_fail = int(input())
            failure1 = random.randint(1,5)
            failure2 = random.randint(1,5)
            if pass_or_fail == failure1 or pass_or_fail == failure2:
              print("Dang...I guess you weren't good enough to pass...Its alright though. Keep your head up")
              stats["Study Points"] -= 5
              stats["Stress"] += 25
            else:
              print("Oh shoot! I guess lady luck answered your prayer! Nice job.")
              stats["Study Points"] += 4
              stats["Stress"] -= 10
        else:
          print("Ight you must be doing this on purpose at this point. So imma just say that you still couldn't get outta bed. Tough world")
          stats["Study Points"] -= 10
          stats["Stress"] -= 25
        upgrade_sets = study_hours // 12
        if study_hours >= 12:
          print("Oh well it looks like you can upgrade your stats already!")
          print(f"You have {upgrade_sets} upgrade set(s).")
          choice1 = input(f"Type the first class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] += 1
            print(f"{choice1} increased to {stats[choice1]}!")
          choice2 = input(f"Type the second class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice2 in stats:
            stats[choice2] += 1
            print(f"{choice2} increased to {stats[choice2]}!")
          choice3 = input(f"Type the third class you wish to upgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice3 in stats:
            stats[choice3] += 1
            print(f"{choice3} increased to {stats[choice3]}!")
          upgrade_sets -= 1
          print("\nUpgrades complete!")
          print("Final stats:")
          print(stats)
        print(f"\nThats the end of week 1. Not too shabby. Lets see your stats so far...\n{stats}")
        if stats["Stress"] > 100:
          print("It looks like you're stress levels exeeded 100. You now must give up one stat point from one of your classes.")
          choice1 = (input("Which one will you take away?: "))
          if choice1 in stats:
            stats[choice1] -= 1
            print(f"{choice1} decreased to {stats[choice1]}...")
            print("Final stats:")
            print(stats)
          else:
            print("You're ragebaiting me...I know it.")
            stats["Study Points"] -= 10
        print("Week 1 Complete! CONGRATULATIONS")
        print("-------------------------------------------------------")
        print(" *          *    *****    *****    *    *     *****    ")
        print(" *    **    *    *        *        *   *     *     *   ")
        print(" *  *   *   *    *****    *****    * *            *    ")
        print(" * *      * *    *        *        *   *        *      ")
        print(" *          *    *****    *****    *    *     ******   ")
        print("-------------------------------------------------------")
        