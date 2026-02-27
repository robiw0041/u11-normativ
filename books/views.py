from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator
from .models import Post


# CREATE
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

# READ (List)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


# UPDATE
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})


# DELETE
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})




def post_list(request):
    posts = Post.objects.all()

    # SEARCH
    q = request.GET.get("q")
    if q:
        posts = posts.filter(
            title__icontains=q
        ) | posts.filter(
            content__icontains=q
        )

    # PAGINATION
    paginator = Paginator(posts, 5)  # har sahifada 5 ta
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "posts/post_list.html", {
        "page_obj": page_obj,
    })