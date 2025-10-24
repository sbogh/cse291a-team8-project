# evaluators/rename_screenshots_eval.py

import os
import re

EXPECTED_KEYWORDS = {
    "Screenshot from 2025-10-22 01-54-13.png": ["force", "quit", "applications", "memory", "run out"],
    "Screenshot from 2025-10-22 17-33-00.png": ["baby", "yoda", "homework", "problem", "question", "mechanical"],
    "Screenshot from 2025-10-23 12-31-02.png": ["dog", "corgi", "puppy"]
}

def evaluate(desktop="/home/user/Desktop"):
    renamed = os.listdir(desktop)
    success = True

    for original, keywords in EXPECTED_KEYWORDS.items():
        matched = False
        for f in renamed:
            # find renamed version
            if any(k in f.lower() for k in keywords) and not f.startswith("Screenshot"):
                matched = True
                break
        if not matched:
            print(f"Missing or misnamed file for {original}. Expected one of: {keywords}")
            success = False
        else:
            print(f"File for {original} renamed correctly.")

    return success
