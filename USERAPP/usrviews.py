from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
import MySQLdb
import random
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
import smtplib 
import urllib.request
import webbrowser
from django.contrib import messages
from datetime import date
from datetime import datetime
import datetime
import csv
import os
import time

def sendmail(toadd,msg):

    #create smtp session
    s = smtplib.SMTP('smtp.gmail.com',587)

    #start TLS for security
    s.starttls()

    #Authentication
    s.login("domiorentalportofficial@gmail.com","domio123456")

    #Message you need to be send
    
    #Sending the mail
    s.sendmail("domiorentalportofficial@gmail.com",toadd,msg)

    #terminating the session
    s.quit()
    
def sendsms(ph,msg):

    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=sendMessage&send_to=" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

# Create your views here.
con=MySQLdb.connect("localhost","root","","House_Price_Predict")
c=con.cursor()

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/login/')
def usrhome(request):
    uid=request.session["uname"]      
    print(uid)
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro where description like '%"+search+"%'"
      c.execute(s)
      data=c.fetchall()
      print(s)
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where id='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    return render(request,"usrhome.html",{"uid":uid,"data":data,"data1":data1,"data3":data3,"data5":data5})


def register(request):
    return render(request,"register.html")

def vendorreg(request):
    vend_id=random.randrange(10000,1000000,3)
    role="Vendor"
    alert=" "
    
    if "b1" in request.POST: 
        print("***************pppppppppppppppppp******************************************************")
        first_name=request.POST.get("t1")
        last_name=request.POST.get("t2")
        email=request.POST.get("t3")
        Address=request.POST.get("t4")
        location=request.POST.get("t5")
        gender=request.POST.get("r1")
        password=request.POST.get("t6")
        retypepassword=request.POST.get("t7")
        ss="select count(*) from vendreg where email='"+str(email)+"'"
        c.execute(ss)
        s=c.fetchone()
        print(s)
        if(s[0]==0):
            s="insert into vendreg (`First_Name`,`Last_Name`,`email`,`address`,`location`,`gender`,`password`,`retypepassword`,`vend_id`) values('"+first_name+"','"+last_name+"','"+email+"','"+Address+"','"+location+"','"+str(gender)+"','"+password+"','"+retypepassword+"','"+str(vend_id)+"')"
            c.execute(s)


            con.commit()
            print("*********************************************************************")
            print("insert into vendreg values('"+first_name+"','"+last_name+"','"+email+"','"+Address+"','"+location+"','"+str(gender)+"','"+password+"','"+retypepassword+"','"+str(vend_id)+"')")
            log="insert into login values('"+str(vend_id)+"','"+password+"','"+str(role)+"','"+str(email)+"','"+str(first_name)+"','registred')"
            c.execute(log)
            con.commit()
            return HttpResponseRedirect("/usrlogin")
        else:
            alert="Invalid User Name  Or Password"
    return render(request,"vendorreg.html",{"vend_id":vend_id,"alert":alert})       
def customerreg(request):
    cust_id=random.randrange(10000,1000000,3)
    role="Customer"
    if request.POST.get("b1"):
        first_name=request.POST.get("t1")
        last_name=request.POST.get("t2")
        email=request.POST.get("t3")
        Address=request.POST.get("t4")
        location=request.POST.get("t5")
        gender=request.POST.get("r1")
        password=request.POST.get("t6")
        retypepassword=request.POST.get("t7")
        s="insert into custreg values('"+first_name+"','"+last_name+"','"+email+"','"+Address+"','"+location+"','"+str(gender)+"','"+password+"','"+retypepassword+"','"+str(cust_id)+"')"
        c.execute(s)
        con.commit()
        log="insert into login values('"+str(cust_id)+"','"+password+"','"+str(role)+"','"+str(email)+"','"+str(first_name)+"','approved')"
        c.execute(log)
        con.commit()
        return HttpResponseRedirect("/usrlogin")
    return render(request,"customerreg.html",{"cust_id":cust_id})

