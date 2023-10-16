from django.http import JsonResponse
from django.db.models import Count, Avg, F, Func
from app_name.models import H1BApplicant
from django.http import HttpResponse
from .utilis import countndpreprocess

# Create your views here.
# I. Number of results
def index(request):
    return HttpResponse("Homepage")

def total_records(request):
    total = H1BApplicant.objects.count()
    return JsonResponse({"total_records": total})

#II. Mean salary
def mean_salary(request):
    mean = H1BApplicant.objects.aggregate(mean_salary=Avg('salary'))
    return JsonResponse(mean)

#III. Median salary
def median_salary(request):
    median = H1BApplicant.objects.aggregate(median_salary=Func(F('salary'), function='percentile_cont', expression='0.5 within group (order by salary)'))
    return JsonResponse(median)

#IV. 25% percentile salary
def percentile_25(request):
    percentile_25 = H1BApplicant.objects.aggregate(percentile_25=Func(F('salary'), function='percentile_cont', expression='0.25 within group (order by salary)'))
    return JsonResponse(percentile_25)

#V. 75% percentile salary
def percentile_75(request):
    percentile_75 = H1BApplicant.objects.aggregate(percentile_75=Func(F('salary'), function='percentile_cont', expression='0.75 within group (order by salary)'))
    return JsonResponse(percentile_75)
