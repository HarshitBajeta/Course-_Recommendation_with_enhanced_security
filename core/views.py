from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from item.models import Category, Item
from .forms import SignupForm, LoginForm
from .models import Order, Order_Item, User
# from django.contrib.User import User
import io
from django.conf import settings
import numpy as np
import bcrypt


# Create your views here.
def index(request):
    recommended = []
    if request.user.is_authenticated:
        customer = User.objects.get(username=request.user.username)
        recommended_category = get_user_preferred_category(customer)
        if recommended_category:
        # profile = Profile.objects.get(user=customer)
        # recommended_category = profile.preferred_category
            recommended_all = Item.objects.filter(category=recommended_category)

            order = Order.objects.get(user=customer)
            items = Order_Item.objects.filter(order=order)

            for item in recommended_all:
                if item not in items:
                    recommended.append(item)
                if len(recommended)==3:
                    break

    items = Item.objects.all().order_by('price')#.values()
    categories = Category.objects.all()
    user=request.user
    a = dict()
    a['user']=user
    a['items'] = items
    a['categories'] = categories
    a['count'] = int(len(recommended))
    a['recommended'] = recommended

    return render(request, 'core/index.html', context=a)

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            # image = form.cleaned_data.get("image")
            hash = bcrypt.hashpw(password1.encode('utf8'), bcrypt.gensalt())
            
            xyz=User(username=username,email=email,password=password1,hashed_password=hash)
            xyz.save()
            
            user = User.objects.get(username=username)
            order = Order(user=user)
            order.save()
            # print(xyz.username)
            # print(xyz.password)
            # user_img = Userimage(user=user, img=image)
            # user_img.save()
            # profile = Profile(user=user)
            # profile.save()
            # user = authenticate(username=username,password=password1)
            login(request,user)        
            return redirect('/')
        else:
            a=dict()
            a['form'] = form
            return render(request, 'core/signup.html', context=a)
        
    else:
        form = SignupForm()
        
    a=dict()
    a['form'] = form
    return render(request, 'core/signup.html', context=a)

def login_view(request):
    if request.method == 'POST':
        # if form.is_valid():
        # print(123)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user1 = User.objects.get(username=username)
        print(user1.username, user1.password)
        #user = authenticate(request, username=username,password=password)
        # print(user.password)
        # if user is not None:
        if username == user1.username and password == user1.password:
                login(request, user1)
                return redirect('/')
            
        else:
            form = LoginForm()
            # form.add_error(None, 'Username and Password do not match.')
    else:
        form = LoginForm()

    return render(request, "core/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

def learning(request):
    if request.user.is_authenticated:
        customer = User.objects.filter(username=request.user.username)[0]
        order = Order.objects.get(user=customer)
        items = Order_Item.objects.filter(order=order)
    else:
        form = LoginForm()
        return render(request, "core/login.html", {'form': form})
    
    return render(request, 'core/cart.html', {'items': items})

def get_user_preferred_category(user):
    # try:
    #     profile = Profile.objects.get(user=user)
    # except:
    #     return 
    order = Order.objects.get(user=user)
    purchased_courses = Order_Item.objects.filter(order=order)

    # Count the occurrences of each category in purchased courses
    category_counts = {}
    for course in purchased_courses:
        category_counts[course.item.category] = category_counts.get(course.item.category, 0) + 1

    # Find the category with the maximum count
    if len(category_counts)>0:
        preferred_category = max(category_counts, key=category_counts.get)

        return preferred_category
    return False

import pickle
from django.http import HttpResponse


def initialize_app():
    popular_df = pickle.load(open('core/data/courses.pkl', 'rb'))
    similarity_scores = pickle.load(open('core/data/similarity.pkl', 'rb'))
    return popular_df, similarity_scores

popular_df, similarity_scores = initialize_app()

def recommend_ui(request):
    return render(request, 'core/recommend1.html')

def recommend(request):
    if request.method == 'GET':
        user_input = request.GET.get('user_input')
        try:
            index = popular_df[popular_df['course_name'] == user_input].index[0]
        except:
            return render(request, 'core/error.html', {'message': 'Course not found'})

        distances = sorted(list(enumerate(similarity_scores[index])), reverse=True, key=lambda x: x[1])
        data = []
        for i in distances[1:6]:
            item = []
            item.append(popular_df.iloc[i[0]].course_name)
            item.append(popular_df.iloc[i[0]].University)
            item.append(popular_df.iloc[i[0]].difficulty_level)
            item.append(popular_df.iloc[i[0]].course_rating)
            data.append(item)
        print(data)
        return render(request, 'core/recommend1.html', {'data': data})
    return HttpResponse('Invalid request')
