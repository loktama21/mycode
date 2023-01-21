#!/usr/bin/env python3
import requests
import numpy as np

URL= "https://opentdb.com/api.php?amount=5&category=12&difficulty=easy&type=multiple"

def question_and_answer():
    data= requests.get(URL).json()
    results_array= data.get("results")
    total = 0
    for result in results_array:
        total += 1

        answers_array = []
        answers_array.append(result['correct_answer'])
        answers_array.append(result['incorrect_answers'][0])
        answers_array.append(result['incorrect_answers'][1])
        answers_array.append(result['incorrect_answers'][2])

        np.random.shuffle(answers_array)

        question_answer = {
            "question" : f"{result['question']}",
            'A' : answers_array[0],
            'B' : answers_array[1],
            'C' : answers_array[2],
            'D' : answers_array[3],
            "answer" : f"{result['correct_answer']}"
        }

        return question_answer
