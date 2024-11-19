from django.urls import path
from . import views



urlpatterns = [
       path('applications/', views.ApplicationListView.as_view(), name='application_list'),
       path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application_detail'),
       path('applications/create/', views.ApplicationCreateView.as_view(), name='application_create'),
       path('applications/<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='application_update'),
       path('applications/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application_delete'),
   ]