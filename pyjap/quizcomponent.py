import random

daysOftheYear = [("1st day of the month", "tsuitachi"),
                 ("2nd day of the month", "futsuka"),
                 ("3rd day of the month", "mikka"),
                 ("4th day of the month", "yokka"),
                 ("5th day of the month", "itsuka"),
                 ("6th day of the month", "muika"),
                 ("7th day of the month", "nanoka"),
                 ("8th day of the month", "youka"),
                 ("9th day of the month", "kokonoka"),
                 ("10th day of the month", "tooka")]

monthsOftheYear = [("January","ichigatsu"),
                   ("February", "nigatsu"),
                   ("March", "sangatsu"),
                   ("April","shigatsu"),
                   ("May", "gogatsu"),
                   ("June", "rokugatsu"),
                   ("July", "shichigatsu"),
                   ("August","hachigatsu"),
                   ("September","kugatsu"),
                   ("October","juugatsu"),
                   ("November","juichigatsu"),
                   ("December","junigatsu")]

hoursOfaDay = [
        ("1:00", "ichiji"),
        ("2:00", "niji"),
        ("3:00", "sanji"),
        ("4:00", "yoji"),
        ("5:00", "goji"),
        ("6:00", "rokuji"),
        ("7:00", "shichiji"),
        ("8:00", "hachiji"),
        ("9:00", "kuji"),
        ("10:00", "juuji"),
        ("11:00", "juuichiji"),
        ("12:00", "juuniji"),
        ("What time?", "nanji"),
        ("AM", "gozen"),
        ("PM", "gogo")
        ]

minutesOfAnHourReference = {
        "1" : "ippun",
        "2" : "nifun",
        "3" : "sanpun",
        "4" : "yonpun",
        "5" : "gofun",
        "6" : "roppun",
        "7" : "nanafun",
        "8" : "happun",
        "9" : "kyuufun",
        "10" : "juppun",
        }

japaneseNumbers = {
        "1" : "ichi",
        "2" : "ni",
        "3" : "san",
        "4" : "yon",
        "5" : "go",
        "10": "juu"
        }

def generateMinutesOfAnHourDictionary():
    minutesOfAnHour = []
    for minute in range(1,60):
        quotient = minute/10
        if quotient <= 1:
            minutesOfAnHour.append((str(minute), minutesOfAnHourReference[str(minute)]))
        else:
            remainder = minute % 10
            minutesInJapanese = ""
            
            if remainder == 0:
                minutesInJapanese = "{}{}".format(japaneseNumbers[str(int(quotient))], minutesOfAnHourReference["10"])
            else:
                baseMin = round(quotient - round(remainder/10,1))
                if baseMin == 1:
                    minutesInJapanese = "{}{}".format(japaneseNumbers["10"], minutesOfAnHourReference[str(remainder)])
                else:
                    minutesInJapanese = "{}{}{}".format(japaneseNumbers[str(baseMin)], japaneseNumbers["10"], minutesOfAnHourReference[str(remainder)])
                
            minutesOfAnHour.append((str(minute), minutesInJapanese))

    return minutesOfAnHour

minutesOfAnHour = generateMinutesOfAnHourDictionary()
quizSetSelections = {"Days of the Year": daysOftheYear, "Months of the Year": monthsOftheYear, "Hours of a Day": hoursOfaDay, "Minutes of an Hour": minutesOfAnHour}

def quizQuestion(shitsumon):
    maxLength = len(shitsumon)-1
    correctAnswers = 0
    
    while(maxLength >= 0 ):
        
        if maxLength == 0 :
            randomNum =  0
        else:
            randomNum =  random.randrange(0,maxLength)
        
        chosenMonth = shitsumon[randomNum]
        shitsumon[randomNum] = shitsumon[maxLength]
        
        
        userInput = input("Japanese For: {} \n".format(chosenMonth[0]))
        
        if(userInput == chosenMonth[1]) :
            print("Correct. Next!" )
            correctAnswers = correctAnswers + 1
        else:
            print("Wrong Answer. \n Correct Answer is: {}".format(chosenMonth[1]))
            
        
        maxLength = maxLength - 1
    
    print("You got {} out of {} correct answers".format(correctAnswers, len(shitsumon)))

