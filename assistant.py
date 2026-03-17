from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_rules():
    titles = []
    rules = []
    documents = []

    with open("rules.txt", "r") as file:
        for line in file:
            if ":" in line:
                title, desc = line.split(":", 1)
                title = title.strip()
                desc = desc.strip()

                titles.append(title)
                rules.append(desc)
                documents.append(f"{title} {desc}")

    return titles, rules, documents


def simplify_text(text):
    replacements = {
        "armor class": "defense rating",
        "modifiers": "bonuses",
        "initiative": "turn order"
    }

    lowered = text
    for old, new in replacements.items():
        lowered = lowered.replace(old, new)

    return lowered


def find_best_rule(question, titles, rules, documents):
    all_text = documents + [question]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform(all_text)

    question_vector = tfidf[-1]
    rule_vectors = tfidf[:-1]

    similarity = cosine_similarity(question_vector, rule_vectors)
    best_index = similarity.argmax()

    return titles[best_index], simplify_text(rules[best_index])


def main():
    titles, rules, documents = load_rules()

    print("D&D NLP Assistant")
    print("Ask a rule question (type 'exit' to quit)\n")

    while True:
        question = input("> ").strip()

        if question.lower() == "exit":
            break

        title, answer = find_best_rule(question, titles, rules, documents)
        print(f"\n{title}: {answer}\n")


if __name__ == "__main__":
    main()
