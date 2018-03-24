from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^animals/create/$', views.create_animal, name='create/'),
    url(r'^animals/(?P<owner_id>[0-9]+)/$', views.get_animals, name='get_animals/'),
    url(r'^animals/delete/$', views.delete_animal, name='delete_animal/'),
    url(r'^animals/update/$', views.udpate_animal, name='update_animals/'),

]