from django.shortcuts import render,redirect,get_object_or_404
from .forms import CandidateForm,VotersForm
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages



def home(request):
    return render(request,'base/home.html')


@login_required(login_url='login')
def candidate_register(request):
    submitted=False
    if request.method=='POST':
        form=CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/can-register?submitted=True')
    else:
        form=CandidateForm()
        if 'submitted' in request.GET:
            submitted=True

    context={'form':form,'submitted':submitted}
    return render(request,'base/candidate_register.html',context)


@login_required(login_url='login')
def candidate(request):
    candidates=Candidate.objects.all()
    context={'candidates':candidates}
    return render(request,'base/candidate.html',context)


@login_required(login_url='login')
def candidate_profile(request,pk):
    profile=Candidate.objects.get(id=pk)
    context={'profile':profile}
    return render (request,'base/candidate_profile.html',context)


@login_required(login_url='login')
def update_candidate(request,pk):
    candidate=Candidate.objects.get(id=pk)
    form=CandidateForm(request.POST or None,instance=candidate)
    if form.is_valid():
        form.save
        return redirect('/candidate')

    context={'form':form,'candidate':candidate}
    return render(request,'base/candidate_update.html',context)


@login_required(login_url='login')
def voter_register(request):
    submitted=False
    if request.method=='POST':
        form=VotersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/voter-register?submitted=True')
    else:
        form=VotersForm()
        if 'submitted' in request.GET:
            submitted=True

    context={'form':form,'submitted':submitted}
    return render(request,'base/voter_register.html',context)



@login_required(login_url='login')
def voter_list(request):
    voters=Voters.objects.all()
    context={'voters':voters}
    return render(request,'base/voter_list.html',context)



def voter_details(request,pk):
    details=Voters.objects.get(id=pk)
    context={'details':details}
    return render(request,'base/voter_details.html',context)



@login_required(login_url='login')
def update_voter(request,pk):
    voter=Voters.objects.get(id=pk)
    form=VotersForm(request.POST or None,instance=voter)
    if form.is_valid():
        form.save()
        messages.success(request,"Successfully updated")
        return redirect('/voter-list')

    context={'form':form,'voter':voter}
    return render(request,'base/voter_update.html',context)


@login_required(login_url='login')
def position(request):
    pos=Position.objects.all()
    context={'pos':pos}
    return render(request,'base/position.html',context)


@login_required(login_url='login')
def position_candidate(request, pk):
    obj = get_object_or_404(Position, id=pk)
    profile=Candidate.objects.all()

    if request.method == "POST":
        temp = ControlVote.objects.get_or_create(voter=request.user, position=obj)[0]
        if temp.status == False:
            temp2 = Candidate.objects.get(id=request.POST.get(obj.title))
            temp2.total_vote += 1
            temp2.save()
            temp.status = True
            temp.save()
            return redirect('/position/')
        else:
            messages.success(request, 'You Have Already Been Voted For This Position.')
            return render(request, 'base/position_details.html', {'obj':obj,'profile':profile})
    else:
        return render(request, 'base/position_details.html', {'obj':obj,'profile':profile})


@login_required(login_url='login')
def results(request):
    results = Candidate.objects.all().order_by('position','-total_vote')
    context={'results':results}
    return render(request,'base/result.html',context)
