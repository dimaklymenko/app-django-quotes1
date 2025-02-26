from django.shortcuts import render, get_object_or_404, redirect
from .utils import get_mongodb
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm, TagForm
from .models import Author, Quote, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# def main(request, page=1):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page =paginator.page(page)
#     return render(request, 'quotes/index.html', context={'quotes' : quotes_on_page})


def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(quotes, per_page)

    try:
        quotes_on_page = paginator.page(page)
    except PageNotAnInteger:
        # Якщо сторінка не є цілим числом, показуємо першу сторінку
        quotes_on_page = paginator.page(1)
    except EmptyPage:
        # Якщо сторінка поза діапазоном (наприклад, 9999), показуємо останню сторінку
        quotes_on_page = paginator.page(paginator.num_pages)

        # Отримуємо топ-10 тегів
    top_tags = Tag.objects.annotate(num_quotes=Count("quote")).order_by("-num_quotes")[
        :10
    ]

    return render(
        request,
        "quotes/index.html",
        {
            "quotes": quotes_on_page,
            "top_tags": top_tags,
        },
    )


#
# def main(request, page=1):
#     quotes = Quote.objects.all()
#     per_page = 10
#     paginator = Paginator(list(quotes), per_page)
#     quotes_on_page =paginator.page(page)
#     return render(request, 'quotes/index.html', context={'quotes' : quotes_on_page})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quotes:root")
    else:
        form = AuthorForm()
    return render(request, "quotes/add_author.html", {"form": form})


# @login_required
# def add_quote(request):
#     if request.method == 'POST':
#         form = QuoteForm(request.POST)
#         if form.is_valid():
#             quote = form.save(commit=False)
#             quote.user = request.user
#             quote.save()
#             return redirect('quotes:root')
#     else:
#         form = QuoteForm()
#     return render(request, 'quotes/add_quote.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.save()  # Зберігаємо цитату
            form.save_m2m()  # Зберігаємо зв'язки ManyToMany (теги)
            return redirect("quotes:root")  # Перенаправлення після успішного збереження
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})


@login_required
def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="quotes:root")
        else:
            return render(request, "quotes/tag.html", {"form": form})

    return render(request, "quotes/add_tag.html", {"form": TagForm()})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, "quotes/author_detail.html", {"author": author})


def tag_detail(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    # Отримуємо всі цитати, пов'язані з цим тегом
    quotes = Quote.objects.filter(tags=tag)
    return render(request, "quotes/tag_detail.html", {"quotes": quotes, "tag": tag})


def top_tags(request):
    # Отримуємо топ-10 тегів за кількістю цитат
    top_tags = Tag.objects.annotate(num_quotes=Count("quote")).order_by("-num_quotes")[
        :10
    ]
    return render(request, "quotes/top_tags.html", {"top_tags": top_tags})
