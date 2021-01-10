from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketMessage
from .forms import ADDTicketForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
	return render(request, 'App1/home.html')

@login_required
def Tickets(request):
	if request.user.is_staff:
		tickets = Ticket.objects.all()
	else:
		tickets = Ticket.objects.filter(sender=request.user)
	
	context = {'tickets':tickets}
	return render(request, 'App1/Tickets.html', context)

@login_required
def TicketDetail(request, TicketID):
	ticket = get_object_or_404(Ticket, id=TicketID)
	if ticket.sender != request.user and not request.user.is_staff:
		return redirect("App1:home")
		message.error(request, 'Yot can not see this Ticket', 'danger')
	context = {'ticket':ticket}
	return render(request, 'App1/TicketDetail.html', context)

@login_required # maybe raise error
def ADDTicket(request):
	form = ADDTicketForm(request.POST or None)
	if form.is_valid():
		cd = form.cleaned_data
		Ticket.objects.create(title=cd['title'], sender=request.user, status="P")
		return redirect("App1:tickets")
		message.success(request, 'your ticket has sent', 'success')
	return render(request, 'App1/ADDTicket.html', {'form':form})


