from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=256, unique=True)
    league = models.ForeignKey('LeagueDetail', on_delete=models.CASCADE)


class Results(models.Model):
    datetime = models.DateTimeField()
    command1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    command2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    result1 = models.SmallIntegerField(default=0)
    result2 = models.SmallIntegerField(default=0)

    class Meta:
        unique_together = ['command1', 'command2']


class News(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=256, unique=True)
    content = models.TextField(null=True, blank=True)


class StandingsDetail(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mp = models.SmallIntegerField(default=0)
    w = models.SmallIntegerField(default=0)
    d = models.SmallIntegerField(default=0)
    l = models.SmallIntegerField(default=0)
    g = models.SmallIntegerField(default=0)
    pts = models.SmallIntegerField(default=0)
    form = models.CharField(max_length=200)


class Form(models.Model):
    pass


class OverUnder(models.Model):
    pass


class HtFt(models.Model):
    pass


class TopScores(models.Model):
    pass


class Standings(models.Model):
    standings = models.ForeignKey(StandingsDetail, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    over_under = models.ForeignKey(OverUnder, on_delete=models.CASCADE)
    ht_ft = models.ForeignKey(HtFt, on_delete=models.CASCADE)
    top_scores = models.ForeignKey(TopScores, on_delete=models.CASCADE)


class Archive(models.Model):
    season = models.CharField(max_length=256)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)


class Summary(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    countries = models.ForeignKey('Countries', on_delete=models.CASCADE)


class Countries(models.Model):
    flag = models.ImageField(upload_to='flags/')
    name = models.CharField(max_length=256, unique=True)


class Leagues(models.Model):
    icon = models.ImageField(upload_to='icons/')
    name = models.CharField(max_length=256, unique=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='leagues')


class LeagueDetail(models.Model):
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    results = models.ForeignKey(Results, on_delete=models.CASCADE)
