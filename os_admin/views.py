import json
import random
from django.contrib import messages
from django.shortcuts import render, redirect
from os_admin.models import AdminLogin, Agent
from Online_Sales import sendMessage
from os_agent.models import Property
from os_client.models import Client

def os_admin_login_check(request):
    if request.method == 'POST':
        contact = request.POST.get("contact")
        password = request.POST.get("pass")
        try:
            result = AdminLogin.objects.get(a_contact_no=contact, a_password=password)
            a_otp = random.randint(100000,999999)
            result.a_otp= a_otp
            result.save()
            message = "Hello Admin this is your one time password : " + str(a_otp)
            d1 = sendMessage.sendACASMS(contact, message)
            print(d1)
            # dd = json.loads(d1)
            # if dd["return"]:
            if d1:
                return render(request, "os_admin_template/os_admin_otp.html")
            else:
                return render(request, "os_admin_template/os_admin_home.html", {"error": "Sorry Unable to send OTP"})
        except:
            messages.error(request, "Invalid User")
            return render(request, "os_admin_template/os_admin_home.html")
    else:
        return render(request, "os_admin_template/os_admin_home.html")

def os_admin_welcome_page(request):
    if request.method == "POST":
        check_otp = request.POST.get("otp_pass")
        result = AdminLogin.objects.get(a_otp=check_otp)
        request.session["status"] = True
        qs = Agent.objects.all()
        if result:
            return render(request, "os_admin_template/os_admin_welcome_page.html", {"data":qs})
        else:
            return render(request, 'os_admin_template/os_admin_home.html', {"message": "Invalid OTP"})
    else:
        return render(request, 'os_admin_template/os_admin_home.html', {"message": "Invalid OTP"})

def os_admin_logout(request):
    request.session["status"] = False
    return render(request, "os_admin_template/os_admin_home.html")

def os_admin_agent_registration(request):
    qs = Agent.objects.all()
    ws = AdminLogin.objects.all()
    return render(request, "os_admin_template/os_admin_agent_registration.html", {"data":qs, "data1":ws})

def os_admin_save_agent(request):
    agent_no = request.POST.get("agent_no")
    agent_name = request.POST.get("agent_name")
    agent_photo = request.FILES["agent_photo"]
    agent_address = request.POST.get("agent_address")
    agent_contact = request.POST.get("agent_contact")
    agent_username = request.POST.get("agent_username")
    agent_password = request.POST.get("agent_password")
    agent_otp = 12345
    Agent(ag_no=agent_no, ag_name=agent_name, ag_photo=agent_photo, ag_address=agent_address, ag_contact_no=agent_contact,ag_username=agent_username,ag_password=agent_password, ag_otp=agent_otp).save()
    qs = Agent.objects.all()
    return render(request, "os_admin_template/os_admin_agent_registration.html", {"data":qs})

def os_admin_agent_delete(request):
    idno = request.GET.get("idno")
    Agent.objects.filter(ag_no=idno).delete()
    qs = Agent.objects.all()
    return redirect('/osadmin/os_admin_agent_registration/')

def os_admin_agent_update(request):
    username = request.POST.get("username")
    result = Agent.objects.filter(ag_username=username)
    return render(request, "os_admin_template/os_admin_agent_update.html", {"data":result})

def os_admin_welcome_home(request):
    qs = AdminLogin.objects.all()
    return render(request, "os_admin_template/os_admin_welcome_home.html", {"data":qs})

def os_admin_view_property(request):
    qs = Property.objects.filter(p_status="post")
    ws = AdminLogin.objects.all()
    return render(request, "os_admin_template/os_admin_view_property.html", {"data":qs, "data1":ws})

def os_admin_view_client(request):
    qs = Client.objects.all()
    ws = AdminLogin.objects.all()
    return render(request, "os_admin_template/os_admin_view_client.html", {"data":qs, "data1":ws})

def os_admin_view_client_delete(request):
    c_un = request.GET.get("c_un")
    qs = Client.objects.filter(c_username=c_un).delete()
    return redirect('/osadmin/os_admin_view_client/', {"data":qs})

def os_admin_about_us(request):
    qs = AdminLogin.objects.all()
    return render(request, "os_admin_template/os_admin_about_us.html", {"data":qs})

