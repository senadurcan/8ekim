from django.db import models

# Create your models here.

class Construction(models.Model):
    title = models.CharField(("Proje Adı"),max_length=100) ###kelime sınırlama
    detay = models.TextField(("Proje Detayları"))
    proje_user = models.CharField(("Proje Sorumlusu"), max_length=50)
    maliyet = models.IntegerField(("Maliyet"),null=True,blank=True)###integer değer ile sayı yazma 
    image = models.FileField(("Proje Resmi"), upload_to='', max_length=100)
    
    def __str__(self) -> str:
        return self.title   ####admin panelinde görünür obje adları sağlanır.
    