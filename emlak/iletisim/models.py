from django.db import models
from datetime import datetime

class Iletisim(models.Model):
    ilan = models.CharField(max_length=200)
    ilan_id =models.IntegerField()
    isim = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    telefon = models.CharField(max_length=100)
    mesaj = models.TextField(blank=True)
    iletisim_tarihi = models.DateTimeField(default=datetime.now, blank=True)
    kullanici_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.isim
