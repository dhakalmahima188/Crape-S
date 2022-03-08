from msilib.schema import tables
from tabnanny import verbose
from unicodedata import category
from attr import fields
from django.db import models
from django_quill.fields import QuillField
from setuptools_scm import meta


# Create your models here.

Section_dropdown = [
    ('section', 'section'),
    ('Agriculture & land', 'Agriculture & land'),
    ('Civil Society & Foreign Aid', 'Civil Society & Foreign Aid'),
    ('Economy,Market & finance', 'Economy, Market & Finance'),
    ('Energy & Environment', 'Energy & Environment'),
    ('Industy', 'Industry'),
    ('Infrastructure,Communication & Technology',
     'Infrastructure,Communication & Technology'),
    ('Law & Justice', 'Law & Justice'),
    ('Millennium Development Goals (MDGs)', 'Millennium Development Goals (MDGs)'),
    ('Public Finance', 'Public Finance'),
    ('Public Service', 'Public Service'),
    ('Social & Human Development', 'Social & Human Development'),
    ('State & Politics', 'State & Politics'),
    ('Sustainable Development Goals (SDGs)',
     'Sustainable Development Goals (SDGs)'),
]

Institution_dropdown = [
    ('Institution by Type', 'Institution by Type'),
    ('Bagmati Province', 'Bagmati Province'),
    ('Bikas Udhyami', 'Bikas Udhyami'),
    ('Central/Federal', 'Central/Federal'),
    ('Gandaki Province', 'Gandaki Province'),
    ('International', 'International'),
    ('Karnali Province', 'Karnali Province'),
    ('Lumbini Province', 'Lumbini Province'),

]


class files(models.Model):
    # title = models.CharField(max_length=200)
    # fullfile = models.CharField(max_length=1000)
    # file = models.BinaryField()
    # institution=models.CharField(max_length=200)
    # url=models.CharField(max_length=200)

    # #check??
    # #make folder attribute by yourself
    # language=models.CharField(max_length=100)
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    # creation_date = models.CharField(max_length=200)
    # preview = models.BinaryField()

    section = models.CharField(max_length=100, choices=Section_dropdown)
    institutiontype = models.CharField(
        max_length=100, choices=Institution_dropdown)
    institution = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = QuillField()
    publishedby = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    ADBS = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    youtubeurl = models.CharField(max_length=200)

    file = models.FileField()
    thumbimage = models.ImageField()
    status = models.CharField(max_length=100)
    pubdate = models.CharField(max_length=100)
    metadescription = models.TextField(max_length=2000)
    metakeywords = models.TextField(max_length=2000)
    slug = models.SlugField(max_length=200, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    creation_date = models.CharField(max_length=200)
    preview = models.BinaryField()

    fullfile = models.CharField(max_length=1000)
    id = models.BigIntegerField(primary_key=True, null=False,)

    class Meta:
        db_table = "news_files"


# parameters_add
# institution(url parse)
# url
# title_actual
# published date
# 1at 5 pages preview


def __str__(self):
    return self.title

    # tabular form


# class fileTable(tables.Table):

#     class Meta:
#         model = files
#         fields = ('section', 'title', 'institutiontype')


class tableForm(models.Model):
    section = models.CharField(max_length=100, choices=Section_dropdown)
    institutiontype = models.CharField(
        max_length=100, choices=Institution_dropdown)
    institution = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = QuillField()
    publishedby = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    ADBS = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    youtubeurl = models.CharField(max_length=200)

    file = models.FileField(
    )
    thumbimage = models.ImageField()
    status = models.CharField(max_length=100)
    pubdate = models.CharField(max_length=100)
    metadescription = models.TextField(max_length=2000)
    metakeywords = models.TextField(max_length=2000)
    slug = models.SlugField(max_length=200, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    creation_date = models.CharField(max_length=200)
    preview = models.BinaryField()

    fullfile = models.CharField(max_length=1000)
