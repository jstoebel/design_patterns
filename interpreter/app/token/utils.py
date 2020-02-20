# from app.token import Token, IntWrapper, IntToken
import app.token as token

class IllegalTokenError(Exception):
    pass

def token_factory(char: str) -> token.Token:
    if char.isdigit():
        return token.IntToken(char)
    elif char == '+':
        return token.AddToken()
    elif char == '-':
        return token.SubtractToken()
    elif char == '*':
        return token.MultiplyToken()
    elif char == '/':
        return token.DivideToken()
    elif char == ' ':
        return token.SpaceToken()
    else:
        raise IllegalTokenError

def int_wrapper_factory(int_str: str):
    int_tokens = [token.IntToken(char) for char in int_str]
    return token.IntWrapper(int_tokens)
