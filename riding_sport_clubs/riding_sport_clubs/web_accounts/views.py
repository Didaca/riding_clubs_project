import os

from django.shortcuts import redirect
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy

from riding_sport_clubs.web_accounts.forms import UserRegistrationForm
from riding_sport_clubs.web_accounts.models import Profile, HorseUser


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'account/create_profile.html'

    success_url = reverse_lazy('login')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('list clubs')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home page')


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'account/edit_password.html'
    success_url = reverse_lazy('list clubs')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'account/details_profile.html'


class ProfileEditView(UpdateView):
    model = Profile
    fields = ('email', 'phone_number', 'picture',)
    template_name = 'account/edit_profile.html'

    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'account/delete_profile.html'

    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

    def form_valid(self, form):
        success_url = self.get_success_url()
        u = HorseUser.objects.filter(pk=self.object.pk)
        img = Profile.objects.get(pk=self.request.user.pk).picture.path
        u.delete()
        self.object.delete()
        os.remove(img)
        return redirect(success_url)
