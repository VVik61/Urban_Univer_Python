# создаём функцию send_email
def send_email(message, recipient, sender = "univerity.help@gmail.com"):
    find_ok = '@' in recipient and '@' in sender
    # проверка заканчиваются ли адреса на '.com', '.ru', '.net'
    variants = ('.com', '.ru', '.net')
    domen_ok = recipient.endswith(variants) and sender.endswith(variants)
    # проверка совпадают ли адреса отправителя и получателя
    odinadr_ok = recipient != sender
    # проверка совпадает ли адрес отправителя с адресом по умолчанию
    sender_ok = sender == "univerity.help@gmail.com"
    if find_ok and domen_ok and odinadr_ok and sender_ok:
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif not odinadr_ok:
        print("Нельзя отправить письмо самому себе!")
    elif not domen_ok:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not sender_ok:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
