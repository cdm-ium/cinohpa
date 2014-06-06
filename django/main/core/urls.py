from django.conf.urls.defaults import *

urlpatterns = patterns(
    'core',
    (r'^$', 'views.display'),
    (r'^status$', 'views.status'),
    (r'^content/(?P<entry_id>[a-zA-Z0-9_ ]*)$', 'views.content'),
    (r'^content/ajax/(?P<page>[0-9]+)$', 'views.content_ajax'),
    (r'^contact$', 'views.contact'),
)
