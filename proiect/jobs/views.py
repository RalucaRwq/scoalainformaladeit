from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView

from jobs.models import Job


class CreateJobView(CreateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:list')


class UpdateJobView(UpdateView):
    model = Job
    fields = '__all__'
    template_name = 'jobs/jobs_form.html'

    def get_success_url(self):
        return reverse('jobs:list')

class ListJobView(ListView):
    model = Job
    template_name = 'jobs/jobs_index.html'
