import random
from django.shortcuts import render, redirect
from rest_framework.utils import json
from Online_Sales import sendMessage
from os_admin.models import Agent
from os_agent.models import Property, BlockProperty, SoldProperty

def os_agent_login_check(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("pass")
        try:
            result = Agent.objects.get(ag_username=username, ag_password=password)
            request.session['username'] = username
            contact_fsms = result.ag_contact_no
            ag_otp = random.randint(100000,999999)
            result.ag_otp = ag_otp
            result.save()
            message = "Hello Agent this is your one time password : " + str(ag_otp)
            d1 = sendMessage.sendACASMS(str(contact_fsms), message)
            dd = json.loads(d1)
            if dd["return"]:
                return render(request, "os_agent_template/os_agent_otp.html")
            else:
                return render(request, "os_agent_template/os_agent_home.html", {"error": "Sorry Unable to send OTP"})
        except:
            from django.contrib import messages
            messages.error(request, "Invalid User")
            return render(request, "os_agent_template/os_agent_home.html")
    else:
        return render(request, "os_agent_template/os_agent_home.html")

def os_agent_welcome_page(request):
    if request.method == "POST":
        check_otp = request.POST.get("otp_pass")
        result = Agent.objects.get(ag_otp=check_otp)
        if result:
            request.session["status"] = True
            return render(request, "os_agent_template/os_agent_welcome_page.html")
        else:
            return render(request, 'os_agent_template/os_agent_home.html', {"message": "Invalid OTP"})
    else:
        return render(request, 'os_agent_template/os_agent_home.html', {"message": "Invalid OTP"})

def os_agent_new_properties(request):
    qs = Property.objects.all()
    un = request.session['username']
    ws = Agent.objects.filter(ag_username=un)
    return render(request, "os_agent_template/os_agent_new_properties.html", {"data":qs, "data1":ws})

def os_agent_save_property(request):
    pname = request.POST.get("pname")
    plocation = request.POST.get("plocation")
    psize = request.POST.get("psize")
    pprice = request.POST.get("pprice")
    pfacing = request.POST.get("pfacing")
    pcomment = request.POST.get("pcomment")
    pphoto = request.FILES["pphoto"]
    pstatus = "post"
    p_agent_un_id = request.session["username"]
    Property(p_name=pname, p_location=plocation, p_size=psize, p_prize=pprice, p_facing=pfacing, p_comment=pcomment, p_photo=pphoto, p_status=pstatus, p_agent_un_id=p_agent_un_id).save()
    # qs = Property.objects.filter(p_agent_un_id=p_agent_un_id)
    qs = Property.objects.all()
    return redirect('/osagent/os_agent_new_properties/')

def os_agent_property_delete(request):
    pno = request.GET.get("pno")
    Property.objects.filter(p_no=pno).delete()
    qs = Property.objects.all()
    return redirect('/osagent/os_agent_new_properties/')


def os_agent_property_update(request):
    pno = request.POST.get("pno")
    result = Property.objects.filter(p_no=pno)
    return render(request, "os_agent_template/os_agent_property_update_save.html", {"data": result})

def os_agent_block_property(request):
    p_agent_un_id = request.session['username']
    qs = Property.objects.filter(p_agent_un_id = p_agent_un_id, p_status="post")
    list = []
    ws =Agent.objects.filter(ag_username=p_agent_un_id)
    for x in qs:
        list.append(BlockProperty.objects.filter(b_property_no_id = x.p_no))
    return render(request, "os_agent_template/os_agent_block_property.html", {"data": list, "data1":ws})

def os_agent_sold_property(request):
    p_no = request.GET.get("p_no")
    client_un = request.GET.get("client_un")
    qs=SoldProperty(s_property_no_id = p_no, s_client_un_id = client_un).save()
    Property.objects.filter(p_no=p_no).update(p_status="sold")
    return render(request, "os_agent_template/os_agent_view_sold_property.html")

def os_agent_logout(request):
    request.session['status'] = False
    return render(request, "os_agent_template/os_agent_home.html")

def os_agent_property_update_confirm(request):
    pno = request.POST.get("pno")
    pname = request.POST.get("pname")
    plocation = request.POST.get("plocation")
    psize = request.POST.get("psize")
    pprice = request.POST.get("pprice")
    pfacing = request.POST.get("pfacing")
    pcomment = request.POST.get("pcomment")
    p_add_dt = request.POST.get("p_add_dt")
    p_agent_un_id = request.session['username']
    pphoto = request.FILES["pphoto"]
    pstatus = "post"
    p_agent_un_id = request.session["username"]
    Property.objects.filter(p_no=pno).delete()
    Property(p_name=pname, p_location=plocation, p_size=psize, p_prize=pprice, p_facing=pfacing, p_comment=pcomment,
             p_photo=pphoto, p_status=pstatus, p_agent_un_id=p_agent_un_id).save()
    qs = Property.objects.all()
    return redirect('/osagent/os_agent_new_properties/', {"data":qs})

def os_agent_view_sold_property(request):
    p_agent_un = request.session['username']
    qs = Property.objects.filter(p_agent_un_id=p_agent_un, p_status="sold")
    ws = Agent.objects.filter(ag_username=p_agent_un)
    # sd=SoldProperty.objects.all()
    return render(request, "os_agent_template/os_agent_view_sold_property.html", {"data":qs, "data1":ws})

def os_agent_welcome_home_page(request):
    username = request.session['username']
    qs = Agent.objects.filter(ag_username=username)
    return render(request, "os_agent_template/os_agent_welcome_home_page.html", {"data":qs})


def os_agent_sold_delete(request):
    pno = request.GET.get('pno')
    Property.objects.filter(p_no=pno).delete()
    qs = SoldProperty.objects.filter(s_property_no_id=pno)
    return render(request, 'os_agent_template/os_agent_view_sold_property.html', {"data":qs})






