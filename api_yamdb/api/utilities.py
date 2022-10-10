from django.core.mail import send_mail


def send_token_email(username, access_code, to_email, created):
    if created:
        title_email = 'YAMDB access code.'
    else:
        title_email = 'YAMDB access code has been renewed.'
    from_email = 'admin@yamdb.com'
    text = (
        f'Hello, please use your username: {username} '
        f'and access code: {access_code} to \n'
        f'get the access to the site via the link /api/v1/auth/token/'
    )
    send_mail(title_email, text, from_email, [to_email], fail_silently=False)
