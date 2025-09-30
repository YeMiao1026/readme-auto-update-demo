#!/usr/bin/env python3
import re, subprocess, datetime

README = "README.md"
START = "<!-- AUTO-UPDATE-START -->"
END   = "<!-- AUTO-UPDATE-END -->"

def get_commits(n=5):
    fmt = "- `%h` %s — (%an, %ad)"
    cmd = ["git", "log", f"-n{n}", "--date=short", f"--pretty=format:{fmt}"]
    return subprocess.check_output(cmd, text=True)

def build_section():
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')
    return f"**Last updated:** {timestamp}\n\n{get_commits()}"

def main():
    text = open(README).read()
    pattern = re.compile(re.escape(START) + ".*?" + re.escape(END), re.S)
    new_block = f"{START}\n{build_section()}\n{END}"
    new_text = pattern.sub(new_block, text)
    if new_text != text:
        open(README, "w").write(new_text)
        print("README updated.")

if __name__ == "__main__":
    main()
