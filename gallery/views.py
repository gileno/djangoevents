#encoding: utf-8

from django.shortcuts import render, get_object_or_404

from .models import Album

def album(request, pk):
    template_name = 'gallery/album.html'
    context = {}
    context['album'] = get_object_or_404(Album, pk=pk)
    return render(request, template_name, context)