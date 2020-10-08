import random

            


minutesOfAnHourReference = {}

for minute in range(11, 61):
    pass



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

quiz = Quiz(quizSetSelections, quizQuestion)
quiz.startQuiz()