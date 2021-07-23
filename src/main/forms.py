from django.forms import ModelForm, Textarea, TextInput, Select
from django import forms

from main.models import Post, Subscriber, Author


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название поста",
            }),
            "description": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Краткое описание",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержание",
            }),
        }


class SubscriberForm(ModelForm):
    # CharField - если поле author_id просто перечисление, без привязки к другой модели.
    # author_id = forms.CharField(
    #     widget=forms.Select(
    #         choices=Author.objects.all().order_by('name').values_list('id', 'name'),
    #         attrs={
    #             'class': 'form-control',
    #         }),
    # )

    # author_id = forms.ModelChoiceField(
    #     queryset=Author.objects.all().order_by('name'),
    #     empty_label='Выберите автора',
    #     widget=forms.Select(attrs={
    #         "class": "form-control",
    #     }),
    # )

    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email подписчика',
            }),
            "author_id": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "ID автора",
                }),
        }

    # def save(self, commit=True):
    #     # forms.ModelForm.save(self, commit)
    #     # super().save(commit=False)
    #
    #     print('SubscriberForm BEFORE save')
    #     sbr = super().save(commit=False)
    #     sbr.email_to = sbr.email_to.title() + " [email]"
    #     sbr.save()
    #     print('SubscriberForm AFTER save')
    #     return sbr
