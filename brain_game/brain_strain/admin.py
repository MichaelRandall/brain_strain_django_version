from django.contrib import admin
from brain_strain.models import Player, GamesRecord, GameInProgress, GameStat


admin.site.register(Player)
#admin.site.register(GamesRecord)
#admin.site.register(GameInProgress)
admin.site.register(GameStat)
