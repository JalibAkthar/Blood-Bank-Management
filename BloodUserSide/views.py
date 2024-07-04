from django.shortcuts import render,redirect
from BloodAdminSide.models import DonarDB,RecipientDB
from BloodUserSide.models import ContactDB,LoginDB
from django.contrib import messages


# Create your views here.

def home_page(request):
    return render(request,"Home.html")

def donar__page(request):
    donar = DonarDB.objects.all()
    blood = request.POST.get('search_don')
    if blood:
        donar = donar.filter(Blood_Group__icontains=blood)
    loct = request.POST.get('don_loct')
    if loct:
        donar = donar.filter(Place__icontains=loct)
    return render(request,"Donar.html",{'donar':donar,'blood':blood,'loct':loct})

def about_page(request):
    return render(request,"About.html")

def recipient__page(request):
    rec = RecipientDB.objects.all()
    bld = request.POST.get('search_rec')
    if bld:
        rec = rec.filter(R_Blood_Group__icontains=bld)
    loc = request.POST.get('rec_loc')
    if loc:
        rec = rec.filter(R_Place__icontains=loc)
    return render(request,"Recipient.html",{'rec':rec,'bld':bld,'loc':loc})


def single_page(request,recid):
    single = RecipientDB.objects.get(id=recid)
    return render(request,"Single_Recpient.html",{'single':single})

def single_donar(request,donarid):
    sing = DonarDB.objects.get(id=donarid)
    return render(request,"Single_Donar.html",{'sing':sing})


# ---------------
def adding_donar(request):
    return render(request,"Adding_Donar.html")

def donar_save(request):
    if request.method =="POST":
        dn = request.POST.get('d_name')
        ag = request.POST.get('age')
        mb = request.POST.get('mobile')
        bg = request.POST.get('blood')
        em = request.POST.get('email')
        pl = request.POST.get('place')
        ad = request.POST.get('address')
        di = request.FILES['d_image']
        obj = DonarDB(Donar_Name=dn,Age=ag,Mobile=mb,Blood_Group=bg,Email=em,Place=pl,Address=ad,Profile_Image=di)
        obj.save()
        messages.success(request,"Donar Details Saved Successfully")
        return redirect(donar__page)



def adding_recipient(request):
    return render(request,"Adding_Recipient.html")

def recipient_save(request):
    if request.method =="POST":
        rn = request.POST.get('r_name')
        age = request.POST.get('r_age')
        mob = request.POST.get('r_mobile')
        bgrp = request.POST.get('r_blood')
        dat = request.POST.get('r_date')
        email = request.POST.get('r_email')
        plc = request.POST.get('r_place')
        add = request.POST.get('r_address')
        ri = request.FILES['r_image']
        obj = RecipientDB(Recipient_Name=rn,R_Age=age,R_Mobile=mob,R_Blood_Group=bgrp,R_Date=dat,R_Email=email,R_Place=plc,R_Address=add,R_Profile_Image=ri)
        obj.save()
        messages.success(request,"Recipient Details Saved Successfully")
        return redirect(recipient__page)

    # --------
def contact_page(request):
    return render(request,"Contact.html")

def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        mob = request.POST.get('mobile')
        em = request.POST.get('email')
        add = request.POST.get('address')
        sub = request.POST.get('subject')
        obj = ContactDB(Name=na,Mobile=mob,Email=em,Address=add,Subject=sub)
        obj.save()
        return redirect(contact_page)




# ----------
def login_page(request):
    return render(request,"Login.html")

def save_signup(request):
    if request.method =="POST":
        ln = request.POST.get('up_name')
        le = request.POST.get('up_email')
        lp = request.POST.get('up_pass')
        mob = request.POST.get('up_mob')
        obj = LoginDB(L_Name=ln,L_Email=le,L_Password=lp,L_Mobile=mob)
        obj.save()
        return redirect(login_page)

def Signin_check(request):
    if request.method =="POST":
        em = request.POST.get('email')
        pas = request.POST.get('password')

        if LoginDB.objects.filter(L_Email=em,L_Password=pas).exists():
            request.session['L_Email'] = em
            request.session['L_Password'] = pas
            return redirect(home_page)
        else:
            return redirect(login_page)
    return redirect(login_page)


def logout(request):
    del request.session['L_Email']
    del request.session['L_Password']
    return redirect(login_page)