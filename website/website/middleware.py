from django.shortcuts import render
from social.exceptions import AuthForbidden

class ForbiddenAuthMiddleware(object):
    def process_exception(self, request, exception):
        if not isinstance(exception, AuthForbidden):
            return
        
        return render(request, '403.html', status=403)
