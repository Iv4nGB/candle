from django.shortcuts import render, redirect
import logging
# from . import models
from . import forms
import requests

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('request index')
    return render(request, 'myapp/index.html')


def catalog(request):
    logger.debug('request catalog')
    return render(request, 'myapp/catalog.html')


def about_products(request):
    logger.debug('request about_products')
    return render(request, 'myapp/about_products.html')


def aroma_oil(request):
    logger.debug('request aroma_oil')
    return render(request, 'myapp/aroma_oil.html')


def send_by_telegram(message_bot):
    tel_bot = "TOKEN"
    chat_id = "chat_id"
    url = f"https://api.telegram.org/bot{tel_bot}/sendMessage?chat_id={chat_id}&text={message_bot}"
    try:
        requests.get(url).json()
        logger.debug('сообщение в телеграмм успешно отправлено')
    except ConnectionError:
        logger.error('сообщение в телеграмм НЕ отправлено!')


def master_class(request):
    logger.debug('request master_class')
    if request.method == 'POST':
        form = forms.AddMasterClassForm(request.POST)
        if form.is_valid():
            object_order = form.save()
            # Сообщение в телеграмм
            message_bot = f'Заявка на участие в мастер-классе:' \
                          f'\nУчастник: № {object_order.pk},' \
                          f'\n имя: {form.cleaned_data["customer_name"]},' \
                          f'\n телефон:  {form.cleaned_data["customer_phone"]}'
            send_by_telegram(message_bot)
            return redirect('master_cass_confirm')
    else:
        form = forms.AddMasterClassForm()
    return render(request, 'myapp/master_class.html', {'form': form})


def master_cass_confirm(request):
    logger.debug('request master_cass_confirm')
    return render(request, 'myapp/master_cass_confirm.html')


def gift_certificate(request):
    logger.debug('request gift_certificate')
    if request.method == 'POST':
        form = forms.AddGiftCertificate(request.POST)
        if form.is_valid():
            object_order = form.save()
            # Сообщение в телеграмм
            message_bot = f'Требуется обратная связь' \
                          f'\nЗаявка № {object_order.pk},' \
                          f'\n имя: {form.cleaned_data["customer_name"]},' \
                          f'\n телефон:  {form.cleaned_data["customer_phone"]}'
            send_by_telegram(message_bot)
            return redirect('master_cass_confirm')
    else:
        form = forms.AddGiftCertificate()
    return render(request, 'myapp/gift_certificate.html', {'form': form})


def reviews(request):
    logger.debug('request reviews')
    return render(request, 'myapp/reviews.html')
