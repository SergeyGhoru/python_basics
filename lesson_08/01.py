import re


def email_parse(mail: str):
    RE_EMAIL = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+')
    username, domain = RE_EMAIL.findall(mail)[0].split('@')
    return {'username': username, 'domain': domain}


print(email_parse('someone@geekbrains.ru'))
print(email_parse('test@gmail.com'))
