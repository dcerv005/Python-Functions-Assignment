#Question 4 
#Task 1
question_list= ["What year is it? ", "What day of the week is it today? ", "What is 1 plus 2 "]
answer_list=['2024', 'sunday', '3']

def quiz_game():#Task 2
    correct= 0
    for question in question_list:
        user_input = input(f"{question}").lower()
        if user_input == answer_list[question_list.index(question)]:
            correct += 1
        else:
            print("Answer incorrect!")
    print(f"You got {correct}/{len(question_list)} correct!")#Task 3

quiz_game()

