from django.shortcuts import render, redirect

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    # sort = request.GET.get('sort', None)
    template = 'books/books_list.html'
    _books = Book.objects.all()
    books = [
        {'name': book.name, 'author': book.author, 'pub_date': book.pub_date}
        for book in _books
    ]
    context = {'books': books}
    return render(request, template, context)


def books_view_by_date(request, pub_date):
    # sort = request.GET.get('sort', None)
    template = 'books/books_list.html'
    _books = Book.objects.all()
    books = []
    prev_pub_dates = []
    next_pub_dates = []
    for book in _books:
        book_pub_date = book.pub_date.strftime('%Y-%m-%d')
        if book_pub_date == pub_date:
            books.append({'name': book.name, 'author': book.author, 'pub_date': book_pub_date})
        if book_pub_date < pub_date:
            prev_pub_dates.append(book_pub_date)
        if book_pub_date > pub_date:
            next_pub_dates.append(book_pub_date)

    prev_pub_dates.sort()
    next_pub_dates.sort()

    context = {
        'books': books,
        'prev_pub_date': prev_pub_dates[-1] if len(prev_pub_dates) else None,
        'next_pub_date': next_pub_dates[0] if len(next_pub_dates) else None
    }
    return render(request, template, context)
