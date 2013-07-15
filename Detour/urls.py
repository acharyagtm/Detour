from django.conf.urls import patterns, include, url
from Detour.views import hello, index, sms_submit, search, process_questionnaire_xml, process_SMS, write_XML,\
    process_questionnaire_xml
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),                   
    url(r'^hello/$',hello),
    url(r'^submit_SMS/$', sms_submit),
    url(r'^search/$', search),
    url(r'^process_xml/$',process_questionnaire_xml),
    url(r'^process_SMS/$',process_SMS),
    url(r'^write_XML/$',write_XML),
    # Examples:
    # url(r'^$', 'test_server.views.home', name='home'),
    # url(r'^test_server/', include('test_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
