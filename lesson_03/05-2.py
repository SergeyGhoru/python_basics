import random


def get_jokes(n: int, unique=False):
    """
    Input: number of jokes to return
    Return: list of strings with jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    noun, adverb, adjective, jokes = [], [], [], [] #list(range(4))

    for n_joke in range(n):
        if unique and n <6:
            while True:
                new_noun = nouns[random.randint(0,4)]
                if new_noun not in noun:
                    noun.append(new_noun)
                    break

            while True:
                new_adverb = adverbs[random.randint(0,4)]
                if new_noun not in adverb:
                    adverb.append(new_adverb)
                    break

            while True:
                new_adjective = adjectives[random.randint(0,4)]
                if new_noun not in adjective:
                    adjective.append(new_adjective)
                    break
            new_joke = [noun[n_joke], adverb[n_joke], adjective[n_joke]]
        elif unique and n >= 6:
            return "Error: jokes dictionary size exceeded"
        else:
            new_noun = nouns[random.randint(0, 4)]
            new_adverb = adverbs[random.randint(0, 4)]
            new_adjective = adjectives[random.randint(0, 4)]
            new_joke = [new_noun, new_adverb, new_adjective]

        jokes.append(' '.join(new_joke))
    return jokes

print(get_jokes(5, unique=True))
print(get_jokes(3))
print(get_jokes(6, unique=True))
