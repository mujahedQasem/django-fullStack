from django.urls import path
from tv_show_app import views

urlpatterns =[
    path('',views.index),
    path('shows',views.shows,name='shows'),
    path('shows/<int:show_id>',views.view_show,name='view_selected_show'),
    path('shows/new',views.new_show,name='new_show'),
    path('shows/,<int:show_id>/edit',views.edit,name='edit'),
    path('shows/<int:show_id>/delete',views.delete,name='delete')
    
]