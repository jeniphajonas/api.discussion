from rest_framework.serializers import ModelSerializer
from . models import Mapindi,MapindiSeason,MapindiUserVote,MapindiVideoComment


class MapindiSerializer(ModelSerializer):
    class Meta:
        model = Mapindi
        fields =( "user_id", "season_id","winner_status","vote","first_name","last_name","school_name","school_location",
        "subject_name" ,"class_name" ,"lesson" ,"description","video_id","date_uploaded","status")

        
class MapindiSeasonSerializer(ModelSerializer):
    class Meta:
        model = MapindiSeason
        fields =("season_name","open_close_status","start_date", "end_date", "date_added")


class MapindiUserVoteSerializer(ModelSerializer):
    class Meta:
        model = MapindiUserVote
        fields =("user_id","video_id","date_added")


class MapindiVideoCommentSerializer(ModelSerializer):
    class Meta:
        model = MapindiVideoComment
        fields =("user_id","video_id","content","date_added")

        


