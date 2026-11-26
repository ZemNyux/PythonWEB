from .accounts_memory import account_for_username

def site_account(request):
    username = request.session.get('site_username')
    account = account_for_username(username) if username else None
    return {'site_account': account}
