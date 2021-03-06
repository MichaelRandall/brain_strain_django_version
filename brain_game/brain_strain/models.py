from django.db import models
from django_countries.fields import CountryField


class Country(models.Model):
    country_name = models.CharField(max_length=254)

    def __unicode__(self):
        return unicode(self.country_name)


class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    player_gender = models.CharField(max_length=10)
    player_country = CountryField()
    sign_up_date = models.DateField(auto_now_add=True)
    last_sign_in_date_time = models.DateTimeField(auto_now=True)
    total_games_played = models.IntegerField(default=0)
    games_won = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.first_name + " " + self.last_name)


class GameStat(models.Model):
    number_of_moves = models.IntegerField(default=0)
    game_player = models.ForeignKey(Player)
    game_start_date_time = models.DateTimeField()
    game_end_date_time = models.DateTimeField()

    def __unicode__(self):
        return unicode(str(self.id) + " " + self.game_player.first_name)


class GamesRecord(models.Model):
    time_date_played = models.DateTimeField(auto_now_add=True)
    time_date_started = models.DateTimeField(auto_now_add=True)
    time_date_completed = models.DateTimeField(auto_now=True)
    game_winner = models.ForeignKey(Player, related_name='game_player_winner')
    player_one = models.ForeignKey(Player, related_name='game_player_one')
    number_of_moves = models.IntegerField(default=0)
    player_two = models.ForeignKey(Player, related_name='game_player_two')

    def __unicode__(self):
        return unicode(self.game_winner)


class GameInProgress(models.Model):
    turn_count = models.IntegerField(default=0)
    current_player = models.ForeignKey(Player)

    def __unicode__(self):
        return unicode("Current player: " + str(self.current_player))


