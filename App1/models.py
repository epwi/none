from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Ticket(models.Model):
	STATUS_CHOICES = (
		('A', 'پاسخ داده شده'),  # answered
		('P', 'در حال بررسی'),   # Pending
		('C', 'بسته شده')        # closed
	)
	title             = models.CharField(max_length=150, verbose_name="عنوان")
	sender            = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="فرستنده", related_name="UTickets", null=True)
	created           = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
	status            = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name="وضعیت")
	is_deleted        = models.BooleanField(default=False, verbose_name="حذف شده / نشده")
	is_read_by_admin  = models.BooleanField(default=False, verbose_name="خوانده شده / نشده توسط ادمین")
	is_read_by_sender = models.BooleanField(default=True, verbose_name="خوانده شده / نشده توسط فرستنده")

	def __str__(self):
		return f"{self.sender} - {self.title[:30]}"

	def get_absolute_url(self):
		return reverse('App1:ticket-detail', args=[self.id])

	class Meta:
		verbose_name = "تیکت"
		verbose_name_plural = "تیکت ها"
		ordering = ('-created',)

class TicketMessage(models.Model):
	ticket  = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="مربوط به تیکت", related_name="TMessages")
	created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
	sender  = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فرستنده")
	text    = models.TextField(verbose_name="متن پیام")

	def __str__(self):
		return f"{self.sender} - {self.ticket.sender} ({self.ticket.title[:15]} .. )"

	class Meta:
		verbose_name = "پیام تیکت"
		verbose_name_plural = "پیام های تیکت"
