import random
from dictCall import dictCall
from spanishDict import categories

dc = dictCall(categories)

def quiz():
    dc.listCategories()
    catChoice = int(input("Select category number: "))
    score = 0

    flag = True
    while flag:
        flag = False
        try:
            catName = dc.key[catChoice - 1]
            words = list(categories[catName].items())
        except:
            flag = True
            catChoice = int(input("Select category number: "))




    print("\nChoose quiz type:")
    print("1. Multiple Choice")
    print("2. Open-Ended")
    mode = eval(input("Enter 1 or 2: "))

    questionAmount = eval(input(f"How many questions? "))

    random.shuffle(words)
    words = words[:questionAmount]

    for span, eng in words:
        if mode == 1:
            multiChoice = [i for j, i in words if i != eng]
            random.shuffle(multiChoice)
            wrongChoice = multiChoice[:3]
            choices = wrongChoice + [eng]
            random.shuffle(choices)

            print(f"\nWhat is the English word for '{span}'? ")
            number = 1
            for k in choices:
                print(str(number) + ". " + k)
                number += 1

            ansChoice = eval(input("Your choice: "))
            if ansChoice and 1 <= ansChoice <= len(choices):
                answer = choices[ansChoice - 1]
            else:
                answer = ''
        elif mode == 2:
            answer = input(f"\nWhat is the English word for '{span}'? ").strip()
        else:
            print(f"Invalid Quiz Type. ")
            return
        if answer.lower() == eng.lower():
            print("\nCorrect!")
            score += 1
        else:
            print(f"\nWrong! The correct answer is {eng}.")

    print(f"\nYou got {questionAmount - score} questions out of {questionAmount} incorrect.\nYour total score is", (score/questionAmount)*100,"%")

def main():
    while True:
        print("\n--- Kadabra Spanish Trainer ---")
        print("1. List categories")
        print("2. Show English words")
        print("3. Show Spanish words")
        print("4. Show translations")
        print("5. Take a quiz")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            dc.listCategories()
        elif choice == "2":
            dc.listCategories()
            num = int(input("Select category number: "))
            dc.listEnglish(num)
        elif choice == "3":
            dc.listCategories()
            num = int(input("Select category number: "))
            dc.listSpanish(num)
        elif choice == "4":
            dc.listCategories()
            num = int(input("Select category number: "))
            dc.listTranslations(num)
        elif choice == "5":
            quiz()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

main()
