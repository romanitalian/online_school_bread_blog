from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views.generic import UpdateView, CreateView, ListView

from account.forms import AvaForm
from account.models import User, Ava


class MyProfile(LoginRequiredMixin, UpdateView):
    queryset = User.objects.filter(is_active=True)
    fields = ('first_name', 'last_name',)
    success_url = reverse_lazy('home_page')

    def get_object(self, queryset=None):
        return self.request.user


class AvaCreate(LoginRequiredMixin, CreateView):
    model = Ava
    form_class = AvaForm
    success_url = reverse_lazy('home_page')

    # # variant - #1
    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     return form_class(request=self.request, **self.get_form_kwargs())

    # TODO add: variant - #2
    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs['request'] = self.request
        return form_kwargs


class AvaList(LoginRequiredMixin, ListView):
    queryset = Ava.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    # def get_queryset(self):
    #     return self.request.user.ava_set.all()
