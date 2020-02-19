from app.token import IntWrapper, IntToken

def int_wrapper_factory(int_str: str):
    int_tokens = [IntToken(char) for char in int_str]
    return IntWrapper(int_tokens)
