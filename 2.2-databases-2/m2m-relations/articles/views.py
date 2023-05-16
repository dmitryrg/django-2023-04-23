from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    # articles = Article.objects.all()
    articles = Article.objects.prefetch_related('scopes').all()
    # for article in articles:
    #     for scope in article.scopes.all():
    #         print(scope.is_main)

    context = {'object_list': articles}

    return render(request, template, context)
