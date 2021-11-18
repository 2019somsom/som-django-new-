from django.urls import path, include

from .views import slide
from .views import user
from .views import etc
from .views import rank

urlpatterns = [
    path('', etc.index, name='index'),
    path('main/slide', slide.get_main_slide_list, name='main_slide'),
    path('main/slide/create/dummy', slide.create_dummy_slide, name='create_dummy_slide'),
    path('main/slide/<int:slide_id>', slide.get_one_main_slide, name='main_slide'),
    path('user', user.signup, name='signup'),
    path('user/check/email', user.id_check, name='check_email'),
    path('user/check/nickname', user.nickname_check, name='check_nickname'),
    path('session', user.login, name='login'),

    path('hotel/rank/category', rank.get_rank_cat_list, name='rank_category'),
    path('hotel/rank/hotel/<str:cat_code>', rank.get_top_rank_list, name='rank'),

    path('users/', include('users.urls')),
]
