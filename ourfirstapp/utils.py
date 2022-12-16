def count_vowel(text):
    vowels = ('a', 'e', 'i', 'o', 'u');
    count = 0
    for x in text.lower():
        if x in vowels:
            count = count + 1
    return count


def fakelogincheck(username, password):
    if username == "cdcju" and password == "cdcju":
        return True
    else:
        return False



