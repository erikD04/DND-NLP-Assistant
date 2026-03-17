import re

def load_rules():
    rules = {}
    with open("rules.txt", "r") as file:
        for line in file:
            if ":" in line:
                title, description = line.split(":", 1)
                rules[title.strip().lower()] = description.strip()
    return rules


def simplify_text(text):
    # Very simple "NLP" simplification
    text = re.sub(r"armor class", "defense rating", text)
    text = re.sub(r"modifiers", "bonuses", text)
    text = re.sub(r"initiative", "turn order", text)
    return text


def ask_question(question, rules):
    question = question.lower()

    for rule in rules:
        if rule in question:
            explanation = rules[rule]
            return simplify_text(explanation)

    return "I couldn't find that rule yet. Try asking about attack, saving throw, or initiative."


def main():
    print("D&D Rule Assistant")
    print("Ask a question about a rule (type 'exit' to quit).\n")

    rules = load_rules()

    while True:
        question = input("> ")

        if question.lower() == "exit":
            break

        answer = ask_question(question, rules)
        print(answer)
        print()


if __name__ == "__main__":
    main()
