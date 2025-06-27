import urllib.parse, base64

def encode_payload(payload, method):
    if method == "base64":
        return base64.b64encode(payload.encode()).decode()
    elif method == "url":
        return urllib.parse.quote(payload)
    elif method == "hex":
        return ''.join(hex(ord(c))[2:] for c in payload)
    return payload
