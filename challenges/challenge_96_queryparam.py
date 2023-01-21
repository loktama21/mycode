import requests

url = "https://opentdb.com/api.php?amount=5&category=10&difficulty=easy&type=multiple"

def main():
    data = requests.get(url).json()
    for q in data["results"]:
        print(q.get("question"))
        correct_ans = q.get("correct_answer")
        incorrect_ans = q.get("incorrect_answers")
        incorrect_ans.append(correct_ans)
        print(incorrect_ans)

        user_ans = input("Answer: ")
        if user_ans == correct_ans:
            print("Good job! That is a correct answer\n")
        elif user_ans == "exit":
            break
        else:
            print("Incorrect answer. Try again!\n")

    play_again = input('Do you want to play again? "Y" or "N"\n> ')
    if play_again == "y" or play_again == "Y":
        print()
        main()
    else:
        print("Thanks for playing. Bye!")
        print()

if __name__ == "__main__":
    main()
