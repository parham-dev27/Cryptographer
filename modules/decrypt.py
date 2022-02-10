from base64 import b64decode
from codecs import decode


def decodeBase64(text):
    try:
        text = str(text)
        asciiEncodeText = text.encode('ascii')
        b64 = b64decode(asciiEncodeText)
        decoded = b64.decode('ascii')
        return decoded
    except:
        return False


def decodeHex(text):
    try:
        text = str(text)
        hexadecimal = bytes.fromhex(text)
        decoded = hexadecimal.decode("ascii")
        return decoded
    except:
        return False


def decodeRot13(text):
    try:
        text = str(text)
        decoded = decode(text, "rot13")
        return decoded
    except:
        return False
