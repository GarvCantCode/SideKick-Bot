import base64


def convert(mode, text):
    if mode == "encode":
        return base64.b64encode(text.encode("utf-8")).decode("ascii")
    
    text = text.strip()
    return base64.b64decode(text, validate=True).decode("utf-8")