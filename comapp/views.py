from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Company

def main(request):
    return render(request, 'comapp/index.html')



def companies(request):
    title = 'компании'

    list_of_companies = Company.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_companies': list_of_companies,
    }

    return render(request, 'comapp/companies.html', content)


def company(request, pk):
    title = 'компания'

    content = {
        'title': title,
        'company': get_object_or_404(Company, pk=pk),
    }

    return render(request, 'comapp/company_details.html', content)
