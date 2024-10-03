from django.shortcuts import render

def animal_list(request):
    return render(request, 'blog/animal_list.html',{})


def colaborador_list(request):
    return render(request, 'blog/animal_list.html',{})


def protectora_list(request):
    return render(request, 'blog/animal_list.html',{})