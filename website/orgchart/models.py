from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html
from mptt.models import MPTTModel, TreeForeignKey
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.urlresolvers import reverse

class Person(MPTTModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    boss = TreeForeignKey('self', null=True, blank=True, related_name='subordinates')
    photo = ThumbnailerImageField(upload_to='photos', blank=True)
    nickname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.full_name()
    
    def short_name(self):
        return self.name + ' ' + self.surname
    
    def full_name(self):
        name = self.name + ' ' + self.surname
        if self.nickname:
            name = name + ' (%s)' % self.nickname
        return name
    
    def title(self):
        return ', '.join(self.title_set.values_list('title', flat=True))
    
    def phone(self):
        return ', '.join(self.phonenumber_set.values_list('number', flat=True))
    
    def photo_html(self):
        if self.photo:
            return format_html('<img src="{0}" alt="{1}">',
                self.photo.get_thumbnail({'size':(35, 35)}).url,
                self.full_name()
            )
        else:
            return ''
    photo_html.short_description = 'pic'
    photo_html.allow_tags = True
    
    def get_absolute_url(self):
        return reverse('person_detail', kwargs={'pk':self.id})
    
    def levels_below(self):
        bottom = self.get_descendants().aggregate(max=models.Max('level'))['max']
        if bottom is None:
            return 0
        else:
            return bottom - self.level
    
    class Meta:
        ordering = ['surname', 'name']
        verbose_name_plural = 'people'
    
    class MPTTMeta:
        parent_attr = 'boss'

class PhoneNumber(models.Model):
    person = models.ForeignKey(Person)
    number = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.number

class Title(models.Model):
    person = models.ForeignKey(Person)
    title = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.title
