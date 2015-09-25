from django.db import models
from django.utils import timezone


class three_letter_noun(models.Model):
	word = models.CharField(max_length=200)

class four_letter_noun(models.Model):
	word = models.CharField(max_length=200)

class double_letter_cons(models.Model):
	word = models.CharField(max_length=200)

class double_letter_vowel(models.Model):
	word = models.CharField(max_length=200)

class double_word(models.Model):
	word = models.CharField(max_length=200)

class e_2word(models.Model):
	word = models.CharField(max_length=200)

class e_3word(models.Model):
	word = models.CharField(max_length=200)

class e_4word(models.Model):
	word = models.CharField(max_length=200)

class four_word(models.Model):
	word = models.CharField(max_length=200)

class I_3word(models.Model):
	word = models.CharField(max_length=200)

class I_4word(models.Model):
	word = models.CharField(max_length=200)

class single_word(models.Model):
	word = models.CharField(max_length=200)

class st_2word(models.Model):
	word = models.CharField(max_length=200)

class st_3word(models.Model):
	word = models.CharField(max_length=200)

class st_4word(models.Model):
	word = models.CharField(max_length=200)

class three_word(models.Model):
	word = models.CharField(max_length=200)