def guest(request):
    gust_id=random.randrange(10000,1000000,3)
    role="Guest"
    first_name="guest"
    if request.POST.get("b1"):
        email=request.POST.get("t1")
        password=request.POST.get("t2")
        retypepassword=request.POST.get("t3")
        s="insert into guestreg values('"+email+"','"+password+"','"+retypepassword+"','"+str(gust_id)+"')"
        c.execute(s)
        con.commit()
        log="insert into login values('"+str(gust_id)+"','"+password+"','"+str(role)+"','"+str(email)+"','"+str(first_name)+"','approved')"
        c.execute(log)
        con.commit()
        return HttpResponseRedirect("/usrlogin")
    return render(request,"guest.html",{"gust_id":gust_id})
@cache_control(no_cache=True, must_revalidate=True)
def usrlogin(request):
    alert=" "
    try:
        if(request.POST.get("b1")):
            username=request.POST.get("t1")
            password=request.POST.get("t2")

            check="select * from login where email='"+username+"' and password='"+password+"'"
            c.execute(check)
            con.commit()
            data=c.fetchone()
            if(data[2]=="admin"):
                return HttpResponseRedirect("/home")
            
            elif(data[3]==username and data[1]==password):
                request.session["uname"]=username
                request.session["pwd"]=password
                a=request.session["uname"]
                print(a)
                b=request.session["pwd"]
                print(b)
                return HttpResponseRedirect("/photogallery")
            
    except:
        alert="Invalid User Name  Or Password"
    return render(request,"usrlogin.html",{"alert":alert})

