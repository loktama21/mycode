#!/usr/bin/env python3
import requests

url = "https://opentdb.com/api.php?amount=3&category=10&difficulty=easy&type=multiple"

def main():
    data = requests.get(url).json()
    for q in data["results"]:
        print(q.get("question"))
        print(q.get("correct_answer"))

if __name__ == "__main__":
    main()
