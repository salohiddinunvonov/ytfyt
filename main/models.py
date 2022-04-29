from typing import List
from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    all_name = models.CharField(max_length=255)


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class AudioBook(models.Model):
    img = models.ImageField(upload_to='book/image/')
    name = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField(upload_to="book/files/audio/")
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)
    auth = models.ForeignKey(Client, on_delete=models.CASCADE)
    data = models.DateField()
    rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Historyaudio(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Book(models.Model):
    img = models.ImageField(upload_to='book/image/')
    name = models.CharField(max_length=255)
    text = models.TextField()
    file = models.FileField(upload_to="book/files/")
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)
    auth = models.ForeignKey(Client, on_delete=models.CASCADE)
    data = models.DateField()
    rating = models.IntegerField(default=0)
    rating_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    star = models.IntegerField()

    
    def __str__(self):
        return self.star


class HistoryAudioBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class HistoryBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class HistoryBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class AudioHistoryBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class RatingAudioBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class RatingBook(models.Model):
    type = models.IntegerField(choices=((1,"go to"), (2, "reading"), (3, "readed")))
    book = models.ForeignKey(AudioBook, on_delete=models.CASCADE)
    user = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username