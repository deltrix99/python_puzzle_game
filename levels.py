# holds all functions for each individual level
import random


# for testing purposes ONLY
def main():
    n_raw = input("Enter the level number you want to test: ")
    
    try:
        n = int(n_raw)
        level_selected(n)
    
    except ValueError:
        print(f"{n_raw} is not a valid level number. Please enter a number between 1 and 10.")


# level_selected function: selects the level based on the input number
# n: the level number to select
def level_selected(n):
    
    # selects level 1
    if n == 1:
        
        print("You are on Level 1: Complicated Math Puzzles that I hate.")
        print("I have chosen the worst topic for you: math, and used the parts I don't enjoy.\n")
        
        level1_questions()
    
    # selects level 2
    elif n == 2:

        print("You are on Level 2: arras.io Questions that most people don't know.")
        print("I have chosen another topic for you: arras.io, a simple browser game based off of diep.io.\n")
        
        level2_questions()

    # selects level 3
    elif n == 3:
        print("You are on Level 3: choose the better quote based off of common sense.")
        print("The next topic will be about comparing quotes in my opinion, so choose wisely.\n")
        
        level3_questions()
    
    # selects level 4

    # if the level is not implemented
    else:
        
        print(f"Level {n} is unfortunately not implemented yet. Please try another level (1-10).")
        return