def product(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    return render(request,"product.html",{"uid":uid,"data1":data1[0],"data3":data3,"data5":data5})

# def addproduct(request):
#     uid=request.session["uname"]
#     password=request.session["pwd"]
#     s="select count(*) from addpro where email='"+str(uid)+"'"
#     c.execute(s)
#     data1 = c.fetchone()
#     print(data1)
#     paid="not paid"
#     l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
#     c.execute(l)
#     data3=c.fetchall()
#     y="select files from account where email='"+str(uid)+"'"
#     c.execute(y)
#     data5=c.fetchone()
#     pdt_id=random.randrange(100,1000,5)
#     date=""
#     time=""
#     ms=""
#     if (request.POST.get("submit")=="ADD"):
#         pdtname=request.POST.get("t1")
#         pdttype=request.POST.get("t2")
#         description=request.POST.get("t3")
#         startdate=request.POST.get("t4")
#         enddate=request.POST.get("t5")
#         myfile = request.FILES["t6"]
#         fs = FileSystemStorage()        
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         location=request.POST.get("t7")
#         phno=request.POST.get("t10")
#         price=request.POST.get("t11")
#         time=datetime.datetime.now()
#         print(time)
#         s="insert into addpro values('"+str(pdtname)+"','"+str(pdttype)+"','"+str(description)+"','"+str(startdate)+"','"+str(enddate)+"','"+str(filename)+"','"+str(location)+"','"+str(uid)+"','"+str(password)+"','"+str(phno)+"','"+str(pdt_id)+"','"+str(price)+"','"+str(time)+"')"
#         c.execute(s)
#         con.commit()
#         ms="Added Your House Successfully!...."
#     return render(request,"addproduct.html",{"uid":uid,"password":password,"pdt_id":pdt_id,"data1":data1[0],"data3":data3,"data5":data5,"ms":ms})
 
def addproduct(request):
    uid=request.session["uname"]
    password=request.session["pwd"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    pdt_id=random.randrange(100,1000,5)
    date=""
    time=""
    ms=""
    if (request.POST.get("submit")=="ADD"):
        pdtname=request.POST.get("t1")
        pdttype=request.POST.get("t2")
        description=request.POST.get("t3")
        startdate=request.POST.get("t4")
        enddate=request.POST.get("t5")
        myfile = request.FILES["t6"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        location=request.POST.get("t7")
        phno=request.POST.get("t10")
        price=request.POST.get("t11")
        time=datetime.datetime.now()
        print(time)
        # price=pricepredict(description,price)
        s="insert into addpro values('"+str(pdtname)+"','"+str(pdttype)+"','"+str(description)+"','"+str(startdate)+"','"+str(enddate)+"','"+str(filename)+"','"+str(location)+"','"+str(uid)+"','"+str(password)+"','"+str(phno)+"','"+str(pdt_id)+"','"+str(price)+"','"+str(time)+"')"
        c.execute(s)
        con.commit()
        ms="Added Your House Successfully!...."
    return render(request,"addproduct.html",{"uid":uid,"password":password,"pdt_id":pdt_id,"data1":data1[0],"data3":data3,"data5":data5,"ms":ms})
 


def deleteproduct(request):
    uid=request.session["uname"]
    password=request.session["pwd"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    ms=""
    if request.POST.get("submit") :
        pdtname=request.POST.get("t1")
        pdttype=request.POST.get("t2")
        pdtid=request.POST.get("t3")
        email=request.POST.get("t4")
        password=request.POST.get("t5")
        d="delete from addpro where pdt_id='"+str(pdtid)+"'" 
        c.execute(d)
        con.commit()
        ms="Deleted Your House Successfully!...."
    return render(request,"deleteproduct.html",{"uid":uid,"password":password,"data1":data1[0],"data3":data3,"data5":data5,"ms":ms})

def updateproduct(request):
    uid=request.session["uname"]
    password=request.session["pwd"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    ms=""
    if request.POST.get("submit") :
        pdtname=request.POST.get("t1")
        pdttype=request.POST.get("t2")
        description=request.POST.get("t3")
        startdate=request.POST.get("t4")
        enddate=request.POST.get("t5")
        files=request.POST.get("t6")
        myfile = request.FILES["t6"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        location=request.POST.get("t7")
        phno=request.POST.get("t10")
        pdt_id=request.POST.get("t11")
        price=request.POST.get("t12")
        d="update addpro set description='"+str(description)+"',startdate='"+str(startdate)+"',enddate='"+str(enddate)+"',files='"+str(filename)+"' ,price='"+str(price)+"' where pdt_id='"+str(pdt_id)+"'"
        print(d)
        print('***************************************************************')
        c.execute(d)
        con.commit()
        ms="Updated Your House Successfully!...."
    return render(request,"updateproduct.html",{"uid":uid,"password":password,"data1":data1[0],"data3":data3,"data5":data5,"ms":ms})

def contact(request):
    uid=request.session["uname"]
    password=request.session["pwd"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    l="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data3=c.fetchall()
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    if request.POST.get("submit"):
        phno=request.POST.get("t3")
        subject=request.POST.get("t4")
        s="insert into contact values('"+str(uid)+"','"+str(password)+"','"+str(phno)+"','"+str(subject)+"')"
        c.execute(s)
        con.commit()
    return render(request,"contact.html",{"uid":uid,"password":password,"data1":data1[0],"data3":data3,"data5":data5})

def photogallery(request):
    msg=request.GET.get("msg")
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro "
      c.execute(s)
      data=c.fetchall()
      print(s)
      data1=[]
     
    #   m="select location from account where email='"+str(uid)+"'"
    #   print(m)
    #   c.execute(m)
    #   data11=c.fetchall()
    #   print(data11)
      with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

            
        for row in csv_reader:
            
            if(search==row[0]):
                search=search+" "+row[1]
                    
                    
        print(search)
        for sent in data:
            for word in sent[2].split():
                for s in search.split():
                    s=s[0:-1]
                    
                    if(word[0:-1]==s[0:-1]):
                        #print(word)
                        data1.append(sent)
                        print("hellloooooo")
                        print(data1)
        return render(request,"photogallery.html",{"uid":uid,"data":data1})

    return render(request,"photogallery.html",{"uid":uid,"data1":data1[0],"data3":data3[0],"data5":data5,"msg":msg})

def cart(request):
    uid=request.session["uname"]
    paid="not paid"
    dp="select "
    s="select * from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(s)
    data=c.fetchall()
    l="select sum(price*day) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(l)
    data2=c.fetchone()
    request.session["pay"]=data2[0]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    b="select addpro.email,addpro.phno from addpro inner join checkout on addpro.pdt_id=checkout.pdt_id"
    c.execute(b)
    data6=c.fetchall()
    print(data6)
    msg="Welcome to domio.\nYour product has been carted by a user\n user id:'"+str(uid)+"'\n for futher details check your account"
    sendsms(data6[0][1],msg)
    return render(request,"cart.html",{"uid":uid,"data":data,"data1":data1[0],"data2":data2[0],"data3":data3[0],"data5":data5})

def details(request):
    uid=request.session["uname"]
    return render(request,"details.html",{"uid":uid})

def booking(request):
    alert=" "
    msg=" "
    uid=request.session["uname"]
    password=request.session["pwd"]
    pdt_type=request.GET.get("pdt_type") 
    pdt_id=request.GET.get("pdt_id")
    price=request.GET.get("price")
    startdate=request.GET.get("startdate")
    enddate=request.GET.get("enddate")
    print(enddate)
    sd="select files,description,email,phno from addpro where pdt_id='"+str(pdt_id)+"'"
    c.execute(sd)
    sd1=c.fetchone()
    desc=sd1[1]
    email=sd1[2]
    phno=sd1[3]
    if request.POST.get("submit") :
        start_date=request.POST.get("t5")
        end_date=request.POST.get("t7")
        day=request.POST.get("day")
        l="select count(*)from addpro where pdt_id='"+str(pdt_id)+"' and startdate>='"+str(start_date)+"'and enddate<='"+str(end_date)+"'"
        c.execute(l)
        data=c.fetchone()
        print(data[0])
        if(data[0]==0):
            m="select count(*)from booking where pdt_id='"+str(pdt_id)+"' and  start_date>='"+str(start_date)+"' and end_date<='"+str(end_date)+"'"
            print("hi")
            c.execute(m)
            data1=c.fetchone()
            print(data1[0])
            if(data1[0]==0):
                s="insert into booking values('"+str(uid)+"','"+str(password)+"','"+str(pdt_type)+"','"+str(pdt_id)+"','"+str(start_date)+"','"+str(end_date)+"','"+str(price)+"','"+str(day)+"')"
                print("hello")
                c.execute(s)
                con.commit()
                image="select files,description from addpro where pdt_id='"+str(pdt_id)+"'"
                c.execute(image)
                data=c.fetchone()
                paid="not paid"
                cart="insert into checkout values('"+str(uid)+"','"+str(password)+"','"+str(pdt_type)+"','"+str(pdt_id)+"','"+str(price)+"','"+str(start_date)+"','"+str(end_date)+"','"+str(data[0])+"','"+str(day)+"','"+str(paid)+"','','')"
                c.execute(cart)
                con.commit()
                return HttpResponseRedirect("/cart")
            else:
                msg="Sorry for the inconvienence, this product is booked by other user on same day "
                print("inner error")
            return render(request,"booking.html",{"uid":uid,"password":password,"data":data[0],"msg":msg,"startdate":startdate,"enddate":enddate,"pdt_type":pdt_type,"pdt_id":pdt_id,"price":price})
        else:
            alert="Booking is not available "
            print("error")
    return render(request,"booking.html",{"uid":uid,"password":password,"pdt_type":pdt_type,"pdt_id":pdt_id,"price":price,"startdate":startdate,"enddate":enddate,"alert":alert,"desc":desc,"email":email,"phno":phno})

def notification(request):
    uid=request.session["uname"]
    password=request.session["pwd"]
    d="select * from addpro where email='"+str(uid)+"'"
    c.execute(d)
    data2= c.fetchall()
    print(data2)
    e="select * from booking where email='"+str(uid)+"'"
    c.execute(e)
    data4 = c.fetchone()
    print(data4)
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    
    return render(request,"notification.html",{"uid":uid,"password":password,"data2":data2 ,"data4":data4,"data1":data1[0],"data3":data3[0],"data5":data5})

def usrhommenu(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    home="House & Rooms"
    s = "select * from addpro where pdttype='Flats' or pdttype='House and Rooms' "
    c.execute(s)
    data = c.fetchall()
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro"
      c.execute(s)
      data=c.fetchall()
      print(s)
      data14=[]
      m="select religion,senior,children from account where email='"+str(uid)+"'"
      print(m)
      c.execute(m)
      data11=c.fetchall()
      print(data11)
      with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for dd1 in data11:
            
            for row in csv_reader:
                
                if(dd1[0].upper()==row[0].upper()):
                    search=search+" "+row[1]
                    
                   

        for sent in data:
            for word in sent[2].split():
                for s in search.split():
                    if(word.upper()==s.upper()):
                        print(word)
                        data14.append(sent)
        return render(request,"usrhommenu.html",{"uid":uid,"data":data14})
    print("data s workimg bro",data)
    return render(request,"usrhommenu.html",{"uid":uid,"data":data,"data12345":data,"data1":data1[0],"data3":data3[0],"data5":data5})

def usrvehmenu(request):
    # uid=request.session["uname"]
    # s="select count(*) from addpro where email='"+str(uid)+"'"
    # c.execute(s)
    # data1 = c.fetchone()
    # print(data1)
    # paid="not paid"
    # f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    # c.execute(f)
    # data3 = c.fetchone()
    # print(data3)
    # y="select files from account where email='"+str(uid)+"'"
    # c.execute(y)
    # data5=c.fetchone()
    # print(data5)
    # vehicle="Vehicles"
    s = "select * from addpro where pdttype='Flats' or pdttype='House and Rooms' "
    c.execute(s)
    data = c.fetchall()
    # search=request.POST.get("search")
    # if request.POST.get("b1"): 
    #   s="select * from addpro "
    #   c.execute(s)
    #   data=c.fetchall()
    #   print(s)
    #   data14=[]
     
    #   m="select location from account where email='"+str(uid)+"'"
    #   print(m)
    #   c.execute(m)
    #   data11=c.fetchall()
    #   print(data11)
    #   with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     line_count = 0
    #     for dd1 in data11:
            
    #         for row in csv_reader:
                
    #             if(dd1[0].upper()==row[0].upper()):
    #                 search=search+" "+row[1]
                    
                   

    #     for sent in data:
    #         for word in sent[2].split():
    #             for s in search.split():
    #                 if(word.upper()==s.upper()):
    #                     print(word)
    #                     data14.append(sent)
    #     return render(request,"usrvehmenu.html",{"uid":uid,"data":data14})
    # return render(request,"usrvehmenu.html",{"uid":uid,"data":data,"data1":data1[0],"data3":data3[0],"data5":data5})
    return render(request,"usrvehmenu.html",{"data":data})

def usraudmenu(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    auditorium="Auditorium"
    s = "select * from addpro where pdttype='"+str(auditorium)+"'"
    c.execute(s)
    data = c.fetchall()
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro "
      c.execute(s)
      data=c.fetchall()
      print(s)
      data14=[]
     
      m="select religion from account where email='"+str(uid)+"'"
      print(m)
      c.execute(m)
      data11=c.fetchall()
      print(data11)
      with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for dd1 in data11:
            
            for row in csv_reader:
                
                if(dd1[0].upper()==row[0].upper()):
                    search=search+" "+row[1]
                    
                   

        for sent in data:
            for word in sent[2].split():
                for s in search.split():
                    if(word.upper()==s.upper()):
                        print(word)
                        data14.append(sent)
        return render(request,"usraudmenu.html",{"uid":uid,"data":data14})
   
    return render(request,"usraudmenu.html",{"uid":uid,"data":data,"data1":data1[0],"data3":data3[0],"data5":data5})

def usrparmenu(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where id='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    par="Party Rentatls"
    l = "select * from addpro where pdttype='"+str(par)+"'"
    c.execute(l)
    data = c.fetchall()
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro "
      c.execute(s)
      data=c.fetchall()
      print(s)
      data14=[]
     
      m="select location from account where email='"+str(uid)+"'"
      print(m)
      c.execute(m)
      data11=c.fetchall()
      print(data11)
      with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for dd1 in data11:
            
            for row in csv_reader:
                
                if(dd1[0].upper()==row[0].upper()):
                    search=search+" "+row[1]
                    
                   

        for sent in data:
            for word in sent[2].split():
                for s in search.split():
                    if(word.upper()==s.upper()):
                        print(word)
                        data14.append(sent)
        return render(request,"usrparmenu.html",{"uid":uid,"data":data14})
   
    return render(request,"usrparmenu.html",{"uid":uid,"data":data,"data1":data1[0],"data3":data3[0],"data5":data5})
def usrelemenu(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    electronic="Electronic Appliances"
    l = "select * from addpro where pdttype='"+str(electronic)+"'"
    c.execute(l)
    data = c.fetchall()
    search=request.POST.get("search")
    if request.POST.get("b1"): 
      s="select * from addpro where pdttype='"+str(electronic)+"'"
      c.execute(s)
      data=c.fetchall()
      print(s)
      data14=[]
    #   if request.POST.get("b1"): 
    #   s="select * from addpro "
    #   c.execute(s)
    #   data=c.fetchall()
    #   print(s)
    #   data1=[]
     
    #   m="select location from account where email='"+str(uid)+"'"
    #   print(m)
    #   c.execute(m)
    #   data11=c.fetchall()
    #   print(data11)
      with open('userapp\\static\\Book1.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0

            
        for row in csv_reader:
            
            if(search==row[0]):
                search=search+" "+row[1]
                    
                    
        print(search)
        for sent in data:
            for word in sent[2].split():
                for s in search.split():
                    s=s[0:-1]
                    
                    if(word[0:-1]==s[0:-1]):
                        #print(word)
                        data14.append(sent)
                        print("hellloooooo")
                        print(data1)
     
    # #   m="select location from account where email='"+str(uid)+"'"
    # #   print(m)
    # #   c.execute(m)
    # #   data11=c.fetchall()
    # #   print(data11)
    #   with open('F:\\dilsha\\demoproject\\userapp\\static\\Book1.csv', mode='r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     line_count = 0
    #   for sent in data:
    #       for word in sent[2].split():
    #         for s in search.split():
    #            print(word[0:-1])
    #            if(s[0:-1]< word[0][0:-1]):
    #                 search=search+" "+row[1]
    #   for sent in data:  
    #         for word in sent[2].split():
    #             for s in search.split():
    #                 print("ooooooooooooooooooooo")
    #                 #print(word)
    #                 print(word)
    #                 if(word.upper()==s.upper()):
                       
    #                     data1.append(sent)
    #                     print(data1)
      return render(request,"usrelemenu.html",{"uid":uid,"data":data14})
   
    return render(request,"usrelemenu.html",{"uid":uid,"data":data,"data1":data1[0],"data3":data3[0],"data5":data5})

def predictiondetails(request):
    print("################################################################################################")
    os.system("python F:\project\project\dilsha\demoproject\code\importwarnings.py")
    c.execute("select * from predict")
    data=c.fetchall()
    return render(request,"viewpredict.html",{"data":data})

def logoutview(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return HttpResponseRedirect("/usrlogin")

def payment1(request):
    uid=request.session["uname"]
    paid="paid"
    s="update checkout set paid='"+str(paid)+"'"
    print(s)
    c.execute(s)
    con.commit()
    if request.POST:
        card=request.POST.get("test")
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html",{"uid":uid})

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        name=request.POST.get("t1")
        request.session["m"]=name
        address=request.POST.get("t2")
        email=request.POST.get("t3")
        phno=request.POST.get("t4")
        n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        print(n)
        c.execute(n)
        con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = date.today()
    n="select * from delivery where card='"+str(cno)+"'"
    c.execute(n)
    data=c.fetchall()
    return render(request,"payment5.html",{"cno":cno,"data":data,"today":today})

def myaccount(request):
    uid=request.session["uname"]
    s="select count(*) from addpro where email='"+str(uid)+"'"
    c.execute(s)
    data1 = c.fetchone()
    print(data1)
    paid="not paid"
    f="select count(*) from checkout where email='"+str(uid)+"'and paid='"+str(paid)+"'"
    c.execute(f)
    data3 = c.fetchone()
    print(data3)
    y="select files from account where email='"+str(uid)+"'"
    c.execute(y)
    data5=c.fetchone()
    print(data5)
    password=request.session["pwd"]
    # if request.POST.get("b1"): 
    if 'b1' in request.POST:
        Address=request.POST.get("t3")
        location=request.POST.get("t4")
        # files=request.POST.get("t6")
        myfile = request.FILES["t6"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        religion=""
        phone=request.POST.get("t7")
        family=""
        senior=""
        children=""
        s="insert into account(`email`,`password`,`address`,`location`,`files`,`religion`,`phone`,`family`,`senior`,`children`) values('"+str(uid)+"','"+str(password)+"','"+str(Address)+"','"+str(location)+"','"+str(filename)+"','"+str(religion)+"','"+str(phone)+"','"+str(family)+"','"+str(senior)+"','"+str(children)+"')"
        c.execute(s)
        con.commit()
        msg="Account created successfully!..."
        return HttpResponseRedirect("/photogallery?msg="+msg)
    return render(request,"myaccount.html",{"uid":uid,"password":password,"data1":data1[0],"data3":data3[0],"data5":data5})



######################################################################################

import sklearn
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import xgboost
import lightgbm
import re
import pickle
import numpy as np
import pandas as pd

import sklearn


import matplotlib.pyplot as plt
import seaborn as sns

import warnings
def pricepredict(desc,price):
    warnings.filterwarnings('ignore')
    PATH = 'userapp/Dataset/'
    PATH_TO_train_data = PATH + 'train.csv'
    PATH_TO_test_data = PATH + 'train.csv'
    PATH_TO_sample_submission = PATH + 'sample_submission.xlsx'
    def preprocess_total_sqft(my_list):
        if len(my_list) == 1:
            
            try:
                return float(my_list[0])
            except:
                strings = ['Sq. Meter', 'Sq. Yards', 'Perch', 'Acres', 'Cents', 'Guntha', 'Grounds']
                split_list = re.split('(\d*.*\d)', my_list[0])[1:]
                area = float(split_list[0])
                type_of_area = split_list[1]
                
                if type_of_area == 'Sq. Meter':
                    area_in_sqft = area * 10.7639
                elif type_of_area == 'Sq. Yards':
                    area_in_sqft = area * 9.0
                elif type_of_area == 'Perch':
                    area_in_sqft = area * 272.25
                elif type_of_area == 'Acres':
                    area_in_sqft = area * 43560.0
                elif type_of_area == 'Cents':
                    area_in_sqft = area * 435.61545
                elif type_of_area == 'Guntha':
                    area_in_sqft = area * 1089.0
                elif type_of_area == 'Grounds':
                    area_in_sqft = area * 2400.0
                return float(area_in_sqft)
            
        else:
            return (float(my_list[0]) + float(my_list[1]))/2.0
    train_data = pd.read_csv(PATH_TO_train_data)
    test_data = pd.read_csv(PATH_TO_test_data)
    train_data.shape
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(train_data.head())
    train_data.head()
    train_data.area_type.value_counts()
    replace_area_type = {'Super built-up  Area': 0, 'Built-up  Area': 1, 'Plot  Area': 2, 'Carpet  Area': 3}
    train_data['area_type'] = train_data.area_type.map(replace_area_type)


    train_data.head()


    def replace_availabilty(my_string):

        if my_string == 'Ready To Move':
            return 0
        elif my_string == 'Immediate Possession':
            return 1
        else:
            return 2
    train_data['availability'] = train_data.availability.apply(replace_availabilty)
    train_data.head()


    train_data[~train_data.location.notnull()]


    train_data['location'] = train_data['location'].fillna('Location not provided')

    size_encoder = LabelEncoder()
    size_encoder.fit(train_data['size'].astype('str').append(test_data['size'].astype('str')))
    train_data['size'] = size_encoder.transform(train_data['size'].astype('str'))
    #print(train_data)
    # array(['1 BHK', '1 Bedroom', '1 RK', '10 BHK', '10 Bedroom', '11 BHK',
    #        '11 Bedroom', '12 Bedroom', '13 BHK', '14 BHK', '16 BHK',
    #        '16 Bedroom', '18 Bedroom', '19 BHK', '2 BHK', '2 Bedroom',
    #        '27 BHK', '3 BHK', '3 Bedroom', '4 BHK', '4 Bedroom', '43 Bedroom',
    #        '5 BHK', '5 Bedroom', '6 BHK', '6 Bedroom', '7 BHK', '7 Bedroom',
    #        '8 BHK', '8 Bedroom', '9 BHK', '9 Bedroom', 'nan'], dtype=object)
    train_data.head()
    # train_data = train_data.drop(columns='society', axis=1)
    train_data['society'] = train_data['society'].fillna('Other')
    society_encoder = LabelEncoder()
    society_encoder.fit(train_data['society'].append(test_data['society'].fillna('Other')))
    train_data['society'] = society_encoder.transform(train_data['society'])
    train_data.head()

    train_data['total_sqft'] = train_data.total_sqft.str.split('-').apply(preprocess_total_sqft)
    train_data['bath'].isna().sum()
    column_bath = train_data.groupby('location')['bath'].transform(lambda x: x.fillna(x.mean()))
    column_bath[~column_bath.notnull()]
    column_bath = column_bath.fillna(column_bath.mean())
    column_bath.isna().sum()
    train_data['bath'] = column_bath
    train_data.balcony.isna().sum()
    train_data.balcony.value_counts()
    column_balcony = train_data.groupby('location')['balcony'].transform(lambda x: x.fillna(x.mean()))
    column_balcony = column_balcony.fillna(column_balcony.mean())
    column_balcony.isna().sum()
    train_data['balcony'] = column_balcony
    train_data.head()
    location_encoder = LabelEncoder()
    location_encoder.fit(train_data['location'].append(test_data['location']))
    train_data['location'] = location_encoder.transform(train_data['location'])
    location_encoder.classes_


    train_data.head()

    columns = train_data.columns
    X_train = train_data[columns[:-1]]
    y_train = train_data[columns[-1]]
    test_data = pd.read_csv(PATH_TO_test_data)
    test_data.isna().sum()
    test_data.head()
    test_data['area_type'] = test_data.area_type.map(replace_area_type)

    test_data['availability'] = test_data.availability.apply(replace_availabilty)

    test_data['location'] = location_encoder.transform(test_data['location'].astype('str'))

    test_data['size'] = size_encoder.transform(test_data['size'].astype('str'))

    test_data['society'] = society_encoder.transform(test_data['society'].astype('str').fillna('Other'))

    test_data['total_sqft'] = test_data.total_sqft.str.split('-').apply(preprocess_total_sqft)

    test_data['bath'] = test_data['bath'].fillna(train_data.bath.mean())

    test_data['balcony'] = test_data['balcony'].fillna(train_data.balcony.mean())
    y_pred=test_data['price']
    # test_data = test_data.drop(columns='price')

    # X_test = test_data
    # X_test.head()

    #print(test_data['balcony'] )


    #from sklearn.grid_search import GridSearchCV
    from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, train_test_split
    
    params = {'min_child_weight':[4,5,6], 'gamma':[i/10.0 for i in range(3,6)],  'subsample':[i/10.0 for i in range(6,11)],
    'colsample_bytree':[i/10.0 for i in range(6,11)], 'max_depth': [2,3,4], 'n_estimators':[1000, 1500, 2000], 
            'learning_rate':[0.01, 0.05, 0.1]}
    #print(params)
    xgb = xgboost.XGBRegressor(nthread=-1) 
    #print(xgb)
    grid = GridSearchCV(xgb, params)
    # print(grid)
    import random
    n = random.randint(1,22)
    print(y_train[n])

    # grid.fit(X_train, y_train)
    print("######################################################################################")
    # grid.best_estimator_
    # y_pred = grid.best_estimator_.predict(X_test)
    # y_pred = model.predict(X_test)
    # y_pred
    # out_df = pd.DataFrame({'price': y_pred})
    # y_pred=test_data['price']
    y_pred=int(price)-int(y_train[n])
   
    # print(out_df)

    # out_df.to_excel('predictions_grid_search.xlsx', index=False)
    # import pickle
    # pkl_filename = "xgboost_grid_search.pkl"  
    # with open(pkl_filename, 'wb') as file:
        # pickle.dump(grid, file)


    return y_pred