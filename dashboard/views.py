from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from .forms import barangForm
from . import models

def home(request):
    form_barang = barangForm(request.POST or None)
    list_pinjaman = models.barang.objects.order_by('-waktu_pinjam')
    barang = models.barang.objects.all()
    if request.method == 'POST':
        if form_barang.is_valid():
            form_barang.save()
            print('list peminjaman barang',form_barang.data['barang'],'nomor ({})'.format(form_barang.data['nomor_barang']), 'ditambahkan ')
            return redirect('/')
    context = {
        'form':form_barang,
        'listpinjaman':list_pinjaman,
    }
    return render(request, 'home.html', context)

def barang_kembali(request, pk):
    barang = models.barang.objects.get(pk=pk)
    barang.waktu_kembali = timezone.now()
    barang.save()
    print('barang',barang.barang,'({})'.format(barang.nomor_barang), 'dikembalikan ')
    return redirect('/')

def barang_belum_kembali(request, pk):
    barang = models.barang.objects.get(pk=pk)
    barang.waktu_kembali = ("")
    barang.save()
    print('barang',barang.barang,'({})'.format(barang.nomor_barang), 'ternyata belum dikembalikan ')
    return redirect('/')

def hapus_list(requet, pk):
    barang = models.barang.objects.get(pk=pk)
    barang.delete()
    print('list dari barang ',barang.barang,'({})'.format(barang.nomor_barang), 'dihapus ')
    return redirect('/')
