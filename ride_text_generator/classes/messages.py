import random

GREETING = ["Hi", "Hey", "Ya Ali Madad", "YAM"]

WARMTH = ["hope you're doing well", 
        "hope you're having a good day",
        "hope you're having a good week",
        "hope you're staying warm",
        "hope you're doing okay"]

DRIVER_TRANSITION = ["I just wanted to reach out to you about rides for the upcoming rotation",
                    "I just wanted to let you know who you're giving rides to this rotation"]

RIDER_TRANSITION = ["I just wanted to reach out to you about rides for the upcoming rotation",
                    "I just wanted to let you know who you're getting a ride from for this rotation"]

APPRECIATION = ["thank you",
                "thanks",
                "thank you so much",
                "thanks so much",
                "thanks for your help"]

CLOSING = ["if you have any questions, please let me know",
        "if you have any questions, please reach out",
        "let me know if there are any concerns"]

FAREWELL = ["see you soon",
            "see you in khane",
            "take care"]

def get_greeting():
    return random.choice(GREETING)

def get_warmth():
    return random.choice(WARMTH)

def get_driver_transition():
    return random.choice(DRIVER_TRANSITION)

def get_rider_transition():
    return random.choice(RIDER_TRANSITION)

def get_appreciation():
    return random.choice(APPRECIATION)

def get_closing(): 
    return random.choice(CLOSING)

def get_farewell():
    return random.choice(FAREWELL)
