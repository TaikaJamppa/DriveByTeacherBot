"""
DriveByTeacherBot
Early development build.
"""

SUMMON_COMMANDS = [
    "!spellcheck",
    "!teacher",
    "!opettaja",
]


def is_summoned(text):
    text = text.lower().strip()

    for command in SUMMON_COMMANDS:
        if command in text:
            return True

    return False


def main():
    test_comment = "!spellcheck"

    if is_summoned(test_comment):
        print("DriveByTeacher summoned! 😏")
    else:
        print("No summon detected.")


if __name__ == "__main__":
    main()
