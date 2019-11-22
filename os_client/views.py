import random
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.utils import json
from Online_Sales import sendMessage
from os_agent.models import Property, BlockProperty
from os_client.models import Client
from django.db import IntegrityError


def os_client_detail_save(request):
    c_name = request.POST.get("c_name")
    c_contact_no = request.POST.get("c_contact_no")
    c_address = request.POST.get("c_address")
    c_username = request.POST.get("c_username")
    c_password = request.POST.get("c_password")
    c_photo = request.FILES["c_photo"]
    c_otp = 12345
    Client(c_name=c_name, c_contact_no=c_contact_no, c_address=c_address, c_username=c_username,
           c_password=c_password, c_photo=c_photo,c_otp=c_otp).save()
    qs = Client.objects.all()
    msg = "Hi " + c_name + "Your are Register."
    return render(request, "os_client_template/os_client_home.html", {"data":qs, "message": msg})


def os_client_login_check(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass")
        try:
            result = Client.objects.get(c_username=username, c_password=password)
            request.session['username'] = username
            contact_fsms = result.c_contact_no
            c_otp = random.randint(100000,999999)
            result.c_otp = c_otp
            result.save()
            message = ("Hello " + username + " this is your one time password for client Login: " + str(c_otp))
            d1 = sendMessage.sendACASMS(str(contact_fsms), message)
            dd = json.loads(d1)
            if dd["return"]:
                return render(request, "os_client_template/os_client_otp.html")
            else:
                return render(request, "os_client_template/os_client_home.html", {"error": "Sorry Unable to send OTP"})
        except:
            from django.contrib import messages
            messages.error(request, "Invalid User")
            return render(request, "os_client_template/os_client_home.html")
    else:
        return render(request, "os_client_template/os_client_home.html")


def os_client_otp_check(request):
    if request.method == "POST":
        check_otp = request.POST.get("otp_pass")
        result = Client.objects.filter(c_otp=check_otp)
        qs = Client.objects.all()
        if result:
            request.session["status"] = True
            return render(request, "os_client_template/os_client_welcome_page.html", {"data":qs})
        else:
            return render(request, 'os_client_template/os_client_home.html', {"message": "Invalid OTP"})
    else:
        return render(request, 'os_client_template/os_client_home.html', {"message": "Please Change Your Method, it's not Secure."})


def os_client_view_properties(request):
    qs = Property.objects.filter(p_status="post")
    un = request.session['username']
    ws = Client.objects.filter(c_username=un)
    return render(request, "os_client_template/os_client_view_properties.html", {"data":qs, "data1":ws})

def os_client_property_block(request):
    uname = request.GET.get("uname")
    pno = request.GET.get("pno")
    qs = BlockProperty.objects.filter(b_client_un_id=uname, b_property_no_id=pno)
    if qs:
        messages.info(request, "Blocked Property")
        qs = Property.objects.all()
        return render(request, "os_client_template/os_client_view_properties.html", {"data": qs})
    else:
        BlockProperty(b_client_un_id=uname, b_property_no_id=pno).save()
        ws = BlockProperty.objects.filter(b_client_un_id=uname)
        qs = Client.objects.all()
        return render(request, "os_client_template/os_client_property_blocked.html", {"data": ws, "data1":qs})

def os_client_unblock_property(request):
    uname = request.GET.get("uname")
    pno = request.GET.get("pno")
    BlockProperty.objects.filter(b_client_un_id=uname, b_property_no_id=pno).delete()
    ws = BlockProperty.objects.filter(b_client_un_id=uname)
    return render(request, "os_client_template/os_client_property_blocked.html", {"data": ws})

def os_client_blocked_properties(request):
    uname = request.session['username']
    ws = BlockProperty.objects.filter(b_client_un_id=uname)
    qs = Client.objects.filter(c_username=uname)
    return render(request, "os_client_template/os_client_property_blocked.html", {"data": ws, "data1":qs})

def os_client_home(request):
    request.session['status'] = False
    return render(request, "os_client_template/os_client_home.html")

def os_client_welcome_home(request):
    un = request.session['username']
    qs = Client.objects.filter(c_username=un)
    return render(request, "os_client_template/os_client_welcome_page.html", {"data":qs})
