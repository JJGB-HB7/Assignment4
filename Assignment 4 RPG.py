#COMP 163 - Introduction to Programming
#Assignment: Chapter 4 - College Life Adventure Game
#Name: Julius Wayne Devon Johnson Jr.
#GitHub Username: JJGB-HB7
#Date: 2/14/2026
#Description: 
#This game takes you through a simulation on the kinds of decisions and circumstances college students find themselves in.
#While it is aimed to be very comedic with dialogue, in real life, college is brutal if you make the wrong choices.
#AI Usage: Minimal. Only uses of AI were to help keep track of the levelling system.

#=============================
#Introduction
#=============================
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
items = {}
GPA = {}
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
        #=============================
        #Upgrade
        #=============================
        upgrade_sets = study_hours // 12
        if upgrade_sets > 0:
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
          #=============================
          #Upgrade twice
          #=============================
        if upgrade_sets > 0:
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
        print("\nFor every 12 study hours you have, you can increase your level in 3 courses by 1.\nIf you have a max amount of stress, you'll need to rest or else you may damage your mind.\nA point will be docked in one random class at the end of every week if your level of stress exceeds 100.\nHowever, having negative stress is lazy.\nTry having a lot of social skills. They may help you with future endevors. You never know...\n\nWith everything situated...LETS GET TO YOUR FIRST WEEK!\n")
        print("-----------------------------------------------")
        print(" *****   ***   *     *    *****    ****   *****")
        print("*       *   *  *     *    *       *       *    ")
        print("*       *   *  *     *    *****   * ****  *****")
        print("*       *   *  *     *    *       *    *  *    ")
        print(" *****   ***   ****  **** *****    ****   *****")
        print("-----------------------------------------------")
        print("By: Julius Wayne Devon Johnson Jr.\n\n\n")
        #=============================
        #First Week
        #=============================
        print("---------------------------------------------------")
        print(" *          *    *****    *****    *    *      **  ")
        print(" *    **    *    *        *        *   *     *  *  ")
        print(" *  *   *   *    *****    *****    * *          *  ")
        print(" * *      * *    *        *        *   *        *  ")
        print(" *          *    *****    *****    *    *     *****")
        print("---------------------------------------------------")
        #=============================
        #choice 1
        #=============================
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
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        elif mainchoice == 3:
          print("So you just decided to forget your classes.\nIsn't that...what you came to college for though?\nEh its your story.\nCan't tell you how to live it.")
          stats["Study Points"] += 0
          stats["Stress"] -= 5
          stats["Social"] += 7
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        else:
          print("Since you didn't pay attention to the instructions, we'll just say you couldn't get outta bed today.\nMakes sense.\nThat bed is comfortable.\nBut Imma still give you a punishment")
          stats["Study Points"] -= 2
          stats["Stress"] -= 10
          stats["Social"] += 0
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        print(stats)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        #=============================
        #choice 2
        #=============================
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
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        elif mainchoice == 2:
          print("So you went to the function.\nI feel you.\nHave fun! This is college after all!")
          stats["Study Points"] += 0
          stats["Stress"] -= 15
          stats["Social"] += 10
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        elif mainchoice == 3:
          print("So you decided to go to the library.\nGlad you're taking initiative!")
          stats["Study Points"] += 3
          stats["Stress"] += 2
          stats["Social"] += 0
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        else:
          print("Since you didn't pay attention to the instructions, we'll just say you still couldn't get outta bed today.\nMakes sense.\nThat bed is...still comfortable.\nBut Imma still give you a punishment")
          stats["Study Points"] -= 4
          stats["Stress"] -= 10
          stats["Social"] += 0
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        print(stats)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        #choice 3
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
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        elif mainchoice == 2:
          print("Well thats good because you're just in time for a surprise syllabus quiz.")
          if stats["Computer Science"] >= 1:
            print("It was lightwork for you anyways")
            stats["Study Points"] += 8
            stats["Stress"] -= 15
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            #choice of luck
            print("Pick a number between 1 and 5")
            pass_or_fail = int(input())
            failure1 = random.randint(1,5)
            failure2 = random.randint(1,5)
            if pass_or_fail == failure1 or pass_or_fail == failure2:
              print("Dang...I guess you weren't good enough to pass...Its alright though. Keep your head up")
              stats["Study Points"] -= 5
              stats["Stress"] += 25
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Oh shoot! I guess lady luck answered your prayer! Nice job.")
              stats["Study Points"] += 4
              stats["Stress"] -= 10
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
        else:
          print("Ight you must be doing this on purpose at this point. So imma just say that you still couldn't get outta bed. Tough world")
          stats["Study Points"] -= 10
          stats["Stress"] -= 25
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
          print("It looks like you're stress levels exeeded 100. You now must give up one stat point from each of your classes.")
          stats["Math"] -= 1
          stats["English"] -= 1
          stats["Computer Science"] -= 1
          stats["Science"] -= 1
          stats["Music"] -= 1
          stats["History"] -= 1
          print("Final stats:")
          print(stats)
        if stats["Stress"] < 0:
          print("It looks like you have negative stress levels. You have to take one stat point from one class")
          choice1 = input(f"Type the class you wish to downgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] -= 1
            print(f"{choice1} decreased to {stats[choice1]}.")
        print("Week 1 Complete! CONGRATULATIONS")
        print("Stress Resetted")
        stats["Stress"] = 0
        #Second Week
        print("-------------------------------------------------------")
        print(" *          *    *****    *****    *    *     *****    ")
        print(" *    **    *    *        *        *   *     *     *   ")
        print(" *  *   *   *    *****    *****    * *            *    ")
        print(" * *      * *    *        *        *   *        *      ")
        print(" *          *    *****    *****    *    *     ******   ")
        print("-------------------------------------------------------")
        #choice 1
        print("\nIt's tuesday and your room started flooding last night! They definitely need to fix these residence halls...Anyways, pick between 1 and 2")
        print("--------------------------------------------------------------------------------------------")
        print("1: 1")
        print("2: 2")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do.\n{stats}\nMake your choice: "))
        pipeline_fail = random.randint(1,2)
        if mainchoice == pipeline_fail:
          print("Unfortunately, since you left your bookbag on the floor last night, all of your textbooks, notes, and notebooks got soaked.\nWhat an unfortunate world we live in...")
          print("-1 to all class/study stats")
          stats["Math"] -= 1
          stats["Music"] -= 1
          stats["Science"] -= 1
          stats["History"] -= 1
          stats["Computer Science"] -= 1
          stats["English"] -= 1
          stats["Stress"] += 25
          stats["Social"] += 0
          stats["Study Points"] -= 1
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        elif mainchoice != pipeline_fail:
          print("Thankfully, before going to bed, you put your bookbag on your desk, preventing it from getting soaked.\nGood thinking last night!\nBuuut you still have a flooded room...")
          stats["Stress"] += 5
        else:
          print("You just don't want to play by the rules. Thats okay though. You won't ragebait me. I'll just keep you in bed forever giving you punishments.")
          stats["Study Points"] -= 20
          stats["Stress"] -= 10
          if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        print(stats)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        #choice 2
        print("Its Wednesday and a group of people in your math class are forming a study group. You're not a part of the conversation but you're nearby.")
        print("What do you do?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Walk up to them and ask to join their study group | -15 Social | +2 Math and +8 Study Points Every New Week")
        print("2: I don't wanna self insert myself into the group. | Free |")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          if stats["Social"] >= 15:
            print("You've joined a math study group! This will definitely help in the future")
            items["Math Study Group"] = 1
          else:
            print("Oops...your social skills are lacking and you get social anxiety. You run away without ever interacting with them.")
        elif mainchoice == 2:
          print("You told yourself you don't need a study group. At least you stuck to your morals.")
        else:
          print("Since you didn't pay attention to the instructions, we'll just say you had your headphones in and couldn't hear")
        print(stats)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        print(f"\nThats the end of week 2. pretty decent. Lets see your stats so far...\n{stats}")
        if stats["Stress"] > 100:
          print("It looks like you're stress levels exeeded 100. You now must give up one stat point from each of your classes.")
          stats["Math"] -= 1
          stats["English"] -= 1
          stats["Computer Science"] -= 1
          stats["Science"] -= 1
          stats["Music"] -= 1
          stats["History"] -= 1
          print("Final stats:")
          print(stats)
        if stats["Stress"] < 0:
          print("It looks like you have negative stress levels. You have to take one stat point from one class")
          choice1 = input(f"Type the class you wish to downgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] -= 1
            print(f"{choice1} decreased to {stats[choice1]}.")
        print("Week 2 Complete! CONGRATULATIONS")
        print("Stress Resetted")
        stats["Stress"] = 0
        #Third Week
        print("-------------------------------------------------------")
        print(" *          *    *****    *****    *    *     *****    ")
        print(" *    **    *    *        *        *   *          *    ")
        print(" *  *   *   *    *****    *****    * *        *****    ")
        print(" * *      * *    *        *        *   *          *    ")
        print(" *          *    *****    *****    *    *     *****    ")
        print("-------------------------------------------------------")
        if "Math Study Group" in items:
          stats["Math"] += 2
          stats["Study Points"] += 8

        if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        essay = 8
        music_sheet = 2
        history_project = 12
        math_test = 6
        #choice 1
        print("Its monday again. Your english professor is giving you an essay due at the beginning of next week ")
        print("Dr. Ruff gave you a new sheet of music to memorize by wednesday")
        print("Your History professor gave you a project on the history of Iceland due on the fifth week")
        print("You have a math test at the end of the fourth week")
        print("\n\nThere are a lot of things that need to be done. How're you going to approach them?\n")
        print("Essay: -8 Study Points | +20 Stress | +2 English")
        print("Music: -2 Study Points | +5 Stress | +2 Music")
        print("Project: -12 Study Points | +30 Stress | +2 History")
        print("Test: -6 Study Points | +15 Stress | +2 Math")
        print("--------------------------------------------------------------------------------------------")
        print("1: Begin to write the essay")
        print("2: Begin to memorize the music")
        print("3: Start the History project")
        print("4: Study for the test")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print(f"You began to write the essay. How far do you get?\n{stats}")
          subtract_hours = int(input("How many study hours do you wish to use?: "))
          essay -= subtract_hours
          if essay <= 0:
            print("You've completed the assignment!")
            stats["Study Points"] -= 8
            stats["Stress"] += 20
            stats["English"] += 2
            items["Essay"] = True
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            print("Good job. But theres still some more work to get done")
            print(f"Points needed to complete essay: {essay}")
        elif mainchoice == 2:
          print(f"You began to memorize the music. How far do you get?\n{stats}")
          subtract_hours = int(input("How many study hours do you wish to use?: "))
          music_sheet -= subtract_hours
          if music_sheet <= 0:
            print("You've memorized the music!")
            stats["Study Points"] -= 2
            stats["Stress"] += 5
            stats["Music"] += 2
            items["Music Sheet"] = True
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            print("Good job. But theres still some more work to get done")
            print(f"Remaining points needed to memorize the music: {music_sheet}")
        elif mainchoice == 3:
          print(f"You began to make your project. How far do you get?\n{stats}")
          subtract_hours = int(input("How many study hours do you wish to use?: "))
          history_project -= subtract_hours
          if history_project <= 0:
            print("You've completed the project!")
            stats["Study Points"] -= 8
            stats["Stress"] += 30
            stats["History"] += 2
            items["History Project"] = True
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            print("Good job. But theres still some more work to get done")
            print(f"Remaining points needed to complete the project: {history_project}")
        elif mainchoice == 4:
          print(f"You began to study for your math test. How far do you get?\n{stats}")
          subtract_hours = int(input("How many study hours do you wish to use?: "))
          math_test -= subtract_hours
          if math_test <= 0:
            print("You're prepared for the test")
            stats["Study Points"] -= 6
            stats["Stress"] += 15 
            stats["Math"] += 2
            items["Math Test"] = True
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            print("Good job. But theres still some more work to get done")
            print(f"Remaining points needed to complete your studying: {math_test}")
        else:
          print("You didn't start anything...bruh.")
        print(stats)
        print(items)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        print("\nDon't worry. You'll have more time tomorrow.\n")
        #choice 2
        print("Its Tuesday night and you're at home. You hear on twitter that J Cole is hiding on campus! What do you do?\n")
        print("--------------------------------------------------------------------------------------------")
        print("1: Find him and get a CD | +20 Social | -20 Stress |")
        print("2: I need to get my work done... | +5 Study Points |")
        print("3: Walk in the other direction towards the library to do work... | +7 Study Points | +5 Stress |")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print("You tried finding J Cole and you actually found him! buuut you don't get a CD.\nYou really thought you were gonna be able to get through the sea of students?\nLMAO")
          stats["Social"] += 20
          stats["Stress"] -= 20
        elif mainchoice in (2, 3):
          if mainchoice == 2:
            print("So you decided to stay home and do your work.\nI respect the grind but geez man.\nNot even for J Cole??")
            stats["Study Points"] += 5
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          else:
            print("So you decided to go to the library. Look at this LOSER!\nNah jk but seriously...thats crazy.")
            stats["Study Points"] += 7
            stats["Stress"] += 5
            if stats["Study Points"] >= 12:
              upgrade_sets += 1
              stats["Study Points"] -= 12
          print("--------------------------------------------------------------------------------------------")
          if "Essay" not in items:
            print(f"1: Write the essay | {essay} points needed |")
          if "Music Sheet" not in items:
            print(f"2: Memorize the music | {music_sheet} points needed |")
          if "History Project" not in items:
            print(f"3: Work on the History project | {history_project} points needed |")
          if "Math Test" not in items:
            print(f"4: Study for the test | {math_test} points needed |")
          print("--------------------------------------------------------------------------------------------")
          mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
          
          if mainchoice == 1:
            print(f"You work on the essay. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            essay -= subtract_hours
            if essay <= 0:
              print("You've completed the assignment!")
              stats["Study Points"] -= 8
              stats["Stress"] += 20
              stats["English"] += 2
              items["Essay"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Points needed to complete essay: {essay}")
          elif mainchoice == 2:
            print(f"You work to memorize the music. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            music_sheet -= subtract_hours
            if music_sheet <= 0:
              print("You've memorized the music!")
              stats["Study Points"] -= 2
              stats["Stress"] += 5
              stats["Music"] += 2
              items["Music Sheet"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to memorize the music: {music_sheet}")
          elif mainchoice == 3:
            print(f"You began to make your project. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            history_project -= subtract_hours
            if history_project <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 8
              stats["Stress"] += 30
              stats["History"] += 2
              items["History Project"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {history_project}")
          elif mainchoice == 4:
            print(f"You began to study for your math test. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            math_test -= subtract_hours
            if math_test <= 0:
              print("You're prepared for the test")
              stats["Study Points"] -= 6
              stats["Stress"] += 15 
              stats["Math"] += 2
              items["Math Test"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete your studying: {math_test}")
          else:
            print("You didn't start anything...bruh.")
          print(stats)
          print(items)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        print("\nMaybe you'll see J Cole another day. Who knows?\n")
        #Music Check
        print("Its Wednesday! Dr.Ruff is doing music checks. Have you memorized it?\n")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah")
        print("2: Yeah")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if "Music Sheet" in items:
          if mainchoice == 1:
            print("You liar! But glad you memorized it!")
            stats["Social"] -= 1
          elif mainchoice == 2:
            print("Great! Look at you being a great musician.")
            stats["Social"] += 3
          else:
            print("Don't know what you said but it looks like you memorized it")
        else:
          if mainchoice == 1:
            print("Dissappointing. But at least you were honest about it.")
            stats["Social"] += 1
            stats["Music"] -= 2
          elif mainchoice == 2:
            print("How dare you lie to my face? You MAGGOT!")
            stats["Music"] -= 2
            stats["Social"] -= 3
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
          print("\nToday is thursday. Today is the last day you have to work on anything due at the beginning of next week because of the band performance this weekend.")
          print("--------------------------------------------------------------------------------------------")
          if "Essay" not in items:
            print(f"1: Write the essay | {essay} points needed |")
          if "History Project" not in items:
            print(f"2: Work on the History project | {history_project} points needed |")
          if "Math Test" not in items:
            print(f"3: Study for the test | {math_test} points needed |")
          print("--------------------------------------------------------------------------------------------")
          mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
          
          if mainchoice == 1:
            print(f"You work on the essay. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            essay -= subtract_hours
            if essay <= 0:
              print("You've completed the assignment!")
              stats["Study Points"] -= 8
              stats["Stress"] += 20
              stats["English"] += 2
              items["Essay"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Points needed to complete essay: {essay}")
          elif mainchoice == 2:
            print(f"You began to make your project. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            history_project -= subtract_hours
            if history_project <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 8
              stats["Stress"] += 30
              stats["History"] += 2
              items["History Project"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {history_project}")
          elif mainchoice == 3:
            print(f"You began to study for your math test. How far do you get?\n{stats}")
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            math_test -= subtract_hours
            if math_test <= 0:
              print("You're prepared for the test")
              stats["Study Points"] -= 6
              stats["Stress"] += 15 
              stats["Math"] += 2
              items["Math Test"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete your studying: {math_test}")
          if upgrade_sets > 0:
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
        print("\nHope the performance goes well!\n")
        print("Since you had a marching band performance, your social level doubled!")
        stats["Social"] *= 2
        print(f"That's the end of week 3. Let's look at the final stats:\n{stats}")
        if stats["Stress"] > 100:
          print("It looks like you're stress levels exeeded 100. You now must give up one stat point from each of your classes.")
          stats["Math"] -= 1
          stats["English"] -= 1
          stats["Computer Science"] -= 1
          stats["Science"] -= 1
          stats["Music"] -= 1
          stats["History"] -= 1
          print("Final stats:")
          print(stats)
        if stats["Stress"] < 0:
          print("It looks like you have negative stress levels. You have to take one stat point from one class")
          choice1 = input(f"Type the class you wish to downgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] -= 1
            print(f"{choice1} decreased to {stats[choice1]}.")
        print("Week 3 Complete! CONGRATULATIONS")
        print("Stress Resetted")
        stats["Stress"] = 0
        #Fourth Week
        print("-------------------------------------------------------")
        print(" *          *    *****    *****    *    *     *   *    ")
        print(" *    **    *    *        *        *   *      *   *    ")
        print(" *  *   *   *    *****    *****    * *        *****    ")
        print(" * *      * *    *        *        *   *          *    ")
        print(" *          *    *****    *****    *    *         *    ")
        print("-------------------------------------------------------")
        if "Math Study Group" in items:
          stats["Math"] += 2
          stats["Study Points"] += 8
        if stats["Study Points"] >= 12:
            upgrade_sets += 1
            stats["Study Points"] -= 12
        chemistry = 7
        Programming = 14
        Music_Theory = 4
        #choice 1
        print("\nIt's Monday. Have you finished your essay?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah")
        print("2: Yeah")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if "Essay" in items:
          if mainchoice == 1:
            print("You liar! But glad you did it!")
            stats["Social"] -= 1
          elif mainchoice == 2:
            print("Great! Look at you being an estounding writer.")
            stats["Social"] += 3
          else:
            print("Don't know what you said but it looks like you did it")
        else:
          if mainchoice == 1:
            print("Dissappointing. But at least you were honest about it.")
            stats["Social"] += 1
            stats["English"] -= 2
          elif mainchoice == 2:
            print("How dare you lie to my face? You MAGGOT!")
            stats["English"] -= 2
            stats["Social"] -= 3

        print("New Assignment: Chemistry Elemental Equations | Due Friday of this week | +4 Science | +10 Stress |\n")
        print("New Assignment: Music Theory Worksheet | Due Wednesday of this week | +4 Music | +5 Stress |\n")
        print("New Assignment: Programming RPG Game | Due Fifth Week | +6 Programming | +30 Stress |\n")
        print("A lot of new assignments opened up to complete. Good Luck!")
        print("Your friends invited you to a drinking party. Do you go?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah. I've got work to do | +10 Study Points | +15 Stress |")
        print("2: I'll go but I won't drink. Gotta preserve my body. | +20 Social | -20 Stress")
        print("3: GIMME ALL THE SHOTS! | +35 Social | -50 Stress")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 1:
          print("Choose what you wish to work on:")
          print("------------------------------------------------------------------------------------------")
          if "History Project" not in items:
            print("-1: Work on History Project")
          if "Math Test" not in items:
            print("0: Study for Math Test")
          print("1: Work on Chemistry Homework")
          print("2: Work on Music Theory")
          print("3: Work on RPG Game")
          choice1 = int(input("Make your Choice: "))
          if "History Project" not in items and choice1 == -1:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            history_project -= subtract_hours
            if history_project <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 8
              stats["Stress"] += 30
              stats["History"] += 2
              items["History Project"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {history_project}") 
          if "Math Test" not in items and choice1 == 0:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            math_test -= subtract_hours
            if math_test <= 0:
              print("You've completed your studying!")
              stats["Study Points"] -= 6
              stats["Stress"] += 15
              stats["Math"] += 2
              items["Math Test"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete it: {math_test}")
          if choice1 == 1:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            chemistry -= subtract_hours
            if chemistry <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 7
              stats["Stress"] += 10
              stats["Science"] += 4
              items["Chemistry Assignment"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {chemistry}")

          if choice1 == 2:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            Music_Theory -= subtract_hours
            if Music_Theory <= 0:
              print("You've completed the Music Theory Worksheet!")
              stats["Study Points"] -= 8
              stats["Stress"] += 30
              stats["Music"] += 2
              items["Music Theory"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {Music_Theory}")
          
          if choice1 == 3:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            Programming -= subtract_hours
            if Programming <= 0:
              print("You've completed the RPG!")
              stats["Study Points"] -= 14
              stats["Stress"] += 30
              stats["Computer Science"] += 2
              items["RPG Game"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {Programming}")
        if mainchoice == 2:
          print("You had fun! Good for you")
          stats["Social"] += 20
          stats["Stress"] -= 20
        if mainchoice == 3:
          print("You got absolutely wasted...Oh lord")
          stats["Stress"] -= 50
          stats["Social"] += 35

        print(stats)
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        print("\nAnother day complete!\n")
        #choice 2
        print("Its Wednesday. Have you completed the music theory worksheet?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah")
        print("2: Yeah")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Tell the truth. Be mindful of your stats\n{stats}\nMake your choice: "))
        if "Music Theory" in items:
          if mainchoice == 1:
            print("You liar! But glad you did it!")
            stats["Social"] -= 1
          elif mainchoice == 2:
            print("Great! Look at you being an astounding musician. Gotta tell everyone about you.")
            stats["Social"] += 3
          else:
            print("Don't know what you said but it looks like you did it")
        else:
          if mainchoice == 1:
            print("Dissappointing. But at least you were honest about it.")
            stats["Social"] += 1
            stats["Music"] -= 2
          elif mainchoice == 2:
            print("How dare you lie to my face? You MAGGOT!")
            stats["Music"] -= 2
            stats["Social"] -= 3

        print("Today, nothing is really happening. Its a chill day. What should you do?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Just go get some rest | +0 Study Points | set Stress to 0 | +0 Social |")
        print("2: Smoke with the boys | +0 Study Points | -15 Stress | +10 Social |")
        print("3: Study | +6 Study Points | +5 Stress | +0 Social |")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Choose what you wish to do. Be mindful of your stats\n{stats}\nMake your choice: "))
        if mainchoice == 3:
          print("What do you choose to work on?")
          print("------------------------------------------------------------------------------------------")
          if "History Project" not in items:
            print("0: Work on History Project")
          if "Math Test" not in items:
            print("1: Study for Math Test")
          if "Chemistry" not in items: 
            print("2: Work on Chemistry Homework")
          if "Programming" not in items:
            print("3: Work on RPG Game")
          print("------------------------------------------------------------------------------------------")
          choice1 = int(input("Make your Choice: "))
          if "History Project" not in items and choice1 == 0:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            history_project -= subtract_hours
            if history_project <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 8
              stats["Stress"] += 30
              stats["History"] += 2
              items["History Project"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {history_project}") 
          if "Math Test" not in items and choice1 == 1:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            math_test -= subtract_hours
            if math_test <= 0:
              print("You've completed your studying!")
              stats["Study Points"] -= 6
              stats["Stress"] += 15
              stats["Math"] += 2
              items["Math Test"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete it: {math_test}")
          if "Chemistry" not in items and choice1 == 2:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            chemistry -= subtract_hours
            if chemistry <= 0:
              print("You've completed the project!")
              stats["Study Points"] -= 7
              stats["Stress"] += 10
              stats["Science"] += 4
              items["Chemistry Assignment"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {chemistry}")

          if "RPG Game" not in items and choice1 == 3:
            subtract_hours = int(input("How many study hours do you wish to use?: "))
            Programming -= subtract_hours
            if Programming <= 0:
              print("You've completed the RPG!")
              stats["Study Points"] -= 14
              stats["Stress"] += 30
              stats["Computer Science"] += 2
              items["RPG Game"] = True
              if stats["Study Points"] >= 12:
                upgrade_sets += 1
                stats["Study Points"] -= 12
            else:
              print("Good job. But theres still some more work to get done")
              print(f"Remaining points needed to complete the project: {Programming}")
        #=============================
        #Upgrade
        #=============================
        if upgrade_sets > 0:
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
        print("\nLightwork\n")
        print("Its Friday. Are you ready for your test?")
        print("--------------------------------------------------------------------------------------------")
        print("1: Nah")
        print("2: Yeah")
        print("--------------------------------------------------------------------------------------------")
        mainchoice = int(input(f"Tell the truth. Be mindful of your stats\n{stats}\nMake your choice: "))
        if "Math Test" in items:
          print("Congrats! You studied so much that you blitzed through this test with no problems.")
          stats["Math"] += 2
          stats["Stress"] == 0
        else:
          if stats["Math"] >= 10:
            print("Well in any case, you passed. Great job")
            stats["Math"] += 2
            stats["Stress"] == 0
          else:
            if 5 <= stats["Math"] < 10:
              print("Welp. You know the drill.")
              luck = int(input("Pick a number from 1 to 3:"))
              passed = random.randint(1,3)
              if (1 <= luck <= 3) and luck == passed:
                print("Well lady luck heard your prayers because YOU PASSED!")
                stats["Math"] += 2
                stats["Stress"] == 0
              else:
                print("Sorry but...you failed") 
                stats["Stress"] += 75
                stats["Math"] -= 2
        if upgrade_sets > 0:
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
        print(f"That's the end of week 4. Let's look at the final stats:\n{stats}")
        if stats["Stress"] > 100:
          print("It looks like you're stress levels exeeded 100. You now must give up one stat point from each of your classes.")
          stats["Math"] -= 1
          stats["English"] -= 1
          stats["Computer Science"] -= 1
          stats["Science"] -= 1
          stats["Music"] -= 1
          stats["History"] -= 1
          print("Final stats:")
          print(stats)
        if stats["Stress"] < 0:
          print("It looks like you have negative stress levels. You have to take one stat point from one class")
          choice1 = input(f"Type the class you wish to downgrade your level. Please be mindful of how you type\n{stats}:\n ")
          if choice1 in stats:
            stats[choice1] -= 1
            print(f"{choice1} decreased to {stats[choice1]}.")
        print("Week 4 Complete! CONGRATULATIONS")
        print("Stress Resetted")
        stats["Stress"] = 0
#=========================================
#Finals Week
#=========================================
        print("---------------------------------------------------------------")
        print(" **********  **********  *       *   *****   *         *****   ")
        print(" **              **      * *     *  *     *  *        *        ")
        print(" ******          **      *   *   *  *******  *         *****   ")
        print(" **              **      *     * *  *     *  *              *  ")
        print(" **          **********  *       *  *     *  *******   *****   ")
        print("---------------------------------------------------------------")
        print(stats)
        print("Look at how far you've come. Now comes the deciding factor.")
        if stats["Math"] >= 20:
          ("You got an A in math")
          GPA["Math"] == 16
        elif 15 <= stats["Math"] < 20:
          ("You got a B in math")
          GPA["Math"] == 12
        elif 10 <= stats["Math"] < 15:
          ("You got a C in math")
          GPA["Math"] == 8
        elif 5 <= stats["Math"] < 10:
          ("You got a D in math")
          GPA["Math"] == 4
        else:
          ("You got an F in math...")
          GPA["Math"] == 0

        if stats["History"] >= 20:
          ("You got an A in history")
          GPA["History"] == 12
        elif 15 <= stats["History"] < 20:
          ("You got a B in history")
          GPA["History"] == 9
        elif 10 <= stats["History"] < 15:
          ("You got a C in history")
          GPA["History"] == 6
        elif 5 <= stats["History"] < 10:
          ("You got a D in history")
          GPA["History"] == 3
        else:
          ("You got an F in history...")
          GPA["History"] == 0

        if stats["Computer Science"] >= 20:
          ("You got an A in COMP")
          GPA["Computer Science"] == 12
        elif 15 <= stats["Computer Science"] < 20:
          ("You got a B in COMP")
          GPA["Computer Science"] == 9
        elif 10 <= stats["Computer Science"] < 15:
          ("You got a C in COMP")
          GPA["Computer Science"] == 6
        elif 5 <= stats["Computer Science"] < 10:
          ("You got a D in COMP")
          GPA["Computer Science"] == 3
        else:
          ("You got an F in COMP...")
          GPA["Computer Science"] == 0

        if stats["Science"] >= 20:
          ("You got an A in science")
          GPA["Science"] == 16
        elif 15 <= stats["Science"] < 20:
          ("You got a B in science")
          GPA["Science"] == 12
        elif 10 <= stats["Science"] < 15:
          ("You got a C in science")
          GPA["Science"] == 8
        elif 5 <= stats["Science"] < 10:
          ("You got a D in science")
          GPA["Science"] == 4
        else:
          ("You got an F in science...")
          GPA["Science"] == 0

        if stats["English"] >= 20:
          ("You got an A in english")
          GPA["English"] == 12
        elif 15 <= stats["Math"] < 20:
          ("You got a B in english")
          GPA["English"] == 9
        elif 10 <= stats["Math"] < 15:
          ("You got a C in english")
          GPA["English"] == 6
        elif 5 <= stats["Math"] < 10:
          ("You got a D in english")
          GPA["English"] == 3
        else:
          ("You got an F in english...")
          GPA["English"] == 0

        if stats["Music"] >= 20:
          ("You got an A in music")
          GPA["Music"] == 4
        elif 15 <= stats["Music"] < 20:
          ("You got a B in music")
          GPA["Music"] == 3
        elif 10 <= stats["Music"] < 15:
          ("You got a C in music")
          GPA["Music"] == 2
        elif 5 <= stats["Music"] < 10:
          ("You got a D in music")
          GPA["Music"] == 1
        else:
          ("You got an F in music...")
          GPA["Music"] == 0
        total_points = (
          GPA["Math"] +
          GPA["History"] +
          GPA["Computer Science"] +
          GPA["Science"] +
          GPA["English"] +
          GPA["Music"]
        )
        total_classes = 6
        final_gpa = total_points / total_classes
        print(f"Total GPA for the semester: {final_gpa} ")
        