import sys

class Quiz:
    
    def __init__(self, quizSetSelection, quizFunction):
        self.quizSetSelection = quizSetSelection
        self.quizFunction = quizFunction
    
    def checkQuizSet(self):
        selections =  ""
        questionType = list(self.quizSetSelection.keys())
        
        for i in range(len(questionType)):
            selections = selections + "Input {} for {} \n".format(i,questionType[i])
        
        choice = input("Choose the set of question to be asked.\n{}Enter chosen input: ".format(selections))
        
        try:
            return self.quizSetSelection[questionType[int(choice)]]
             
        except:
            return False
    
    def startQuiz(self):
        mainQuiz = self.checkQuizSet()
        if(mainQuiz == False):
            sys.exit("Choice is not in the list of quiz selection. Exiting...")
        self.quizFunction(mainQuiz)

