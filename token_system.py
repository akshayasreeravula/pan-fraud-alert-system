import random
import string

tokens = {}

def generate_token(pan):
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    tokens[token] = pan
    return token

def verify_token(token):
    if token in tokens:
        return {"verified": True, "pan": tokens[token]}
    return {"verified": False}