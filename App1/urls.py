from django.urls import path
from . import views

app_name = "App1"

urlpatterns = [
	path('', views.Home, name="home"),
	path('Tickets/', views.Tickets, name="tickets"),
	path('Ticket/<int:TicketID>', views.TicketDetail, name="ticket-detail"),
	path('ADDTicket/', views.ADDTicket, name='add-ticket'),
]