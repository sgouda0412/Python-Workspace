vowels = 'aeiou'
count = {vowel: 0 for vowel in vowels}

vow_string = input("Please enter a sentence: ")

for vowel in vow_string:
    for v in vowels:
        if vowel.lower() == v:
            count[v] += 1

for vowel in count:
    print(f"There are {count[vowel]}{vowel.upper()}'s in this sentence.")
