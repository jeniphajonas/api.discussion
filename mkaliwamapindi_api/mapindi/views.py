from requests import get
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MapindiSerializer, MapindiSeasonSerializer, MapindiUserVoteSerializer,MapindiVideoCommentSerializer
from .selectors import Mapindi,Season,UserVote,MapindiVideoComment, all_video,Comment,SingleVideo

class GetMapindi_all_video(APIView):
    querset=all_video()
    serializer_class=MapindiSerializer
    def get(self,request):
        serializer=MapindiSerializer(all_video(),many=True)
        return Response(serializer.data,status=200)
      


     
class GetSingleVideo(APIView):
    querset= SingleVideo()
    serializer_class=MapindiSerializer
    def get(self,request,video_id):
        serializer=MapindiSerializer(SingleVideo(video_id),many=True)
        return Response({"results": serializer.data})
    



class GetMapindiSeason(APIView):
    querset=Season()
    serializer_class=MapindiSeasonSerializer
    def get(self,request):
        serializer=MapindiSeasonSerializer(Season(),many=True)
        return Response(serializer.data,status=200)



class GetMapindiUserVote(APIView):
    querset=UserVote()
    serializer_class=MapindiUserVoteSerializer
    def get(self,request):
        serializer=MapindiUserVoteSerializer(UserVote(),many=True)
        return Response(serializer.data,status=200)




class GetMapindiVideoComment(APIView):
    queryset=Comment
    def get(self, request):
      serializer =MapindiVideoCommentSerializer(Comment(), many=True)
      return Response(serializer.data)    









