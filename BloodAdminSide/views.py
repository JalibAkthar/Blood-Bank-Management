from django.shortcuts import render,redirect
from BloodAdminSide.models import DonarDB,RecipientDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

from BloodUserSide.models import ContactDB



# Create your views here.

def iindexx(request):
    return render(request,"iindexx.html")


# -------------------------------

def donar_page(request):
    return render(request,"Add_Donar.html")

def save_donar(request):
    if request.method =="POST":
        dn = request.POST.get('d_name')
        ag = request.POST.get('age')
        mb = request.POST.get('mobile')
        bg = request.POST.get('blood')
        qua = request.POST.get('quantity')
        em = request.POST.get('email')
        pl = request.POST.get('place')
        ad = request.POST.get('address')
        di = request.FILES['d_image']
        obj = DonarDB(Donar_Name=dn,Age=ag,Mobile=mb,Blood_Group=bg,Quantity=qua,Email=em,Place=pl,Address=ad,Profile_Image=di)
        obj.save()
        messages.success(request,"Donar Details Saved Successfully")
        return redirect(donar_page)

def display_donar(request):
    Donar = DonarDB.objects.all()
    return render(request,"Display_Donar.html",{'Donar':Donar})

def edit_donar(request,dataid):
    Donar = DonarDB.objects.get(id=dataid)
    # donar = DonarDB.objects.all()
    return render(request,"Edit_Donar.html",{'Donar':Donar})

def update_donar(request,dataid):
    if request.method =="POST":
        dn = request.POST.get('d_name')
        ag = request.POST.get('age')
        mb = request.POST.get('mobile')
        bg = request.POST.get('blood')
        qua = request.POST.get('quantity')
        em = request.POST.get('email')
        pl = request.POST.get('place')
        ad = request.POST.get('address')
        try:
            di = request.FILES['d_image']
            fs = FileSystemStorage()
            file = fs.save(di.name,di)
        except MultiValueDictKeyError:
            file = DonarDB.objects.get(id=dataid).Profile_Image
        DonarDB.objects.filter(id=dataid).update(Donar_Name=dn,Age=ag,Mobile=mb,Blood_Group=bg,Quantity=qua,Email=em,Place=pl,Address=ad,Profile_Image=file)
        messages.success(request,"Donar Details Updated Successfully")
        return redirect(display_donar)

def delete_donar(request,dataid):
    Donar = DonarDB.objects.filter(id=dataid)
    Donar.delete()
    messages.error(request, "Donar Details Deleted Successfully")
    return redirect(display_donar)

# ----------------------------

def recipient_page(request):
    return render(request,"Add_Recipient.html")

def save_recipient(request):
    if request.method =="POST":
        rn = request.POST.get('r_name')
        age = request.POST.get('r_age')
        mob = request.POST.get('r_mobile')
        bgrp = request.POST.get('r_blood')
        qt = request.POST.get('r_quantity')
        dat = request.POST.get('r_date')
        email = request.POST.get('r_email')
        plc = request.POST.get('r_place')
        add = request.POST.get('r_address')
        ri = request.FILES['r_image']
        obj = RecipientDB(Recipient_Name=rn,R_Age=age,R_Mobile=mob,R_Blood_Group=bgrp,R_Quantity=qt,R_Date=dat ,R_Email=email,R_Place=plc,R_Address=add,R_Profile_Image=ri)
        obj.save()
        messages.success(request,"Recipient Details Saved Successfully")
        return redirect(recipient_page)


def display_recipient(request):
    Recipient = RecipientDB.objects.all()
    return render(request,"Display_Recipient.html",{'Recipient':Recipient})

def edit_recipient(request,dataid):
    Recipient = RecipientDB.objects.get(id=dataid)
    # recipient = RecipientDB.objects.all()
    return render(request,"Edit_Recipient.html",{'Recipient':Recipient})

def update_recipient(request,dataid):
    if request.method =="POST":
        rn = request.POST.get('r_name')
        age = request.POST.get('r_age')
        mob = request.POST.get('r_mobile')
        bgrp = request.POST.get('r_blood')
        qt = request.POST.get('r_quantity')
        dat = request.POST.get('r_date')
        email = request.POST.get('r_email')
        plc = request.POST.get('r_place')
        add = request.POST.get('r_address')
        try:
            ri = request.FILES['r_image']
            fs = FileSystemStorage()
            file = fs.save(ri.name,ri)
        except MultiValueDictKeyError:
            file = RecipientDB.objects.get(id=dataid).R_Profile_Image
        RecipientDB.objects.filter(id=dataid).update(Recipient_Name=rn,R_Age=age,R_Mobile=mob,R_Blood_Group=bgrp,R_Quantity=qt,R_Date=dat,R_Email=email,R_Place=plc,R_Address=add,R_Profile_Image=file)
        messages.success(request, "Recipient Details Updated Successfully")
        return redirect(display_recipient)


def delete_recipient(request,dataid):
    Recipient = RecipientDB.objects.filter(id=dataid)
    Recipient.delete()
    messages.error(request, "Recipient Details Deleted Successfully")
    return redirect(display_recipient)

# -----------------

def adminlogin_page(request):
    return render(request,"Admin_Login.html")

def adminlogin_save(request):
    if request.method =="POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un,password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(iindexx)
            else:
                return redirect(adminlogin_page)
        else:
            return redirect(adminlogin_page)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin_page)

def display_contact(request):
    contact = ContactDB.objects.all()
    return render(request,"View_Contact.html",{'contact':contact})

def delete_contact(request,dataid):
    Cont = ContactDB.objects.filter(id=dataid)
    Cont.delete()
    # messages.error(request, "Recipient Details Deleted Successfully")
    return redirect(display_contact)