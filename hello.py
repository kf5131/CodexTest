"""
A small hello world script with a playful twist.
"""

import random


def main() -> None:
    greetings = [
        "Hello, world!",
        "Hi there, planet Earth!",
        "Greetings, globe-trotter!",
        "Salutations, tiny blue marble!",
    ]
    mascots = ["🚀", "🤖", "🪐", "🌈", "🧠"]

    greeting = random.choice(greetings)
    mascot = random.choice(mascots)

    print(f"{greeting} Here is a fun mascot for you: {mascot}")


if __name__ == "__main__":
    main()
