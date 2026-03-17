# D&D NLP Assistant

This project is a small prototype that demonstrates how natural language processing can be used to help beginners understand complex tabletop game rules.

The assistant allows users to ask questions about common Dungeons & Dragons mechanics, and it retrieves a simplified explanation of the most relevant rule. Instead of relying on fixed keywords, the system compares the wording of a user's question to stored rule descriptions to determine the best response.

The goal of the project is to explore how NLP techniques can lower the barrier to entry for complex systems by translating dense rule text into beginner-friendly language.

## Example

D&D NLP Assistant
Ask a rule question (type 'exit' to quit)
> how do I determine turn order?

Initiative: Initiative determines the order of turns during combat.

> how do I resist a spell?
Saving Throw: A saving throw represents an attempt to resist a spell, trap, or harmful effect.

## How It Works

The assistant:
- Loads a small set of D&D rules from a text file
- onverts the rule descriptions and the user’s question into vectors
- Compares their similarity using scikit-learn
- Returns the rule explanation that most closely matches the question

This allows the assistant to respond to different ways a user might phrase the same question.

## Running the Project

Install the required dependency:
pip3 install scikit-learn

Then run the assistant:
python3 assistant.py

## Future Improvements

- Expanding the rule database to include more mechanics from the Dungeons & Dragons rulebook, allowing the assistant to answer a wider range of questions.
- Adding a simple interface (web or desktop) so users can interact with the assistant without needing to run it from the command line.
- Allowing the assistant to provide follow-up explanations or examples to help new players better understand how a rule works during gameplay.
