from base64 import b64encode
from codecs import encode


def encodeBase64(text):
    try:
        text = str(text)
        asciiEncodeText = text.encode('ascii')
        b64 = b64encode(asciiEncodeText)
        encoded = b64.decode('ascii')
        return encoded
    except:
        return False


def encodeHex(text):
    try:
        text = str(text)
        asciiEncodeText = text.encode('ascii')
        hexadecimal = asciiEncodeText.hex()
        return hexadecimal
    except:
        return False


def encodeRot13(text):
    try:
        text = str(text)
        rot13 = encode(text, 'rot_13')
        return rot13
    except:
        return False
