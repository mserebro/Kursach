from django.urls import path

from .views import *

urlpatterns = [
   path('', index, name='home'),
   # path('addliblink/', addliblink, name='add_liblink'),
   # path('contact/', contact, name='contact'),
   # path('login/', login, name='login'),
   # path('post/<int:post_id>/', show_post, name='post'),
   path('liblinks/', LiblinksView/as_view(), name='Liblinks'),
   path('liblinks/<int:liblinks_id>/', LiblinksUpdate/as_view(), name='LiblinksUpdate'),
]

