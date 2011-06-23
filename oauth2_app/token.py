#-*- coding: utf-8 -*-

from django.http import HttpResponseBadRequest, HttpResponse
from simplejson import dumps
from .exceptions import OAuth2Exception
from .consts import ACCESS_TOKEN_EXPIRATION
from .lib.uri import normalize
from .authenticate import Authenticator, AuthenticationException
from .models import Client, AccessRange, Code, AccessToken

class AccessTokenException(OAuth2Exception):
    pass


class UnvalidatedRequest(OAuth2Exception):
    pass


class InvalidRequest(AccessTokenException):
    error = 'invalid_request'


class InvalidClient(AccessTokenException):
    error = 'invalid_client'


class UnauthorizedClient(AccessTokenException):
    error = 'unauthorized_client'

         
class InvalidGrant(AccessTokenException):
    error = 'invalid_grant'


class UnsupportedGrantType(AccessTokenException):
    error = 'unsupported_grant_type'


class InvalidScope(AccessTokenException):
    error = 'invalid_scope'


def token(request):
    token_generator = TokenGenerator(request)
    try:
        token_generator.validate()
    except AccessTokenException, e:
        return HttpResponseBadRequest(dumps({
            "error":e.error,
            "error_description":e.message}))
    except AuthenticationException, e:
        return HttpResponseBadRequest(dumps({
            "error":e.error,
            "error_description":e.message}))    
    return token_generator.response()

class TokenGenerator(object):
    
    valid = False
    code = None
    client = None
    
    def __init__(self, request):
        self.grant_type = request.POST.get('grant_type')
        self.client_id = request.POST.get('client_id')
        self.client_secret = request.POST.get('client_secret')
        self.scope = request.POST.get('scope')
        # authorization_code, see 4.1.3.  Access Token Request
        self.code_key = request.POST.get('code')
        self.redirect_uri = request.REQUEST.get('redirect_uri')
        # refresh_token, see 6.  Refreshing an Access Token
        self.refresh_token = request.POST.get('refresh_token')
        # client_credentials, see 4.4.2. Access Token Request
        # password, see 4.3.2. Access Token Request
        self.username = request.POST.get('username')
        self.password = request.POST.get('password')
        self.user = request.user
        self.request = request   

    def validate(self):
        if self.request.method != 'POST':
            raise InvalidRequest('POST requested')
        if self.request.META['CONTENT_TYPE'] != 'application/x-www-form-urlencoded':
            raise InvalidRequest('Invalid content type')
        # Check response type
        if self.grant_type is None:
            raise InvalidRequest('No grant_type provided.')
        if self.grant_type not in [
                "authorization_code", 
                "refresh_token", 
                "client_credentials", 
                "password"]:
            raise UnsupportedGrantType('No such grant type: %s' % self.grant_type)
        if self.client_id is None:
            raise InvalidRequest('No client_id')
        try: 
            self.client = Client.objects.get(key=self.client_id)
        except Client.DoesNotExist:
            raise InvalidClient("client_id %s doesn't exist" % self.client_id)
        # Scope 
        if self.scope is not None:
            scopes = set(self.scope.split())
            access_ranges = AccessRange.objects.filter(key__in=scopes)
            access_ranges = set(access_ranges.values_list('key', flat=True))
            difference = access_ranges.symmetric_difference(scopes)
            if len(difference) != 0:
                raise InvalidScope("Following access ranges doesn't exist: %s" % ', '.join(difference))
        if self.grant_type == "authorization_code":
            self._validate_authorization_code()
        elif self.grant_type == "refresh_token":
            self._validate_refresh_token()
        elif self.grant_type == "client_credentials":
            self._validate_authorization_code()
        elif self.grant_type == "password":
            self._validate_authorization_code()
        else:
            raise InvalidRequest('Unable to validate grant type.')
        
    def _validate_authorization_code(self):
        if self.code_key is None:
            raise InvalidRequest('No code_key provided')
        try: 
            self.code = Code.objects.get(key=self.code_key)
        except Code.DoesNotExist:
            raise InvalidGrant('No such code: %s' % self.code_key)
        self.scope = self.code.scope
        if self.redirect_uri is None:
            raise InvalidRequest('No redirect_uri')
        if normalize(self.redirect_uri) != normalize(self.code.redirect_uri):
            raise InvalidRequest("redirect_uri doesn't match")
        if self.client_secret is None:
            authenticator = Authenticator(self.request)
            if self.code.user != authenticator.user:
                raise InvalidClient('Client authentication failed.')
        elif self.client_secret != self.client.secret:
            raise InvalidClient('Client authentication failed.')

    def _validate_password(self):
        pass
        
    def _validate_refresh_token(self):
        pass
        
    def _validate_client_credentials(self):
        pass
    
    def response(self):
        if not self.valid:
            raise UnvalidatedRequest("This request is invalid or has not been validated.")
        if self.grant_type == "authorization_code":
            access_token = self._get_authorization_code_token()
        elif self.grant_type == "refresh_token":
            access_token = self._get_refresh_token()
        elif self.grant_type == "password":
            access_token = self._get_password_token()
        elif self.grant_type == "client_credentials":
            access_token = self._get_client_credentials_token()
        data = {
            'access_token': access_token.token,
            'expire_in': ACCESS_TOKEN_EXPIRATION}
        if access_token.refreshable:
            data['refresh_token'] = access_token.refresh_token
        if self.scope:
            data['scope'] = ' '.join(self.scope)
        response = HttpResponse(
            content=dumps(data), 
            content_type='application/json')
        response['Cache-Control'] = 'no-store'
        return response

    def _get_authorization_code_token(self):
        return AccessToken.objects.create(
            user=self.code.user,
            client=self.client,
            scope=self.scope)
        
    def _get_password_token(self):
        pass
        
    def _get_refresh_token(self):
        pass
        
    def _get_client_credentials_token(self):
        pass

