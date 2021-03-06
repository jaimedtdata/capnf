from django.contrib import admin
from django.urls import path, include
from apps.views import (Login, dashboard,dash, index, liquid, comision, plan, plan_edit, plan_delete, carga_rules,plan_list,checkout,preguntas,signup,
	entrevistas, charts,member, configs, works, rules, foro, foro_temas,foro_comentarios,
    password_reset,SignUpOthers,success_sign_up)

from django.conf.urls import url



urlpatterns = [
    #path('', login, name='login'),
    #path('foro/', include('foro.urls')),
    path('', Login.as_view(), name='login'),
    path('login/', Login.as_view(), name='login'),
    path('dash/', dash, name='dash'),
    path('db-admin/', admin.site.urls),
    path('success_sign_up/', success_sign_up, name='success_sign_up'),
    #path('sign-up/', signup, name='sign-up'),
    #path('normas/', include('apps.normas.urls',namespace='Normas')),
    #path('foro/', include('apps.foro.urls',namespace='Normas')),
    
    path('dashboard/', dashboard, name='dashboard'),
    
    #path('rules/', rules, name='rules'),
    path('rules/', rules, name='rules'),

    path('carga_rules/', carga_rules, name='carga_rules'),
    # path('member/', member, name='member'),

    path('foro/', foro, name='foro'),
    path('foro_temas/', foro_temas, name='foro_temas'),
    path('foro_comentarios/', foro_comentarios, name='foro_comentarios'),
    

    path('sign-up/', SignUpOthers.as_view(), name='sign-up'),
    path('password_reset/', password_reset, name='password_reset'),
    path('preguntas/', preguntas, name='preguntas'),

    path('plan_list/', plan_list, name='plan_list'),
    path('checkout/', checkout, name='checkout'),
    
    # path('plan', plan, name='plan'),
    # path('plan/plan_edit/<int:pk>/', plan_edit, name='plan_edit'),
    # path('plan/plan_edit/', plan_edit, name='plan_edit'),
    # path('plan/plan_delete/<int:pk>/', plan_delete, name='plan_delete'),

    # path('users/', users, name='users'),
    # url(r'^users/users_create$', users_create, name='users_create'),
    # url(r'^users/users_save$', users_save, name='users_save'),
    # url(r'^users/users_edit/(?P<id>\d+)$', users_edit, name='users_edit'),
    # url(r'^users/users_edit/users_update/(?P<id>\d+)$', users_update, name='users_update'),
    # url(r'^users/users_delete/(?P<id>\d+)$', users_delete, name='users_delete'),
    #path('users_edit/<int:pk>/', users_edit, name='users_edit'),
    # path('configs/', configs, name='configs'),
]
admin.site.site_header = 'Administracion - Normativa'