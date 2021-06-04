from django.shortcuts import redirect, render
from .models import Job
from django.core.paginator import Paginator
from .forms import Apply_form, AddJobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def job_list(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'jobs': page_obj,
        'all_jobs': job_list
    }

    return render(request, 'job/job_list.html', context)


def job_detail(request, slug):
    job_detail = Job.objects.get(slug = slug)
    if request.method == 'POST':
        form = Apply_form(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            form = Apply_form()

    else :
        form = Apply_form()

    context = {
        'job' : job_detail,
        'form': form
    }
    return render(request,'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST, request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            form = AddJobForm()
            return redirect(reverse('jobs:job_list'))
    else :
        form = AddJobForm()

    context = {'form':form}
    return render(request, 'job/add_job.html', context)