from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from cms.models import Book, Impression
from cms.forms import BookForm, ImpressionForm


def book_list(request):
    """書籍の一覧"""
#    return HttpResponse('書籍の一覧')
    books = Book.objects.all().order_by('id')
    return render(request,
                  'cms/book_list.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    """書籍の編集"""
    # Book ID is specified (to modify)
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        # Validation of form
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        # Create an instance from BookForm
        form = BookForm(instance=book)

    return render(request, 'cms/book_edit.html', dict(form=form, book_id=book_id))


def book_del(request, book_id):
    """書籍の削除"""
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('cms:book_list')


class ImpressionList(ListView):
    """感想の一覧"""
    context_object_name = 'impressions'
    template_name = 'cms/impression_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        # Read a parent object (book)
        book = get_object_or_404(Book, pk=kwargs['book_id'])
        # Read the child object (impression)
        impressions = book.impressions.all().order_by('id')
        self.object_list = impressions

        context = self.get_context_data(object_list=self.object_list, book=book)
        return self.render_to_response(context)


def impression_edit(request, book_id, impression_id=None):
    """感想の編集"""
    # Read a parent object (Book)
    book = get_object_or_404(Book, pk=book_id)

    # When modifying impression
    if impression_id:
        impression = get_object_or_404(Impression, pk=impression_id)
    # When adding impression
    else:
        impression = Impression()

    if request.method == 'POST':
        # Read the posted form data
        form = ImpressionForm(request.POST, instance=impression)
        # Validation of form
        if form.is_valid():
            impression = form.save(commit=False)
            impression.book = book  # Set the parent of this impression
            impression.save()
            return redirect('cms:impression_list', book_id=book_id)
    else:
        # Create a form from Impression instance
        form = ImpressionForm(instance=impression)

    return render(request, 'cms/impression_edit.html', dict(form=form, book_id=book_id, impression_id=impression_id))


def impression_del(request, book_id, impression_id):
    """感想の削除"""
    impression = get_object_or_404(Impression, pk=impression_id)
    impression.delete()
    return redirect('cms:impression_list', book_id=book_id)