from django import forms
from pybo.models import Board, Answer


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board  # 사용할 모델
        fields = ['subject', 'content']  # BoardForm에서 사용할 Board 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }