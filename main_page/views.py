from django.shortcuts import render

from blog.models import Blog
from mailing.models import Mailing
from recipient.models import Recipient


def main_page(request):
    mailings = Mailing.objects.all()
    active_mailings = len(Mailing.objects.filter(status=Mailing.STATUS_STARTED))
    count_mailings = len(mailings)
    blogs = Blog.objects.all()
    recipients_count = len(Recipient.objects.all())

    context = {
        'mailings': mailings,
        'active_mailings': active_mailings,
        'count_mailings': count_mailings,
        'blogs': blogs,
        'recipients_count': recipients_count,
        'title': 'Главная страница'
    }

    return render(request, 'main_page/main_page.html', context=context)
