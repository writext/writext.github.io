from django.db import models


class Post(models.Model):
    author = models.CharField('Логин автора', max_length=50, default='None')
    author_name = models.CharField('Автора поста', max_length=40, default='None')
    post_title = models.CharField('Название поста', max_length=40)
    post_text = models.TextField('Текст поста')
    post_category = models.CharField('Катигория', max_length=40)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField('Логин автора', max_length=50, default='None')
    author_name = models.CharField('Автор коментария', max_length=40)
    comment_text = models.CharField('Текст коментария', max_length=100)
    pub_date = models.DateTimeField('Дата публикации', default=None)

    def __str__(self):
        return self.author_name