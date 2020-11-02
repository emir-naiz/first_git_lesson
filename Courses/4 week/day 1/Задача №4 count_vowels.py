def count_vowels(txt):
    vowels = ['a','e','o','i','u']
    count = 0
    for letter in txt:
        if letter in vowels:
            count += 1
    return count
print(count_vowels('Celebration'))