import os
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
_IGNORE = ('_IGNORE', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'os')

INSTALLED_APPS = (
    'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dummyuser',
    'social.apps.django_app.default',
    'easy_thumbnails',
    'orgchart',
    'mptt',
    'treeadmin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_DIRS = (
    #os.path.join(PROJECT_PATH, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'deploy', 'media')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'deploy', 'static')

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
)

AUTH_USER_MODEL = 'dummyuser.DummyUser'

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL= True
USE_SOCIAL_AUTH_AS_ADMIN_LOGIN = True
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email']
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

LOGIN_URL = '/login/google-oauth2/'

DEFAULT_FILE_STORAGE = 'website.utils.ASCIIFileSystemStorage'
