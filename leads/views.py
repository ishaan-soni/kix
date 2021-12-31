
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class= CustomUserCreationForm


    def get_success_url(self):
        return reverse('login')
        

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"

class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

class LeadCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self): #after form saved successfully 
        return reverse('leads:lead-list')
    

    def form_valid(self, form):
        #configure email setting in settings.py
        send_mail(
            subject="A lead has been created",
            message="Check out the new lead",
            from_email="test@test.com",
            recipient_list=["189ishaan@gmail.com"],

        )

        return super(LeadCreateView, self).form_valid(form) #continues with form_valid after finishing desired task. Override to add something in bw
    

class LeadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self): #after form saved successfully 
        return reverse('leads:lead-list')
    

class LeadDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/lead_delete.html" # need to provide templates for CBVs
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse('leads:lead-list')






# def landing_page(request):
#     return render(request,'landing.html')

# def lead_list(request):
#     #return HttpResponse("HE")
#     #return render(request,"leads/home_page.html")
#     leads = Lead.objects.all()
#     context = {
#        "leads" : leads
#     }
#     return render(request, "leads/lead_list.html",context)

# def lead_detail(request,pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }

#     return render(request,"leads/lead_detail.html",context)

# def lead_create(request):
#     form = LeadModelForm()       #assign empty leadform if request is not post 
#     if request.method == "POST":
#         # print("receiving post")
#         form = LeadModelForm(request.POST)   #pass request data in form
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         "form": form #changes to whichever form it is depeneding on method.
#     }
#     return render(request,"leads/lead_create.html",context)

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)#updates specific instance instead of creating another
#     if request.method =="POST":
#         form = LeadModelForm(request.POST,instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')
#     context = {
#         'form':form,
#         'lead':lead
#     }
#     return render(request,'leads/lead_update.html',context)

# def lead_delete(request, pk):
    # lead = Lead.objects.get(id=pk)
    # lead.delete()
    # return redirect('/leads')
    





















# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()       #assign empty leadform if request is not post 
#     if request.method == "POST":
        
#         form = LeadForm(request.POST)   #pass request data in form
#         if form.is_valid():
            
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect('/leads')
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, 'leads/lead_update.html',context)


    # def lead_create(request):
    # form = LeadForm()       #assign empty leadform if request is not post 
    # if request.method == "POST":
    #     # print("receiving post")
    #     form = LeadForm(request.POST)   #pass request data in form
    #     if form.is_valid():
    #         print("Form is valid")
    #         print(form.cleaned_data)
    #         first_name = form.cleaned_data['first_name']
    #         last_name = form.cleaned_data['last_name']
    #         age = form.cleaned_data['age']
    #         agent = form.cleaned_data['agent']
    #         #agent = Agent.objects.first()
    #         Lead.objects.create(
    #             first_name=first_name,
    #             last_name=last_name,
    #             age=age,
    #             agent=agent
    #         )
    #         # print("lead created")
    #         return redirect('/leads')
    # context = {
    #     "form": form #changes to whichever form it is depeneding on method.
    # }
    # return render(request,"leads/lead_create.html",context)
