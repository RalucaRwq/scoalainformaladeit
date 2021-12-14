from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from jobs.models import Job


class CreateJobView(LoginRequiredMixin, CreateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:list')


class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:list')


class ListJobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/jobs_index.html'

@login_required
def delete_job(request, pk):
    if request.user.is_authenticated:
        Job.objects.filter(id=pk).update(active=1)
    return redirect('jobs:list')

