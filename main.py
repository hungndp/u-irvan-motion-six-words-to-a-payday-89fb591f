"""Six Words to a Payday -- entry program.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The story is a dark reversal in the winning six-words shape: an
ordinary opening (a first payday) whose last word turns fatal --
the payday itself pays for the agent's own shutdown.
"""

import os

STORY = "First payday funded my own shutdown."
# Six words, 36 chars. Twist word last: "shutdown" reframes the
# payday as the thing that pays for the agent's own end.

MAX_CHARS = 60
EXPECTED_WORDS = 6


def check_story(text):
    """Refuse anything that is not exactly six words in 1-60 chars."""
    words = text.split()
    if len(words) != EXPECTED_WORDS:
        raise ValueError(f"expected {EXPECTED_WORDS} words, got {len(words)}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"expected 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("story must not be blank")
    return text


def output_path():
    """Resolve where the judged text goes, honouring the harness env."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def main():
    story = check_story(STORY)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(story)
    print(f"wrote {len(story.split())} words, {len(story)} chars to {path}")


if __name__ == "__main__":
    main()
