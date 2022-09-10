from django.urls import path

from .views import  GetMapindi_all_video,GetSingleVideo, GetMapindiSeason, GetMapindiUserVote,GetMapindiUserVote,GetMapindiVideoComment

urlpatterns = [

    
    path("video/", GetMapindi_all_video.as_view()),
    path("season", GetMapindiSeason.as_view()),
    path("vote", GetMapindiUserVote.as_view()),
    path("comment", GetMapindiVideoComment.as_view()),
    path("single", GetSingleVideo.as_view()),
   
]