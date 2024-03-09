# websites/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from .models import *
from .forms import InputIndexForm


def desktop_view(request):
    indexes = Index.objects.all().order_by('website_index_position_num')

    # context or data to webpage
    context = {
        'indexes': indexes,
    }
    return render(request, 'websites/desk_top.html', context)


@csrf_exempt
def update_order(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        order = request.POST.get('order').split(',')

        for position_num, index_id in enumerate(order, start=1):
            Index.objects.filter(id=index_id).update(website_index_position_num=position_num)
        return JsonResponse({'message': 'Order updated successfully'})

    return JsonResponse({'message': 'Invalid request'}, status=400)


def input_index_view(request):
    index_form = InputIndexForm()

    if request.method == 'POST':
        if 'index_form_submit' in request.POST:
            index_form = InputIndexForm(request.POST, request.FILES)
            if index_form.is_valid():
                index_form.save()
                return redirect('/')

    context = {
        'index_form': index_form,
    }

    return render(request, 'websites/input_index.html', context)


def delete_index(request, pk):
    index = Index.objects.get(id=pk)
    if request.method == "POST":
        confirmation_code = request.POST.get('confirmation_code')

        # Check if the confirmation code is valid (preset to 123)
        if confirmation_code == '123':
            index.delete()
            return redirect('/')
        else:
            context = {
                'index': index,
                'msg': 'wrong delete code'
            }
            return render(request, 'websites/delete_index.html', context)

    context = {'index': index}
    return render(request, 'websites/delete_index.html', context)


def desktop_view_for_delete_icon(request):
    indexes = Index.objects.all().order_by('website_index_position_num')

    # context or data to webpage
    context = {
        'indexes': indexes,
    }
    return render(request, 'websites/desk_top_for_delete_icon.html', context)
