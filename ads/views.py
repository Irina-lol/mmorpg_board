from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, Response

class ResponseListView(LoginRequiredMixin, ListView):
    model = Response
    template_name = 'ads/response_list.html'

    def get_queryset(self):
        return Response.objects.filter(ad__author=self.request.user)


class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'

class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'