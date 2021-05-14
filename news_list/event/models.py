from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

#User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


    def get_absolut_url(self):
        return reverse('cat', kwargs={'cat_slug':self.slug})

class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назвавание новости')
    text = models.TextField(verbose_name='Текст статьи', null=True)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)#Не изменить после создания
    update_date = models.DateTimeField(auto_now=True)#Изменяется при каждом обновлении строчки в бд
    image = models.ImageField(verbose_name='Изображение',upload_to='photo/%Y/%m/%d/')
    is_publishing = models.BooleanField(default=True)

    category = models.ForeignKey(Category, verbose_name='Категория',on_delete=models.CASCADE)

    def __str__(self):
        result= ''
        return '{} {}'.format(self.title, self.pub_date)


    def get_absolut_url(self):
        return reverse('event', kwargs={'event_slug':self.slug})


class Comment(models.Model):
    #user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, verbose_name='Пост',on_delete=models.CASCADE)

    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(auto_now_add=True)

   # def __str__(self):
    #    return self.user, self.pub_date
