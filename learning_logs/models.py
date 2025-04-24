from django.db import models

class Topic(models.Model):
    """ Тема которую изучает пользователь """
    text = models.CharField(max_length=150)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Возвращает строковое представление модели """
        return self.text
    
class Entry(models.Model):
    """  Статья на определённую тему """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="entries"

    def __str__(self):
        """ Возвращает строковое представление модели """
        return f"{self.text[:50]}..."