from blog.models import *
from django.db.models import Q, Subquery


# --- 1
art_nurs_two = Article.objects.filter(authors__name='Нурсултан Бердиев')[:2]

art_nurs_two[0].authors.add(Author.objects.get(name='Лю Вероника'))
art_nurs_two[1].authors.add(Author.objects.get(name='Токтосунова Чынара'))


# --- 2
# 1
Publication.objects.filter(author__email__endswith='@gmail.com', date_published__lte='2023-04-17')
# 2
Publication.objects.filter(author__email__endswith='@gmail.com') & \
Publication.objects.filter(date_published__lte='2023-04-17')
# 3
Publication.objects.filter(Q(author__email__endswith='@gmail.com') & Q(date_published__lte='2023-04-17'))


# --- 3
# 1
query1 = Author.objects.filter(name='Нурсултан Бердиев')
query2 = Author.objects.filter(date_register='2021-01-04')
query1.union(query2)
# 2
Author.objects.filter(name='Нурсултан Бердиев') | Author.objects.filter(date_register='2021-01-04')
# 3
Author.objects.filter(Q(name='Нурсултан Бердиев') | Q(date_register='2021-01-04'))


# --- 4
# не логично выбирать Publication.objects.all().exclude(author__name="Лю Вероника"), потому что те статьи в
# которых она находится все равно появятся
# 1
Article.objects.all().exclude(authors__name__in=['Лю Вероника'])
# 2
Article.objects.filter(~Q(authors__name__in=['Лю Вероника']))


# --- 5
Author.objects.all().values('username')


# --- 6
# первый вариант
Publication.objects.filter(Q(author__name='Токтосунова Чынара') | Q(author__name='Лю Вероника'),
                           ~Q(author__date_register='2021-01-04'))


# второй вариант через подзапросы
Publication.objects.filter(author_id__in=Subquery(
        Author.objects.filter(
            Q(name='Токтосунова Чынара') |
            Q(name='Лю Вероника'),
            ~Q(date_register='2021-01-04')
        ).values('id')
    )
)

