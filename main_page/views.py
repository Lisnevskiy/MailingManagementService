from django.shortcuts import render

from mailing.models import Mailing
from main_page.services import get_blogs_cache
from recipient.models import Recipient


def main_page(request):
    """
    Отображает главную страницу.
    Args:
        request (HttpRequest): Запрос от пользователя.
    Returns:
        HttpResponse: Ответ, содержащий главную страницу.
    """
    blogs = get_blogs_cache()

    if request.user.is_authenticated:
        # Если пользователь аутентифицирован, получаем его рассылки и получателей
        mailings = Mailing.objects.filter(sender=request.user)
        active_mailings = len(Mailing.objects.filter(status=Mailing.STATUS_STARTED, sender=request.user))
        count_mailings = len(mailings)
        recipients_count = len(Recipient.objects.filter(sender=request.user))

        context = {
            'mailings': mailings,
            'active_mailings': active_mailings,
            'count_mailings': count_mailings,
            'blogs': blogs,
            'recipients_count': recipients_count,
            'title': 'Главная страница'
        }

    else:
        # Если пользователь не аутентифицирован, показываем только блоги
        context = {
            'blogs': blogs,
            'title': 'Главная страница'
        }

    return render(request, 'main_page/main_page.html', context=context)
