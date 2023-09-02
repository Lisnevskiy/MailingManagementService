from django.shortcuts import render

from blog.models import Blog
from mailing.models import Mailing
from recipient.models import Recipient


def main_page(request):
    mailings = Mailing.objects.all()
    count_mailings = len(mailings)
    blogs = Blog.objects.all()
    recipients_count = len(Recipient.objects.all())

    context = {
        'mailings': mailings,
        'count_mailings': count_mailings,
        'blogs': blogs,
        'recipients_count': recipients_count,
        'title': 'Главная страница'
    }

    return render(request, 'mailing/main_page.html', context=context)
