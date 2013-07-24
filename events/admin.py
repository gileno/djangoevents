#encoding: utf-8

from django.contrib import admin
from django.http import HttpResponse

from models import Event, Comment

def mark_private(modeladmin, request, queryset):
    queryset.update(public=False)
    modeladmin.message_user(request, 
                            u'Eventos atualizados com sucesso')
mark_private.short_description = u'Marcar como evento privado'

class EventAdmin(admin.ModelAdmin):

    list_display = ['name', 'type', 'public', 'comments_count']
    search_fields = ['name']
    actions = [mark_private]

admin.site.register(Event, EventAdmin)

class CommentAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'event']
    search_fields = ['event__name']

admin.site.register(Comment, CommentAdmin)