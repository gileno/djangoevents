#encoding: utf-8

from django.contrib import admin

from models import Photo, Album

class PhotoInline(admin.TabularInline):
    model = Photo

class AlbumAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_on']

    inlines = [PhotoInline]

admin.site.register(Album, AlbumAdmin)