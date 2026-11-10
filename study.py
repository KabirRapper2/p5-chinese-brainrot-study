#!/usr/bin/env python3
"""
P5 Chinese Brainrot Study Tool
100% keyboard only. No trackpad needed.
"""

import random
import sys
import time

try:
    from data import WORDS, CHAR_TYPES, NEAR_SYNONYM, IDIOMS, CONJUNCTIONS, PUNCTUATION
except ImportError:
    print("Error: data.py not found. Make sure both files are in the same folder.")
    sys.exit(1)

# Optional speech
SPEAK = "--speak" in sys.argv
if SPEAK:
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
    except Exception:
        print("Could not load speech. Install with: pip install pyttsx3")
        SPEAK = False

def speak(text):
    if SPEAK:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass

def clear():
    print("\n" * 3)

def wait_enter(msg="Press Enter..."):
    input(f"\n{msg} ")

def quiz_section(name, cards, mode="normal"):
    print(f"\n{'='*40}")
    print(f"  {name}")
    print(f"{'='*40}")
    print("Controls: Enter = show answer | 1 = I knew it | 2 = forgot | s = skip | q = quit\n")

    deck = cards[:]
    random.shuffle(deck)
    wrong = []

    i = 0
    while i < len(deck):
        card = deck[i]
        clear()
        print(f"[{i+1}/{len(deck)}]  {name}\n")

        if mode == "words":
            print(f"Chinese:  {card['zh']}")
            speak(card['zh'])
            wait_enter("Think of the meaning, then press Enter")
            print(f"\n→ {card['en']}")
            print(f"  Hint: {card['hint']}")

        elif mode == "char":
            print(f"Type:  {card['zh']}")
            speak(card['zh'])
            wait_enter("What does this type mean?")
            print(f"\n→ {card['en']}")
            print(f"  {card['hint']}")
            print(f"  Examples: {card['examples']}")

        elif mode == "near":
            print(f"Word:  {card['zh']}")
            speak(card['zh'])
            wait_enter("Is it ✓ (similar) or × (not similar)?")
            print(f"\n→ {card['answer']}   ({card['reason']})")

        elif mode == "idiom":
            print(f"Idiom:  {card['zh']}")
            speak(card['zh'])
            wait_enter("What does it mean?")
            print(f"\n→ {card['en']}")
            print(f"  {card['hint']}")

        elif mode == "conj":
            print(f"Word:  {card['zh']}")
            speak(card['zh'])
            wait_enter("English meaning?")
            print(f"\n→ {card['en']}")
            print(f"  {card['hint']}")

        elif mode == "punct":
            print(f"Mark:  {card['zh']}")
            wait_enter("When do you use it?")
            print(f"\n→ {card['en']}")
            print(f"  {card['hint']}")

        print("\n1 = I knew it    2 = Forgot (show again)    s = skip    q = quit")
        choice = input("> ").strip().lower()

        if choice == "q":
            return
        elif choice == "2":
            wrong.append(card)
            print("Got it. Will show again later.")
            time.sleep(0.6)
        elif choice == "s":
            pass
        # anything else counts as known

        i += 1

    if wrong:
        print(f"\nYou missed {len(wrong)} cards. Doing them again...\n")
        time.sleep(1)
        quiz_section(name + " (retry)", wrong, mode)
    else:
        print(f"\nNice. You finished {name}!")
        time.sleep(1)

def main():
    print("""
╔══════════════════════════════════════╗
║   P5 Chinese Brainrot Study Tool     ║
║   Keyboard only · No trackpad needed ║
╚══════════════════════════════════════╝
""")
    print("Choose a section:\n")
    print("1. Words (詞語)")
    print("2. Character types (造字法)")
    print("3. Near-synonym compounds (近義複合詞)")
    print("4. Idioms (成語)")
    print("5. Conjunctions (連詞)")
    print("6. Punctuation (標點)")
    print("7. Everything (random mix)")
    print("q. Quit\n")

    while True:
        choice = input("Pick (1-7 or q): ").strip().lower()

        if choice == "q":
            print("Good luck tomorrow.")
            break
        elif choice == "1":
            quiz_section("Words 詞語", WORDS, "words")
        elif choice == "2":
            quiz_section("Character Types 造字法", CHAR_TYPES, "char")
        elif choice == "3":
            quiz_section("Near-synonym 近義複合詞", NEAR_SYNONYM, "near")
        elif choice == "4":
            quiz_section("Idioms 成語", IDIOMS, "idiom")
        elif choice == "5":
            quiz_section("Conjunctions 連詞", CONJUNCTIONS, "conj")
        elif choice == "6":
            quiz_section("Punctuation 標點", PUNCTUATION, "punct")
        elif choice == "7":
            # mix everything lightly
            mixed = []
            for w in WORDS:
                mixed.append({"type": "words", "data": w})
            for c in CHAR_TYPES:
                mixed.append({"type": "char", "data": c})
            for n in NEAR_SYNONYM:
                mixed.append({"type": "near", "data": n})
            for i in IDIOMS:
                mixed.append({"type": "idiom", "data": i})
            for c in CONJUNCTIONS:
                mixed.append({"type": "conj", "data": c})
            for p in PUNCTUATION:
                mixed.append({"type": "punct", "data": p})
            random.shuffle(mixed)
            print("\nMixed mode – everything randomly.")
            for item in mixed:
                if item["type"] == "words":
                    quiz_section("Words", [item["data"]], "words")
                elif item["type"] == "char":
                    quiz_section("Char Types", [item["data"]], "char")
                elif item["type"] == "near":
                    quiz_section("Near-synonym", [item["data"]], "near")
                elif item["type"] == "idiom":
                    quiz_section("Idioms", [item["data"]], "idiom")
                elif item["type"] == "conj":
                    quiz_section("Conjunctions", [item["data"]], "conj")
                elif item["type"] == "punct":
                    quiz_section("Punctuation", [item["data"]], "punct")
        else:
            print("Just type 1-7 or q")

if __name__ == "__main__":
    main()
