from django.urls import path

from riding_sport_clubs.web_clubs.views import HomeView, payment, ClubsListView, ClubDetailsView, ClubCreateView, \
    breeds_page, like_club, racing_info

urlpatterns = (
    path('', HomeView.as_view(), name='home page'),
    path('payment/', payment, name='pay page'),

    path('list_clubs/', ClubsListView.as_view(), name='list clubs'),
    path('like/<int:pk>', like_club, name='like club'),
    path('club_info/<int:pk>/', ClubDetailsView.as_view(), name='club info'),
    path('club/create/', ClubCreateView.as_view(), name='create club'),

    path('breeds/', breeds_page, name='breeds page'),

    path('racing_info/', racing_info, name='racing info'),
)
