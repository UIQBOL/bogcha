from django.urls import path
from .views import *

urlpatterns=[
    path('', main, name='main'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('class1/', class1, name='class1'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('picture/', addPicture, name='picture'),
    path('pictures/update/<int:pk>', updatePicture, name='updatePicture'),
    path('staffs/', all_staff),
    path('staffs/detail/<int:pk>', staff_detail, name='detail'),
    path('team/',team, name='team'),


    path('staff/', staff, name='staff'),
    path('staff/add', addStaff, name='s_add'),
    path('staff/update/<str:sid>',updateStaff, name='updateStaff'),
    path('staff/delete/<str:sid>', deleteStaff, name='s_delete'),

    path('child/', children, name='child'),
    path('child/add', addChild, name='c_add'),
    path('c_update/<str:cid>', updateChild, name='child_u'),
    path('c_delete/<str:cid>', deleteChild, name='c_delete'),

    path('group/', group, name='group'),
    path('group/add', addGroup, name='g_add'),
    path('g_update/<str:gid>', updateGroup, name='g_update'),
    path('g_delete/<str:gid>', deleteGroup, name='g_delete'),

    path('news/', news, name='news'),
    path('blog/add', addnews, name='b_add'),
    path('b_update/<str:bid>', updateBlog, name='b_update'),
    path('b_delete/<str:bid>', deleteBlog, name='b_delete'),

    path('meal/', meals, name='meal'),
    path('meal/add', addMeals, name='m_add'),
    path('updateMeals/<str:mid>', updateMeals, name='m_update'),
    path('deleteMeals/<str:mid>', deleteMeal, name='m_delete'),


]