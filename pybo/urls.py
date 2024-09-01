from django.urls import path

from .views import base_views, board_views, answer_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:board_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('board/create/', board_views.board_create, name='board_create'),
    path('board/modify/<int:board_id>/', board_views.board_modify, name='board_modify'),
    path('board/delete/<int:board_id>/', board_views.board_delete, name='board_delete'),
    path('board/vote/<int:board_id>/', board_views.board_vote, name='board_voter'),

    # answer_views.py
    path('answer/create/<int:board_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_voter'),

]
