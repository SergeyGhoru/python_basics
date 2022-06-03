def num_translate_adv(s: str):
    """
    Input: string with number in English from 'zero' to 'ten' (capitalized or lowercase) in text
    Return: sting with number in Russian from 'ноль' to 'десять' (capitalized or lowercase) in text
    """
    nums_dict = {
        "zero"  : "ноль",
        "one"   : "один",
        "two"   : "два",
        "three" : "три",
        "four"  : "четыре",
        "five"  : "пять",
        "six"   : "шесть",
        "seven" : "семь",
        "eight" : "восемь",
        "nine"  : "девять",
        "ten"   : "десять",
    }
    search = str(s)
    res = nums_dict.get(search.lower())
    if res and search[0].isupper():
        return nums_dict.get(search.lower()).capitalize()
    elif res and not search[0].isupper():
        return nums_dict.get(search.lower())


print(num_translate_adv("Zero"))
print(num_translate_adv("One"))
print(num_translate_adv("two"))
print(num_translate_adv("nine"))
print(num_translate_adv("Ten"))
print(num_translate_adv("tententen"))
print(num_translate_adv(123))
