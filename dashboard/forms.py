from django import forms
from .models import barang

class barangForm(forms.ModelForm):
    class Meta:
        model = barang
        fields = [
            'barang',
            'nomor_barang',
            'peminjam',
            'kelas_peminjam',
        ]

        labels = {
            'barang':'',
            'nomor_barang':'',
            'peminjam':'',
            'kelas_peminjam':'',
        }

        widgets = {
            'barang':forms.TextInput(
                attrs={
                    'class':'form-control rounded-0 mt-1 col-9',
                    'placeholder':'Nama Barang'
                }
            ),
            'nomor_barang':forms.TextInput(
                attrs={
                    'class':'form-control rounded-0 mt-1 col-3 border-left-0',
                    'placeholder':'Nomor'
                }
            ),
            'peminjam':forms.TextInput(
                attrs={
                    'class':'form-control rounded-0 mt-1 col-9',
                    'placeholder':'Nama Peminjam'
                }
            ),
            'kelas_peminjam':forms.Select(
                attrs={
                    'class':'form-control rounded-0 border-left-0 mt-1 col-3'
                }
            ),
        }
        