from django.shortcuts import render
#from third_app.models import User
from third_app.forms import NewUserForm
# Create your views here.

def index(request):
    users_dict = {'hello_message': 'Your Form has been Submitted'}
    return render(request, "form_app/index.html", context=users_dict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')
    return render(request, 'third_app/index.html', {'form':form})

def relative(request):
    return render(request, 'third_app/other.html')
