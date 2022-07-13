from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('candidate/',views.candidate,name='candidate'),
    path('can-register/',views.candidate_register,name='candidate-register'),
    path('voter-register/',views.voter_register,name='voter-register'),
    path('voter-list/',views.voter_list,name='voter-list'),
    path('voter-details/<str:pk>/',views.voter_details,name='voter-details'),
    path('vote-update/<str:pk>/',views.update_voter,name='vote-update'),
    path('candidate-profile/<str:pk>/',views.candidate_profile,name='candidate-profile'),
    path('candidate-update/<str:pk>/',views.update_candidate,name='candidate-update'),
    path('position/',views.position,name='position'),
    path('position-details/<str:pk>/',views.position_candidate,name='position-details'),
    path('result/',views.results,name='result'),
]
