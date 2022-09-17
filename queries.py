import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MMElasticSearch.settings")
import django
django.setup()

from django.core.management import call_command

from blog.documents import ArticleDocument
from elasticsearch_dsl import Q

# search = ArticleDocument.search()

query = 'How to'
q = Q(
    'multi_match',
    query=query,
    fields=[
        'name'
    ])

search = ArticleDocument.search().query(q)
search.execute()

# print all the hits
for hit in search:
    print(hit.name)
