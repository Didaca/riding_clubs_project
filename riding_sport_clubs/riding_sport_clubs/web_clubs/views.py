import logging

from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect

from riding_sport_clubs.web_accounts.models import Profile
from riding_sport_clubs.web_clubs.forms import CreateClubForm
from riding_sport_clubs.web_clubs.models import Club


def racing_info(request):
    return render(request, 'web/racing_info.html')


def like_club(request, pk):
    if request.user.is_staff is False:
        club = Club.objects.get(pk=pk)
        club.rating += 1
        club.save()

    return redirect('list clubs')


def breeds_page(request):
    return render(request, 'web/home_breeds.html')


def payment(request):
    return render(request, 'web/pay_page.html')


class HomeView(views.TemplateView):
    context_key = 'user'
    conntext_value = 'No'

    template_name = 'web/home.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('list clubs')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context[self.context_key] = self.request.user.username
        else:
            context[self.context_key] = self.conntext_value

        return context


class ClubsListView(views.ListView):
    model = Club
    template_name = 'web/clubs_list.html'
    ordering = ('-award_gold', '-award_silver', '-award_bronze',)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('trainer_set')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.request.user.pk
        try:
            user_object = Profile.objects.get(pk=pk)
            context['object'] = user_object
        except Profile.DoesNotExist:
            context['object'] = None
            logging.info('authorised user')
        return context


class ClubCreateView(views.CreateView):
    form_class = CreateClubForm
    template_name = 'web/create_club.html'
    success_url = reverse_lazy('list clubs')


class ClubDetailsView(views.DetailView):
    model = Club
    template_name = 'web/club_info.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related('trainer_set')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        try:
            user_object = Profile.objects.get(pk=self.request.user.pk)
            context['object'] = user_object
        except Profile.DoesNotExist:
            context['object'] = None
        return context




