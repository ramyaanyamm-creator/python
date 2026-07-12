#Quiz game
questions=("what is your name:",
           "which old are you:",
           "What is your roll num:",
           "Enter your profession:")
options=(("A.Ramya","B.shannu","C.kumar","D.mani"),
         ("A.12","B.19","C.20","D.21"),
         ("A.1","B.2","C.3","D.4"),
         ("A.teacher","B.engineer","C.developer","D.student"))
         
answers=("A","B","A","C")
guesses=[]
score=0
question_num=0
for question in questions:
    print("............................")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("enter your answer:").upper()
    print(guess)
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("correct")
    else:
        print("incorrect")
        question_num+=1