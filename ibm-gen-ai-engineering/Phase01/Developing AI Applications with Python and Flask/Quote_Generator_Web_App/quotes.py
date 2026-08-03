import random

quotes = [
    "The best way to predict the future is to create it.",
    "First solve the problem, then write the code.",
    "Programs must be written for people to read.",
    "Experience is the name everyone gives to their mistakes.",
    "Code is like humor. When you have to explain it, it’s bad."
]

def get_random_quote():
    return random.choice(quotes)