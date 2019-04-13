from django.forms import ModelForm
from cms.models import Book
from django.contrib.auth.forms import (
    AuthenticationForm
)


class BookForm(ModelForm):
    """書籍のフォーム"""

    class Meta:
        model = Book
        fields = ('name', 'publisher', 'page')


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
