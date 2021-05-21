from difflib import SequenceMatcher

with open('f1.txt') as f1, open('f2.txt') as f2:
    f1_data = f1.read()
    f2_data = f2.read()
    similarity = SequenceMatcher(None, f1_data, f2_data).ratio()
    print(f"The contents are {similarity*100}% common.")
