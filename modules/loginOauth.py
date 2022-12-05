from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


def getSecretToken(clientId,clientSecret,redirect_uri,authorization_base_url,token_url,scope):
    spotify = OAuth2Session(clientId, scope=scope, redirect_uri=redirect_uri)

    authorization_url, state = spotify.authorization_url(authorization_base_url)
    print('Please go here and authorize: ', authorization_url)

    redirect_response = input('\n\nPaste the full redirect URL here: ')

    auth = HTTPBasicAuth(clientId, clientSecret)

    data = spotify.fetch_token(token_url, auth=auth,authorization_response=redirect_response)
    resultAuth = {
        "accessToken":data["access_token"],
        "refreshToken":data["refresh_token"],
        "expiresAt":data["expires_at"],
        "scope":data["scope"]
    }
    return resultAuth


