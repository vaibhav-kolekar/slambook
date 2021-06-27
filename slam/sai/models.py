from django.db import models
from django import forms

# Create your models here.

class sai(models.Model):
    name = models.CharField(max_length=35)
    rel = models.CharField(max_length=15)
    friend = models.CharField(max_length=15, default='False')
    colour = models.CharField(max_length=15, default='False')
    chara = models.CharField(max_length=15, default='False')
    quality = models.CharField(max_length=15, default='False')
    emotional = models.CharField(max_length=15, default='False')
    impression = models.CharField(max_length= 100, null=True)
    memory = models.CharField(max_length=100)
    honest = models.CharField(max_length=100)

    def __str__(self):
        return self.name

"""
bff=[('jyotya','jyotya'),
         ('roshan','roshan'),
         ('aditi', 'aditi'),
         ('shreya', 'shreya'),
         ('kanad', 'kanad'),
        ]
    friend = forms.ChoiceField(choices=bff, widget=forms.RadioSelect)

    col=[('pink', 'pink'),
        ('blue', 'blue'),
        ('black', 'black'),
        ('red', 'red'),
        ('other_colour', 'other_colour')
        ]
    colour = forms.ChoiceField(choices=col, widget=forms.RadioSelect)

    char=[('krishna', 'krishna'),
            ('draupadi', 'draupadi'),
            ('arjun', 'arjun'),
            ('other_char', 'other_char')
        ]
    character = forms.ChoiceField(choices=char, widget=forms.RadioSelect)

"""    