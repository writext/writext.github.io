from django.db import models


class Question(models.Model):
    author = models.CharField('Логин автора', max_length=50, default='None')
    author_name = models.CharField('Автора вопроса', max_length=40)
    question_title = models.CharField('Загаловок вопроса', max_length=40)
    question_text = models.TextField('Текст вопроса')
    question_category = models.CharField('Катигория', max_length=40)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_title

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField('Логин автора', max_length=50, default='None')
    author_name = models.CharField('Автор коментария', max_length=40)
    comment_text = models.CharField('Текст коментария', max_length=100)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.author_name
