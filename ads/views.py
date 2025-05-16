from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, Response
from .forms import AdForm, ResponseForm
from .filters import ResponseFilter
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import reverse

class HomeView(TemplateView):
    template_name = 'ads/home.html'

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ad_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResponseCreateView(LoginRequiredMixin, CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'ads/response_form.html'

    def get_success_url(self):
        return reverse('ad_detail', kwargs={'pk': self.kwargs['ad_id']})

    def form_valid(self, form):
        ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        existing_response = Response.objects.filter(ad=ad, author=self.request.user).first()

        if existing_response:
            existing_response.text = form.cleaned_data['text']
            existing_response.save()
            messages.success(self.request, "Ваш отклик обновлён!")
            return redirect('ad_detail', pk=ad.id)

        form.instance.author = self.request.user
        form.instance.ad = Ad.objects.get(pk=self.kwargs['ad_id'])
        return super().form_valid(form)


class ResponseListView(LoginRequiredMixin, ListView):
    model = Response
    filterset_class = ResponseFilter
    template_name = 'ads/response_list.html'
    context_object_name = 'responses'
    def get_queryset(self):
        return Response.objects.filter(ad__author=self.request.user)

def accept_response(request, pk):
    response = get_object_or_404(Response, pk=pk, ad__author=request.user)
    if not response.is_accepted:
        response.is_accepted = True
        response.save()
        messages.success(request, 'Отклик принят!')
    return redirect('response_list')

def reject_response(request, pk):
    response = get_object_or_404(Response, pk=pk, ad__author=request.user)
    response.delete()
    messages.success(request, 'Отклик удалён.')
    return redirect('response_list')

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'object_list'
    ordering = ['-created_at']


class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
