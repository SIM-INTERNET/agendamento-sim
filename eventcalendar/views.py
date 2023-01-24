from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from calendarapp.models.db import *
from calendarapp.models import Event


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        Atendimentos = Atendimento.objects.all()
        qtd_confirmados = 2
        qtd_comcluidos = 20
        qtd_reagendados = 5
        tecnicos = 3
    
        context = {
            "Confirmados": qtd_confirmados,
            "Comcluidos": qtd_comcluidos,
            "Atendimentos": Atendimentos,
            "Reagendados": qtd_reagendados,
            "Tecnicos": tecnicos,

        }
        return render(request, self.template_name, context)
    
    # class DashboardView(LoginRequiredMixin, View):
    # login_url = "dashboard"
    # template_name = "calendarapp/dashboard.html"

    # def get(self, request, *args, **kwargs):
    #     events = Event.objects.get_all_events(user=request.user)
    #     running_events = Event.objects.get_running_events(user=request.user)
    #     latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
    #     context = {
    #         "total_event": events.count(),
    #         "running_events": running_events,
    #         "latest_events": latest_events,
    #     }
    #     return render(request, self.template_name, context)
    

