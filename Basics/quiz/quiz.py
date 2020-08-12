import random
import datetime

from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        #Generate 10 random question with numbers 1 to 10
        question_types = (Add, Multiply)

        #add these questions into self.questions
        ##### e.g. question_types[0](1, 5)
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)

            self.questions.append(question)

    
    def take_quiz(self):
        
        # log the start time
        self.start_time = datetime.datetime.now()

        # ask all of the questions
        for question in self.questions:
            # log if they got the question right
            self.answers.append(self.ask(question))
        
        else:
            # log the end time
            self.end_time = datetime.datetime.now()
        
        
        
        # show a summary
        return self.summary()


    def total_correct(self):
        
        #return the total # of correct answers
        total = 0
        for answer in self.answers:
            if answer[0] == True:
                total += 1
        
        return total

    
    def ask(self, question):
        
        correct = False

        # log the start time
        question_start = datetime.datetime.now()

        # capture/get the answer
        answer = input(question.text + ' = ')

        # check the answer
        if answer == str(question.answer):
            # if the answer's right, send back true
                # otherwise, send back false
            correct = True

        # log the end time
        question_end = datetime.datetime.now()    

        # send back the elapsed time, too
        return correct, question_end - question_start


    
    def summary(self):
        # how many you got right and the total # of a quiz --> 5/10
        print("you got {} out of {} right".format(self.total_correct(), len(self.questions)))
        
        # print the total time for the quiz --> 50 seconds
        print("it took you {} seconds total.".format(
                (self.end_time - self.start_time).seconds
            ))

quiz = Quiz()
quiz.take_quiz()

# use set for repeated questions
# takes a number of questions to generate
# Make sure the user can specify the range they want the numbers to come from
# Add in some furthur stats that tell you how long it took to answer each question
