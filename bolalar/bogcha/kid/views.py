from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.decorators import gzip
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
import cv2
import threading
from django.utils.translation import activate
from django.http import JsonResponse
from .serializers import StaffSerializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@csrf_exempt
def all_staff(request):
    if request.method=="GET":
        staffs = Staff.objects.all()
        staffs_ser = StaffSerializers(staffs, many=True)
        return JsonResponse(staffs_ser.data, safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serialize=StaffSerializers(data=data)

        if serialize.is_valid:
            serialize.save()
            return JsonResponse(serialize.data, status=201)
        return JsonResponse(serialize.data, status=200)

@csrf_exempt
def staff_detail(request, pk):
    try:
        staff=Staff.objects.get(pk=pk)

    except Staff.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serialize=StaffSerializers(staff)
        return JsonResponse(serialize.data)

    elif request.method=='PUT':
        item=JSONParser().parse(request)
        serialize=StaffSerializers(staff, data=item)
        if serialize.is_valid:
            serialize.save()
            return JsonResponse(serialize.data)
        return JsonResponse(serialize.errors, status=400)

    elif request.method=='DELETE':
        staff.delete()
        return HttpResponse(status=204)





def main(request):
    request.title="Main"
    if request.POST.get('lang')=='en':
        reverse('main:main')
        activate('en')
    elif request.POST.get('lang')=='uz':
        reverse('main:main')
        activate('uz')

    return render(request, 'kid/index.html')

def about(request):

    return render(request, 'kid/about.html')

def blog(request):

    return render(request, 'kid/blog.html')

def class1(request):

    return render(request, 'kid/class.html')

def contact(request):

    return render(request, 'kid/contact.html')

def gallery(request):
    picture=Gallery.objects.all()
    context={'picture':picture}
    return render(request, 'kid/gallery.html', context)

def addPicture(request):
    form=PictureForm()

    if request.method=='POST':
        myform=PictureForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('/gallery/')
        else:
            print(myform.errors)

    context={'form': form}
    return render(request, 'kid/picture.html', context)

def updatePicture(request, gid):
    picture=Gallery.objects.get(id=gid)
    form = PictureForm(instance=picture)

    if request.method=="POST":
        myform=PictureForm(request.POST, instance=picture)
        if myform.is_valid():
            myform.save()
            return redirect('/picture/')

    context={'form': form}
    return render(request, 'kid/picture.html', context)


def team(request):
    staff=Staff.objects.all()
    data={'staff': staff}
    return render(request, 'kid/team.html',data)

@login_required(login_url='userLogin')
def staff(request):
    staff=Staff.objects.all()
    data={'staff': staff}
    return render(request, 'kid/staff.html',data)

def addStaff(request):
    form=StaffForm()

    if request.method=='POST':
        myform=StaffForm(request.POST, request.FILES)
        if myform.is_valid():
            myform.save()
            return redirect('/staff/')
        else:
            print(myform.errors)

    context={'form': form}
    return render(request, 'kid/create.html', context)


def updateStaff(request,sid):
    staff=Staff.objects.get(id=sid)
    form = StaffForm(instance=staff)

    if request.method=="POST":
        myform=StaffForm(request.POST, instance=staff)
        if myform.is_valid():
            myform.save()
            return redirect('/staff/')

    context={'form': form}
    return render(request, 'kid/create.html', context)

def deleteStaff(request, sid):
    staff = Staff.objects.get(id=sid)
    if request.method=='POST':
        staff.delete()
        return redirect('/staff/')
    sdata={'staff':staff}
    return render(request, 'kid/s_delete.html', sdata)


@login_required(login_url='userLogin')
def children(request):
    child=Children.objects.all()
    cdata = {'child': child}
    return render(request, 'kid/child.html', cdata)

def addChild(request):
    cform=ChildrenForm()

    if request.method=='POST':
        myreq=ChildrenForm(request.POST)
        if myreq.is_valid():
            myreq.save()
            return redirect('/child/')
        else:
            print(myreq.errors)
    res={'cform': cform}
    return render(request, 'kid/addchild.html', res)

def updateChild(request,cid):
    child=Children.objects.get(id=cid)
    cform = ChildrenForm(instance=child)

    if request.method=="POST":
        myreq=ChildrenForm(request.POST, instance=child)
        if myreq.is_valid():
            myreq.save()
            return redirect('/child/')

    context={'cform': cform}
    return render(request, 'kid/addchild.html', context)

def deleteChild(request, cid):
    child = Children.objects.get(id=cid)
    if request.method=='POST':
        child.delete()
        return redirect('/child/')
    cdata={'child':child}
    return render(request, 'kid/c_delete.html', cdata)

def group(request):
    group=Group.objects.all()
    
    gdata={'group': group}
    return render(request, 'kid/group.html', gdata)

def addGroup(request):
    gform=GroupForm()

    if request.method=='POST':
        myres=GroupForm(request.POST)
        if myres.is_valid():
            myres.save()
            return redirect('/group/')
        else:
            print(myres.errors)
    res={'gform': gform}
    return render(request, 'kid/addGroup.html', res)

def updateGroup(request,gid):
    group=Group.objects.get(id=gid)
    gform = GroupForm(instance=group)

    if request.method=="POST":
        myreq=GroupForm(request.POST, instance=group)
        if myreq.is_valid():
            myreq.save()
            return redirect('/group/')

    context={'gform': gform}
    return render(request, 'kid/addGroup.html', context)

def deleteGroup(request, gid):
    group = Group.objects.get(id=gid)
    if request.method=='POST':
        group.delete()
        return redirect('/group/')
    gdata={'group':group}
    return render(request, 'kid/g_delete.html', gdata)


@login_required(login_url='userLogin')
def news(request):
    news=Blog.objects.all()
    bdata={'news':news}
    return render(request, 'kid/news.html', bdata)

def addnews(request):
    nform=BlogForm

    if request.method=='POST':
        myres=BlogForm(request.POST)
        if myres.is_valid():
            myres.save()
            return redirect('/news/')
        else:
            print(myres.errors)
    res={'nform': nform}
    return render(request, 'kid/addblog.html', res)

def updateBlog(request,bid):
    news=Blog.objects.get(id=bid)
    nform = BlogForm(instance=news)

    if request.method=="POST":
        myreq=BlogForm(request.POST, instance=news)
        if myreq.is_valid():
            myreq.save()
            return redirect('/news/')

    context={'nform': nform}
    return render(request, 'kid/addblog.html', context)

def deleteBlog(request, bid):
    news = Blog.objects.get(id=bid)
    if request.method=='POST':
        news.delete()
        return redirect('/news/')
    bdata={'news':news}
    return render(request, 'kid/b_delete.html', bdata)


@login_required(login_url='userLogin')
def meals(request):
    meal=Meals.objects.all()
    mdata={'meal':meal}
    return render(request,'kid/meal.html', mdata)


def addMeals(request):
    mform=MealsForm

    if request.method=='POST':
        mymeal=MealsForm(request.POST)
        if mymeal.is_valid():
            mymeal.save()
            return redirect('/meal/')
        else:
            print(mymeal.errors)
    rst={'mform': mform}
    return render(request, 'kid/addmeal.html', rst)

def updateMeals(request,mid):
    meal=Meals.objects.get(id=mid)
    mform = GroupForm(instance=meal)

    if request.method=='POST':
        mymeal=MealsForm(request.POST, instance=meal)
        if mymeal.is_valid():
            mymeal.save()
            return redirect('/meal/')

    rst={'mform': mform}
    return render(request, 'kid/addmeal.html', rst) 

def deleteMeal(request, mid):
    meal = Meals.objects.get(id=mid)
    if request.method=='POST':
        meal.delete()
        return redirect('/meal/')
    mdata={'meal':meal}
    return render(request, 'kid/m_delete.html', mdata)
    
class VideoCamera(object):
    def __init__(self):
        self.video=cv2.VideoCapture(0)
        (self.grabbed, self.frame)=self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image=self.frame
        _, jpeg=cv2.imencode('.jpeg', image)
        return jpeg.tobytes()


    def update(self):
        while True:
            (self.grabbed, self.frame)=self.video.read()

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')

@gzip.gzip_page
def Home(request):
    try:
        cam=VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
