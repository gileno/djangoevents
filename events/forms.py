#encoding: utf-8

from django import forms

from models import Comment, Event

class CommentForm(forms.ModelForm):

    def clean_website(self):
        website = self.cleaned_data['website']
        if website:
            facebook_prefix = 'facebook.com'
            if facebook_prefix not in website:
                message = u'Link do facebook inválido'
                raise forms.ValidationError(message)
            else:
                preffix_link = 'fb.me'
                website = website.replace(facebook_prefix, 
                                          preffix_link)
        return website

    class Meta:
        model = Comment
        exclude = ['event']

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['user']