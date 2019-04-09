from django.db import models

# inspectdb:反向生成model
# Create your models here.

class Conference(models.Model):
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    literature = models.CharField(max_length=255, blank=True, null=True)
    meetingname = models.CharField(db_column='meetingName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meetingtime = models.CharField(db_column='meetingTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meetingadress = models.CharField(db_column='meetingAdress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organizer = models.CharField(max_length=255, blank=True, null=True)
    languages = models.CharField(max_length=15, blank=True, null=True)
    classnumber = models.CharField(db_column='classNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=125, blank=True, null=True)  # Field name made lowercase.
    pagenumber = models.CharField(db_column='pageNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    searchkey = models.CharField(db_column='searchKey', max_length=125, blank=True, null=True)  # Field name made lowercase.
    searchtype = models.CharField(db_column='searchType', max_length=125, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conference'


class Degree(models.Model):
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    degreeunit = models.CharField(db_column='degreeUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    awardedthedegree = models.CharField(db_column='awardedTheDegree', max_length=255, blank=True, null=True)  # Field name made lowercase.
    professional = models.CharField(max_length=255, blank=True, null=True)
    mentorname = models.CharField(db_column='mentorName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    degreeinannual = models.CharField(db_column='degreeInAnnual', max_length=255, blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(max_length=50, blank=True, null=True)
    classnumber = models.CharField(db_column='classNumber', max_length=60, blank=True, null=True)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=25, blank=True, null=True)  # Field name made lowercase.
    searchkey = models.CharField(db_column='searchKey', max_length=25, blank=True, null=True)  # Field name made lowercase.
    searchtype = models.CharField(db_column='searchType', max_length=55, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'degree'


class Perio(models.Model):
    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    englishtitle = models.CharField(db_column='englishTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    doi = models.CharField(max_length=255, blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    englishkeywords = models.CharField(db_column='englishKeyWords', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authors = models.CharField(max_length=125, blank=True, null=True)
    englishauthors = models.CharField(db_column='englishAuthors', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(max_length=75, blank=True, null=True)
    journalname = models.CharField(db_column='journalName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    journal = models.CharField(max_length=255, blank=True, null=True)
    yearsinfo = models.CharField(db_column='yearsInfo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    journalsection = models.CharField(db_column='journalSection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classnumber = models.CharField(db_column='classNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    fundprogram = models.CharField(db_column='fundProgram', max_length=125, blank=True, null=True)  # Field name made lowercase.
    publishtime = models.CharField(db_column='publishTime', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(max_length=6, blank=True, null=True)
    pagenumber = models.CharField(db_column='pageNumber', max_length=6, blank=True, null=True)  # Field name made lowercase.
    searchkey = models.CharField(db_column='searchKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    searchtype = models.CharField(db_column='searchType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perio'


class Tech(models.Model):

    title = models.CharField(unique=True, max_length=255, blank=True, null=True)
    englishtitle = models.CharField(db_column='englishTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    reporttype = models.CharField(db_column='reportType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openrange = models.CharField(db_column='openRange', max_length=125, blank=True, null=True)  # Field name made lowercase.
    pagenumber = models.CharField(db_column='pageNumber', max_length=25, blank=True, null=True)  # Field name made lowercase.
    projectname = models.CharField(db_column='projectName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    planname = models.CharField(db_column='planName', max_length=125, blank=True, null=True)  # Field name made lowercase.
    compiletime = models.CharField(db_column='compileTime', max_length=125, blank=True, null=True)  # Field name made lowercase.
    approvalyear = models.CharField(db_column='approvalYear', max_length=125, blank=True, null=True)  # Field name made lowercase.
    collection = models.CharField(max_length=125, blank=True, null=True)
    searchkey = models.CharField(db_column='searchKey', max_length=125, blank=True, null=True)  # Field name made lowercase.
    searchtype = models.CharField(db_column='searchType', max_length=125, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tech'

