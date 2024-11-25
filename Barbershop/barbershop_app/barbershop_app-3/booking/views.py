from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Master, Service, Visit
from .forms import VisitForm
from django.views.decorators.http import require_POST
from django.conf import settings
import telegram

def main_page(request):
       masters = Master.objects.all()
       visit_form = VisitForm()
       return render(request, 'main.html', {'masters': masters, 'visit_form': visit_form})

def thank_you_page(request):
       return render(request, 'thank you.html')

@require_POST
def create_booking(request):
       form = VisitForm(request.POST)
       if form.is_valid():
           visit = form.save()
           # Sending notification to Telegram
           send_telegram_notification(visit)
           return redirect('thank_you_page')
       return render(request, 'main.html', {'visit_form': form})

def service_fetch(request):
       master_id = request.GET.get('master_id')
       services = Service.objects.filter(master__id=master_id)
       service_list = [{'name': service.name, 'id': service.id} for service in services]
       return JsonResponse(service_list, safe=False)

def send_telegram_notification(visit):
       bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
       message = (
           f"Новая заявка от {visit.name}\\n"
           f"Телефон: {visit.phone}\\n"
           f"Мастер: {visit.master}\\n"
           f"Услуга: {visit.service}"
       )
       bot.send_message(chat_id=settings.ADMIN_CHAT_ID, text=message)