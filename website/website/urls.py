from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.utils.functional import curry
from social.apps.django_app.views import auth as social_auth

# replace admin login with google social auth
admin.autodiscover()
admin.site.login = curry(social_auth, backend='google-oauth2')

from django.http import HttpResponse
def foo(request):
    return HttpResponse(unicode(request.user) + ' ' + unicode(request.user.is_staff))

urlpatterns = patterns('',
    url('^$', foo),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
