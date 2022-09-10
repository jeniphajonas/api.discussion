from mapindi.serializers import MapindiVideoCommentSerializer,MapindiSerializer
from .models import Mapindi, MapindiSeason, MapindiUserVote, MapindiVideoComment
from requests import get

# All functions that only query data on database goes here
# Get all mapindi video from database 
def all_video():
    mapindi=Mapindi.objects.all()
    return mapindi



def SingleVideo(video_id: int) -> object:
    
    #Take video_id and return single  mapindi video

    MapindiVideo= Mapindi.objects.select_related(
        'season_id', 'video_id').filter(video=video_id)
    return MapindiVideo

def UserVote():
    vote=MapindiUserVote.objects.all()
    return vote


def Season():
    mapindi=MapindiSeason.objects.all()
    return mapindi


def Comment():

  videoComment=MapindiSeason.objects.all()
  return videoComment

    

def listmapindi():
    mapindi=Mapindi.objects.all()
    return mapindi