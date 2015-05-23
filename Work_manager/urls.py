from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#from TasksManager import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'TasksManager.views.index.page', name="public_index"),
#    url(r'^index$','TasksManager.views.index.page'),
#    url(r'^connection-TasksManager$', 'TasksManager.views.connection.page', name="public_connection"),

# for graphing
#    url(r'^sample_graph/$', 'TasksManager.views.graph.page', name="graph"),
     url(r'^create-developer$', 'TasksManager.views.create_developer.page',name="create_developer"),
)


