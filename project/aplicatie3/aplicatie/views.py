from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import redirect, render

from aplicatie.models import Jobs


class JobsView(LoginRequiredMixin, ListView):
    model = Jobs
    template_name = 'aplicatie/jobs_index.html'


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Jobs
    fields = ['job_type', 'url', 'title',
              'description', 'how_to_apply', 'active']
    template_name = 'aplicatie/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_jobs')


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Jobs
    fields = ['job_type', 'url', 'title',
              'description', 'how_to_apply', 'active']
    template_name = 'aplicatie/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:lista_jobs')


@login_required
def delete_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=0)
    return redirect('jobs:lista_jobs')


@login_required
def activate_job(request, pk):
    Jobs.objects.filter(id=pk).update(active=1)
    return redirect('jobs:lista_jobs')
