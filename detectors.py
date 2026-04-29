def detect_failures(messages):
    text = " ".join(messages).lower()

    failures = []

    if text.count("agree") >= 2:
        failures.append("Echo Chamber")

    if len(messages) > 8:
        failures.append("Looping")

    if "ignore" in text:
        failures.append("Information Loss")

    return failures