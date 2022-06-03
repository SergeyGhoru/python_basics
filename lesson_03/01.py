def num_translate(s: str):
    """
    Input: string with number in English from 'zero' to 'ten' (lowercase) in text
    Return: sting with number in Russian from 'ноль' to 'десять' (lowercase) in text
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
    return nums_dict.get(s)

print(num_translate("zero"))
print(num_translate("one"))
print(num_translate("two"))
print(num_translate("nine"))
print(num_translate("ten"))
print(num_translate("tententen"))
print(num_translate(123))
