import random

def build_char_markov_chain(text, order=3):
    markov_chain = {}

    for i in range(len(text) - order):
        key = text[i:i+order]
        next_char = text[i + order]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_char)

    return markov_chain

def generate_char_text(chain, length=500, order=3):
    start = random.choice(list(chain.keys()))
    result = start

    for _ in range(length - order):
        current_state = result[-order:]
        next_chars = chain.get(current_state)

        if not next_chars:
            break

        next_char = random.choice(next_chars)
        result += next_char

    return result

def main():
    try:
        with open("input.txt", "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("❌ Error: input.txt not found.")
        return

    order = 3  # You can change this to 4 for even smoother text
    chain = build_char_markov_chain(text, order=order)
    generated_text = generate_char_text(chain, length=500, order=order)

    print("\n📜 Generated Text:\n")
    print(generated_text)

if __name__ == "__main__":
    main()