# level 1 questions: a set of math-related questions
def level1_questions():
    
    # level 1: question1: asks about contrapositive statements
    def level1_question1():
        
        for attempt in range(2):
            answer = input("What is type of conditional statement is the following: 'If it does not happen, then it does not exist'? ").lower().strip()
            
            if answer == "contrapositive":
                print("How did you know that? I hate the existence of this.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("I respect you for not knowing this. It is a contrapositive statement, which is the goofiest type of conditional statement.\n")
        
        return False

    # level 1: question2: asks about the derivative of sec(x)
    def level1_question2():
        
        for attempt in range(2):
            answer = input("What is the derivative of sec(x)? ").lower().strip()
            
            if answer == ["sec(x)tan(x)", "sin(x)/cos^2(x)", "sin(x) / cos^2(x)"]:
                print("You are correct! Personally, I will need to practice memorizing this.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("Incorrect! The derivative of sec(x) is sec(x)tan(x).\n")
        
        return False

    # level 1: question3: asks about the integral of 1/x
    def level1_question3():
        
        for attempt in range(2):
            answer = input("What is the integral of 1/x? ").lower().strip()
            
            if answer == ["ln|x| + C", "ln|x|+C"]:
                print("You are correct! This integral is one of the few I will actually remember easily, but you got it right somehow.\n")
                return True
            
            elif answer == ["ln|x| + c", "ln|x|+c"]:
                print("Close, but remember to capitalize the 'C' for the constant of integration because I am feeling nitpicky.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("Incorrect! The integral of 1/x is ln|x| + C.\n")
        
        return False

    # level 1: question4: asks about the limit of (sin(x)/x) as x approaches 0
    def level1_question4():
        
        for attempt in range(2):
            answer = input("What is the limit of (sin(x)/x) as x approaches 0? ").lower().strip()
            
            if answer == "1":
                print("Correct! This limit is fundamental in calculus.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("Incorrect! The limit of (sin(x)/x) as x approaches 0 is 1.\n")
        
        return False

    # level 1: question5: asks about the Taylor series expansion of e^x at x=0
    def level1_question5():
        
        for attempt in range(2):
            
            answer = input("What is the Taylor series expansion of e^x at x=0 (write as many terms as you can)? ").replace(" ", "").lower()
            terms = ["1", "+x", "+x^2/2!", "+x^3/3!", "+x^4/4!", "+x^5/5!", "+x^6/6!"]
            correct = True
            temp_answer = answer
            
            for term in terms:
                
                if term in temp_answer:
                    idx = temp_answer.index(term) + len(term)
                    temp_answer = temp_answer[idx:]
                
                else:
                    correct = False
                    break
            
            if correct:
                print("Correct! You either are a nerd or you just searched it up.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("It's fine if you don't know this. The Taylor series expansion of e^x at x=0 is 1 + x + x^2/2! + x^3/3! ...\n")
        
        return False

    
    # lists all of the questions for level 1
    all_questions_1 = [level1_question1, level1_question2, level1_question3, level1_question4, level1_question5]
    random.shuffle(all_questions_1)
    for question in all_questions_1:
        question()



# level 2 questions: a set of arras.io-related questions
def level2_questions():
    
    # level 2: question1: asks about the current developer of arras.io
    def level2_question1():
        
        for attempt in range(2):
            answer = input("What is the name of the current mediocre developer who created arras.io? ").lower().strip()
            
            if answer == ["damocles", "damo"]:
                print("Correct! arras.io is currently and unfortunately being updated by damocles.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("The correct answer is 'damocles'.")

        return False
    
    # level 2: question2: asks about the maximum skill points in arras.io
    def level2_question2():
        
        for attempt in range(2):
            print("Provide your answers in the format 'x,y,z' where x is normal, y is growth, and z is sandbox. ")
            answer = input("What is the max amount of skill points provided in the respective gamemodes: normal, growth, sandbox?").lower().strip()

            if answer == ["42,78,180", "42, 78, 180", "42 78 180", "42,78,inf", "42, 78, inf", "42 78 inf"]:
                print("Correct! The max skill points in normal is 42, growth is 78, and sandbox is 180.")
                print("Or infinite if you are in sandbox mode because of some dumb technicalities.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("The correct answer is '42,78,180' or '42,78,inf'\n")

            return False


    # level 2: question3: asks about the doppleganger tank
    def level2_question3():

        for attempt in range(2):
            answer = input("What is the name of the tank that I helped participate in introducing (only true friends know)? ").lower().strip()
            
            if answer == "doppleganger":
                print("Correct! The doppleganger tank is a tank that I indirectly suggested.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("The correct answer is 'doppleganger'. It is a duplicate option for the normal 'ganger'.\n")
        
        return False
    
    # level 2: question4: asks about the best tanks in Arms
    def level2_question4():

        for attempt in range(2):
            answer = input("What is one of the best tanks in Arms Race (non-growth)? ").lower().strip()

            if answer == "Headman":
                print("Correct! Headman is one of the best tabnks because of its high damage drones.\n")
                return True
            
            elif answer == "Spectre":
                print("Correct! Spectre is one of the best because of its powerful drones and auto-turrets.\n")
                return True

            elif answer == "Thrasher":
                print("Correct! Thrasher is one of the best because of its high versatility in many situations.\n")
                return True

            elif answer == "Captrapper":
                print("Correct! Captrapper is one of the best because of its strong spawner drones and defense.\n")
                return True

            elif answer == "Toppler":
                print("Correct! Toppler is one of the best because of its high damage and reload for farming.\n")
                return True

            else:
                if attempt == 0:
                    print("Try again!")
                
                else:
                    print("The correct answers are: 'Headman', 'Spectre', 'Thrasher', 'Captrapper', or 'Toppler'.\n")

            return False

    # level 2: question5: asks about the arras.io game 
    def level2_question5():
        
        for attempt in range(2):
            print("I need an honest opinion on this one. It's not a controversial question, but I need to know.")
            answer = input("Do you think arras.io is a good game? (yes/no): ").lower().strip()

            if answer == "yes":
                print("I half-heartedly appreciate your support for arras.io even though you've probably never played it.\n")
                return True
            
            elif answer == "no":
                print("You should consider actually playing the game and tell me what you think.\n")
                return True
            
            else:
                if attempt == 0:
                    print("Try again with yes/no!")
                
                else:
                    print("No way you couldn't provide a yes/no answer for this.\n")

        return False

    # lists all of the questions for level 1
    all_questions_2 = [level2_question1, level2_question2, level2_question3, level2_question4, level2_question5]
    random.shuffle(all_questions_2)
    for question in all_questions_2:
        question()



# level 3 questions: a set of quote-related questions
def level3_questions():

    # level 3: question1: asks about the better quote about work and happiness
    def level3_question1():
        
        print("Which quote is better: ")
        print("a: 'The only way to do great work is to love what you do.'")
        print("b: 'Success is not the key to happiness. Happiness is the key to success.'")
        answer = input("Please enter 'a' or 'b': ").lower().strip()

        if answer == "a":
            print("Correct! This quote emphasizes passion in work over just being happy with what you do.\n")
            return True
            
        else:
            print("Happiness is not a permanent way of life, find what you truly love doing and stick with it'\n")
        
        return False

    
    def level3_question2():
        
        print("Which quote is better: ")
        print("a: ")
        print("b: ")
        answer = input("Please enter 'a' or 'b': ").lower().strip()

        if answer == "a":
            print("\n")
            return True
            
        else:
            print("\n")
        
        return False




# main function: for testing purposes
if __name__ == "__main__":
    main()