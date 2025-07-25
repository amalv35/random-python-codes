def ask_yes_no(question):
    
    ans = input(question + " (yes/no): ").strip().lower()
    return ans == "yes"

def run_quiz(questions):
    score = 0
    for prompt, correct in questions:
        ans = input(prompt + " ").strip().lower()
        if ans == correct.lower():
            print("Good boi!")
            score += 1
        else:
            print(f"you got it wrong boi— the answer was: {correct}")
    return score

def main():
    print("Hellllooo, welcome to my quiz game sakaaaaa!")
    if not ask_yes_no("Do you wanna play, boi?"):
        print("see ya next time boi")
        return

    qs = [
        ("What does SEO stand for?", "Search Engine Optimization"),
        ("What does API stand for?", "Application Programming Interface"),
        ("What does CRUD stand for?", "Create Read Update Delete"),
        ("What does ORM stand for?", "Object Relational Mapping"),
        ("What does JWT stand for?", "JSON Web Token"),
        ("What does REST stand for?", "Representational State Transfer"),
        ("What does SQL stand for?", "Structured Query Language"),
    ]

    print("\nLet’s go!\n")
    score = run_quiz(qs)
    total = len(qs)

    print("\n" + ("-" * 30))
    print(f"You got {score} out of {total} correct.")
    if score > total * 0.6:
        print("Well done, boi!")
    else:
        print("your weakness diasgusts me")

if __name__ == "__main__":
    main()
