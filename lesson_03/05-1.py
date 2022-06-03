import random


def get_jokes(n: int):
    """
    Input: number of jokes to return
    Return: list of strings with jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []

    for n_joke in range(n):
        new_noun = nouns[random.randint(0,4)]
        new_adverb = adverbs[random.randint(0,4)]
        new_adjective = adjectives[random.randint(0,4)]

        new_joke = [new_noun, new_adverb, new_adjective]
        jokes.append(' '.join(new_joke))
    return jokes


print(get_jokes(9))
