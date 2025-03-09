from django.shortcuts import render ,redirect
from tv_show_app.models import * 
from django.contrib import messages

# the first function to redirct to shows :*****************
def index(request):
    return redirect('shows')


# this function views all the shows in database : **************
def shows(request):
    context = {
        'tv_shows':tv_show.objects.all()
    }
    return render(request,'shows.html',context)


# this function to see the selected show :**********************
def view_show(request,show_id):
    selected = tv_show.objects.get(id=show_id)
    if request.method == 'POST':
        erorrs = tv_show.objects.validate(request.POST)
        if len(erorrs) > 0 :
            print(erorrs)
            for key,value in erorrs.items():
                messages.error(request,value)
                return redirect('edit',show_id)
        else:
            title_from_form = request.POST['title']
            network_from_form = request.POST['network']
            created_from_form = request.POST['date']
            desc_from_form = request.POST['desc']
            selected.title= title_from_form
            selected.network= network_from_form
            selected.release_date= created_from_form
            selected.desc = desc_from_form
            selected.save()
        context = {
            'selected':selected
        }
    return render(request,'selected_show.html',context)


# this function to edit the selected show in database :*******************
def edit(request,show_id):
    selected = tv_show.objects.get(id=show_id)
    context = {
        'selected':selected
    }
    return render(request,'edit.html',context)


# this function to delete the selected show from database :**************
def delete(request,show_id):
    selected = tv_show.objects.get(id= show_id)
    selected.delete()
    selected.save()
    return redirect('/')


# this function to create a new show and save it to database :****************
def new_show(request):
    if request.method == 'POST':
        erorrs = tv_show.objects.validate(request.POST)
        if len(erorrs) > 0 :
            print(erorrs)
            for key,value in erorrs.items():
                messages.error(request,value)
                return redirect('new_show')
        else:
            title_from_form = request.POST['title']
            network_from_form = request.POST['network']
            create_from_form = request.POST['date'] 
            desc_from_form = request.POST['desc']
            tv_show.objects.create(title = title_from_form, network = network_from_form,release_date = create_from_form,desc = desc_from_form)
            return redirect('/')
    return render(request,'new_show.html')

# Create your views here.
