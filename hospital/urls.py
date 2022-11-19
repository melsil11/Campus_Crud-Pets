from django.urls import path
from .views.doctor_views import DoctorsView, DoctorDetailView
from .views.patient_views import PatientsView, PatientDetailView
from .views.appointment_views import AppointmentsView, AppointmentDetailView

urlpatterns = [
    path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor'),
    path('patients/', PatientsView.as_view(), name='patients'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient'),
    path('appointments/', AppointmentsView.as_view(), name='appointments/'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail')
]