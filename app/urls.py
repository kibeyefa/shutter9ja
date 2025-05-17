from django.urls import path
from .views import *

urlpatterns = [
    path("entries/", EntryListView.as_view()),
    path("entries/<id>/", SingleEntryView.as_view()),
    path("entries/<id>/vote/", EntryVoteView.as_view()),
    path("competitions/", CompetitionListView.as_view()),
    path("competitions/current/", GetCurrentCompetitionView.as_view()),
    path("competitions/<id>/", SingleCompetitionView.as_view()),
    path("contact/", ContactAPIView.as_view(), name="contact-api"),
]
