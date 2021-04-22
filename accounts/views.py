from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.forms import UserCreationForm   # A form that creates a user, from the given username and password.
from django.contrib.auth.decorators import login_required  
from .models import ProjectNames, UserTasks    # Models 
from django.contrib.auth.models import User    
# Create your views here. 

def indexView(request):         # method for home page
    return render(request,'index.html')

def registerView(request):      # Method for Signup
    if request.method=='POST':      
        form=UserCreationForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login_url')       # After successful signup redirect to login page
    else:
        form=UserCreationForm()      # If method is GET then show the empty Django UserCreationForm
    return render(request,'registration/register.html',{'form':form})      # render to register.html page with form data

@login_required
def dashboardView(request):
    list_of_projects=ProjectNames.objects.all()           # Fetch all projects

    if request.user.is_authenticated:                      # check user is authenticated or not
        print(request.user.id)
        username=User.objects.get(id=request.user.id)       # get the login user details from auth.User model
        list_of_task=UserTasks.objects.values('id','task_title','projects','start_time','end_time','status').all().filter(employee=username) # get the login user task details from Usertask model 
    if request.method=="POST":                               # when user submit the form (click on start button)
        if request.POST.get('start'):
            selected_project=get_object_or_404(ProjectNames,pk=request.POST.get('project_id'))   # get the selected project details
            task=UserTasks()                      # Create usertask model object
            task.employee=username                # insert the data 
            task.task_title=request.POST.get('name')
            task.projects=selected_project
            task.start_time = request.POST.get('start')
            task.save()
        else:                                
            print(request.POST.get('end'))  # when user end the task
            data=request.POST.get('end')  # it gives us this value(id,end_date) 20,2021-4-22 21:48:35
            if data:                       
                id,date=data.split(',')       # get the id and date
                task=UserTasks.objects.get(id=id)      # get the end task details
                task.end_time=date                     # set the end time and status false
                task.status=False                       
                task.save()

    return render(request,'dashboard.html',{'projects':list_of_projects,'tasks':list_of_task})   # render all the data(projects,tasks) to dashboard.html page

