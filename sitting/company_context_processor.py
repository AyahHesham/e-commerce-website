#function return with dic

from .models import company

def get_company_info(request):
    companyinfo=company.objects.last()
    return{'info':companyinfo}