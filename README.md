# P5 Chinese Brainrot Study Tool

Keyboard-only Chinese study tool for Primary 5 exam revision.
Made for brainrotted brains and laptops with **no trackpad**.

## What it covers
- 詞語 (Words)
- 造字法 (Character types)
- 近義複合詞 (Near-synonym compounds)
- 成語 (Idioms)
- 連詞 (Conjunctions)
- 標點符號 (Punctuation)

## How to run (super simple)

1. Make sure you have Python 3 installed
2. Open terminal in this folder
3. Run:

```bash
python study.py
```

## Controls (100% keyboard)
- `Enter` → show answer / next
- `1` → I got it right
- `2` → I got it wrong (shows again later)
- `q` → quit
- `s` → skip
- `r` → restart current section

No mouse or trackpad needed.

## Listening mode
The script can also speak the cards if you have `pyttsx3` installed:

```bash
pip install pyttsx3
python study.py --speak
```

## Made for last-minute revision
Just run it, smash Enter, and say the answers out loud.
