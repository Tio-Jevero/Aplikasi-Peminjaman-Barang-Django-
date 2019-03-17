from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class barang(models.Model):
    barang = models.CharField(max_length=250)
    nomor_barang  = models.CharField(max_length=200)
    peminjam = models.CharField(max_length=200)
    daftar_kelas = (
        ('X TKJ 1', 'X TKJ 1' ),
        ('X TKJ 2', 'X TKJ 2'),
        ('X TKJ 3', 'X TKJ 3'),
        ('XI TKJ 1', 'XI TKJ 1'),                
        ('XI TKJ 2', 'XI TKJ 2'), 
        ('XI TKJ 3', 'XI TKJ 3'), 
        ('XII TKJ 1', 'XII TKJ 1'), 
        ('XII TKJ 2', 'XII TKJ 2'),
        ('XII TKJ 3', 'XII TKJ 3'),
        ('Kelas Lain', 'Kelas Lain'),
    )
    kelas_peminjam = models.CharField(
        max_length = 50,
        choices = daftar_kelas,
        default = 'Kelas Lain'
    )
    waktu_pinjam = models.DateTimeField(default=timezone.now)
    waktu_kembali = models.DateTimeField(blank=True, null=True, editable=False)
    status = models.CharField(max_length = 50,blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id,self.barang)


