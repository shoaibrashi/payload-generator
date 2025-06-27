def add_comments(payload):
    return payload.replace(" ", "/**/")

def case_swap(payload):
    return ''.join([c.upper() if i % 2 else c.lower() for i, c in enumerate(payload)])
