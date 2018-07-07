from django.conf.urls import url
from django.urls import path
from .hotel.list.view import ExListView
from .hotel.edit.view import ExEditView

urlpatterns = [
    path('', ExListView.as_view(template_name='list.html'), name='list'),
    path('create/', ExEditView.as_view(template_name='edit.html', mode='create'), name='create'),
    path('detail/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='detail'), name='detail'),
    path('update/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='update'), name='update'),
    path('delete/<int:hotel_id>/', ExEditView.as_view(template_name='edit.html', mode='delete'), name='delete')
]
