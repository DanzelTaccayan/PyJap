import quiz
import quizcomponent

def main():
    test = quiz.Quiz(quizcomponent.quizSetSelections, quizcomponent.quizQuestion)
    test.startQuiz()

if __name__ == "__main__":
    main()