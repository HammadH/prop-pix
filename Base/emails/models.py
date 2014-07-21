from django.db import models
from django.contrib import admin

class Leads(models.Model):
	email = models.EmailField(blank=True)

	def __unicode__(self):
		return self.email


admin.site.register(Leads)