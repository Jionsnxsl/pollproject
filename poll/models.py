from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(verbose_name="问题内容", max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published')

    class Meta:
        verbose_name = "问题"
        verbose_name_plural = "问题"

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name="投票理由", max_length=200)
    votes = models.IntegerField(verbose_name="投票数量", default=0)

    class Meta:
        verbose_name = "投票"
        verbose_name_plural = "投票"

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class MyImage(models.Model):
    img = models.ImageField(upload_to="img")

# 调用model的delete方法后，删除media中文件
@receiver(pre_delete, sender=MyImage)
def image_model_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.img.delete(False)