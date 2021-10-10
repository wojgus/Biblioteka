from django.db import models
from django.db.models import Model, CharField, DO_NOTHING, ForeignKey, DateField, IntegerField, TextField


class Genre(Model):
    nazwa = CharField(max_length=128)


class Autor(Model):
    imie = CharField(max_length=128)
    nazwisko = CharField(max_length=128)


class Book(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    autor = ForeignKey(Autor, on_delete=DO_NOTHING)
    wydowanictwo = CharField(max_length=128)
    rok_wydania = DateField()
    ocena = IntegerField()
    opis = TextField()

