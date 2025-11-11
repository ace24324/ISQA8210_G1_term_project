from django.urls import path
from . import views
from .views import FilteredResultsView

urlpatterns = [
    path('', views.index, name='index'),

    path('contact', views.contact, name='contact'),

    path('list_contact', views.list_contact, name='list_contact'),

    path('contact_success', views.contact_success, name='contact_success'),

    path('listing_list/', views.PropListView.as_view(), name='listing_list'),

    path('listing_detail/<int:pk>', views.PropDetailView.as_view(), name='listing_detail'),

    path('events_list/', views.EventsListView.as_view(), name='events_list'),

    path('event_detail/<int:pk>', views.EventsDetailView.as_view(), name='events_detail'),

    path('filtered_results/', FilteredResultsView.as_view(), name='filtered_results'),

    path('profile', views.profile, name='profile'),

    path('listing/create/', views.PropDetailCreate.as_view(), name='listing_create'),
    path('listing/<int:pk>/update/', views.PropDetailUpdate.as_view(), name='listing_update'),

    path('events/create/', views.EventsDetailCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventsDetailUpdate.as_view(), name='events_update'),

]

