from django.core.management.base import BaseCommand
import json

from articles.models import Article


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs=1, type=str)

    def handle(self, *args, **options):
        with open(options['filename'][0], 'r', encoding='utf-8') as file:
            records = json.load(file)

        FIELDS = ["title", "text", "published_at", "image"]
        for record in records:
            if record['model'] == 'articles.article':
                articlesCount = Article.objects.filter(id=record['pk']).count()
                if articlesCount == 0:
                    article = {'id': record['pk']}
                    for field in FIELDS:
                        article[field] = record['fields'][field]

                    Article.objects.create(**article)

        print('Base fill')



