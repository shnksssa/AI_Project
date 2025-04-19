import random

R_ADVICE = "Sure! Never stop learning. Consistency beats intensity every time."
R_EATING = "I don't eat, but if I did, I'd probably snack on data! 😄"

JOKES = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer show up at work late? It had a hard drive!",
    "What do you call 8 hobbits? A hob-byte."
]

def get_joke():
    return random.choice(JOKES)

def unknown():
    responses = [
        "Hmm... I'm not quite sure what you mean. Can you rephrase?",
        "I'm still learning! Mind asking that a different way?",
        "Interesting! Can you tell me a bit more?"
    ]
    return random.choice(responses)
