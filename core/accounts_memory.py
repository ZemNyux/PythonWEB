from threading import RLock

from django.contrib.auth.hashers import check_password, make_password


_accounts_by_username = {}
_username_by_email = {}
_accounts_lock = RLock()


def username_exists(username):
    with _accounts_lock:
        return username.casefold() in _accounts_by_username


def email_exists(email):
    with _accounts_lock:
        return email.casefold() in _username_by_email


def create_account(username, email, raw_password):
    username_key = username.casefold()
    email_key = email.casefold()
    with _accounts_lock:
        if username_key in _accounts_by_username:
            raise ValueError('Цей логін уже використовується.')
        if email_key in _username_by_email:
            raise ValueError('Ця email-адреса вже зареєстрована.')
        account = {
            'username': username,
            'email': email,
            'password_hash': make_password(raw_password),
        }
        _accounts_by_username[username_key] = account
        _username_by_email[email_key] = username_key
    return account


def authenticate_account(username, raw_password):
    with _accounts_lock:
        account = _accounts_by_username.get(username.casefold())
        if not account or not check_password(raw_password, account['password_hash']):
            return None
        return {'username': account['username'], 'email': account['email']}


def account_for_username(username):
    with _accounts_lock:
        account = _accounts_by_username.get(username.casefold())
        if not account:
            return None
        return {'username': account['username'], 'email': account['email']}
