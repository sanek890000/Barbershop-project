from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Application
from django.urls import reverse_lazy

class ApplicationListView(ListView):
       model = Application
       template_name = 'cabinet/application_list.html'

class ApplicationDetailView(DetailView):
       model = Application
       template_name = 'cabinet/application_detail.html'

class ApplicationCreateView(CreateView):
       model = Application
       fields = ['title', 'description', 'status']
       template_name = 'cabinet/application_form.html'
       success_url = reverse_lazy('cabinet:application_list')

class ApplicationUpdateView(UpdateView):
       model = Application
       fields = ['title', 'description', 'status']
       template_name = 'cabinet/application_form.html'
       success_url = reverse_lazy('cabinet:application_list')

class ApplicationDeleteView(DeleteView):
       model = Application
       template_name = 'cabinet/application_confirm_delete.html'
       success_url = reverse_lazy('cabinet:application_list')