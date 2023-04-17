from blog.models import *

auth1 = Author.objects.create(name='Нурсултан Бердиев', email='nursultanberdiev@gmail.com',
                               username='nursultanberdiev', date_register='04-01-2021')

auth2 = Author.objects.create(name='Лю Вероника', email='ronilyu@gmail.com',
                               username='ronik', date_register='12-03-2023')

auth3 = Author.objects.create(name='Токтосунова Чынара', email='chynara0409@gmail.com',
                               username='chynara', date_register='21-11-2023')


art1 = Article.objects.create(title='Что нужно для разработки мобильных приложений: языки и тренды')
art2 = Article.objects.create(title='Зачем нужно использовать кроссплатформенную систему')
art3 = Article.objects.create(title='Сравниваем Java и Python или с чего лучше начать')
art4 = Article.objects.create(title='Новый ChatGPT-4: в чем его особенность')
art5 = Article.objects.create(title='История компании Boston Dynamics. Как появлялись их роботы')

p1 = Publication.objects.create(author=auth1, article=art1)
p2 = Publication.objects.create(author=auth1, article=art2)
p3 = Publication.objects.create(author=auth1, article=art3)
p4 = Publication.objects.create(author=auth2, article=art4)
p5 = Publication.objects.create(author=auth3, article=art5)

Author.objects.order_by('date_register')

Article.objects.filter(authors__name='Нурсултан Бердиев')

Author.objects.filter(date_register__gt='2022-10-10')

Publication.objects.all().values('author__name', 'article__title')

Publication.objects.all().values_list('author__name', 'article__title')

Publication.objects.filter(author__name__contains='В')








