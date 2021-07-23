def notify(email_to, author_name):
    print('-------------- notify: {}'.format(email_to))
    email_send(email_to, author_name)
    telegram_notify(email_to)


def email_send(email_to, author_name):
    from django.core.mail import send_mail

    send_mail(
        'Bread Blog',
        'You have subscribed on Author: {}'.format(author_name),
        'romanitalian.net@gmail.com',
        [email_to],
        fail_silently=False,
    )


def telegram_notify(email_to):
    pass
