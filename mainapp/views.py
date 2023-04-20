from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Deal
from .models import ListOfCountries


def main(request):
    return render(request, 'mainapp/index.html')


def deals(request):
    title = 'предложение'

    list_of_deals = Deal.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_deals': list_of_deals,
    }

    return render(request, 'mainapp/deals.html', content)


def deal(request, pk):
    title = 'предложение'

    content = {
        'title': title,
        'deal': get_object_or_404(Deal, pk=pk),
    }

    return render(request, 'mainapp/deal_details.html', content)
