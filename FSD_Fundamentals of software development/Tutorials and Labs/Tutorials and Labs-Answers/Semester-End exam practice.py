def createQuiz():
    quiz = []
    quizQuestions = input("Enter the question")
    quiz.append(quizQuestions)
    option_a = input("Enter first answer")
    quiz.append(option_a)
    option_b = input("Enter second answer")
    quiz.append(option_b)
    option_c = input("Enter third answer")
    quiz.append(option_c)
    option_d = input("Enter fourth answer")
    quiz.append(option_d)
    return quiz

def saveQuiz():
    fileHandler = open('quiz.txt','w')
    quiz_call = str(createQuiz())
    fileHandler.write(quiz_call)
    fileHandler.close
    
def takeQuiz():
    fileHandler = open('quiz.txt')
    for line in fileHandler:
        print("\n\t*** "+ line + " ***")
    fileHandler.close()

takeQuiz()
