from datetime import *
def isTokenValid(loginOAuthData):
    return loginOAuthData["expiresAt"]>datetime.now().timestamp()