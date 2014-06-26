import random
import re

WORDS = ["HELLO", "HOW", "ARE", "YOU"]

def handle(text, mic, profile):
    """
        Responds to user-input, typically speech text, with general chit chat

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
    """

    mic.say("Hello")

def isValid(text):
    """
        Returns True if the input is related to general chit chat

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bHello\b', text, re.IGNORECASE))
