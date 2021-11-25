from django.shortcuts import render

# Create your views here.
# CreateView -> adaugare date in formular
# UpdateView -> modificare date in formular
# DeleteView -> Stergere date in DB
# IndexView -> informare cu privire la formular
# ListView -> Ofera mai multe info de tip lista din DB
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from aplicatie1.models import Location

class CreateLocationView(CreateView):
    model = Location # modelul in care salvam datele
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')

class UpdateLocationView(UpdateView):
    model = Location # modelul in care salvam datele
    # fields = '__all__'
    fields = ['city', 'country']
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')

class ListLocationView(ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'