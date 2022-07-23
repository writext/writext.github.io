from django.db import models

class Message(models.Model):
    author = models.CharField('Логин автора', max_length=50, default='None')
    author_name = models.CharField('Имя автора сообщения', max_length=40, default='None')
    recipient = models.CharField('Логин получателя', max_length=40, default='None')
    message_text = models.TextField('Текст сообщения')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Messenger'
        verbose_name_plural = 'Messenger'