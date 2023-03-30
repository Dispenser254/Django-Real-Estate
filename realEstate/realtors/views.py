from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Realtor
# Create your views here.

def index(request):
    realtors = Realtor.objects.order_by('-hire_date').filter(is_active=True)
    paginator = Paginator(realtors, 6)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)

    context = {
        'realtors': paged_realtors
    }
    return render(request, 'agents/agents.html', context)

def realtor(request, realtor_id):
    realtor = get_object_or_404(Realtor, pk=realtor_id)
    context = {
        'realtor': realtor
    }
    return render(request, 'agents/agent.html', context)

