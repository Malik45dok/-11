def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if recipient == sender:
        print("Невозможно отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправленос адреса", sender, "на адрес", recipient)
    elif("@" and (".com" or ".ru" or ".net")) not in recipient and ("@" and (".com" or ".ru" or ".net")) not in sender:
        print("Невозможно отправить письмо с указанного адреса", sender, "на адрес", recipient)
    else:
        print("Нестандартный отправитель! Письмо отправлено с адреса", sender, "на адрес", recipient)
send_email('Это сообщение для проверки связи', 'komarik315@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте ошибки', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
