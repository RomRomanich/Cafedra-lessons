from django.db import models
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler
from django.db.models.signals import post_delete, post_save


class status(ChangeloggableMixin, models.Model):
    title = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ('status')

post_save.connect(journal_save_handler, sender=status)
post_delete.connect(journal_delete_handler, sender=status)

class Teachers(ChangeloggableMixin, models.Model):
    cafedra = models.CharField(max_length=512)
    position = models.CharField(max_length=512)
    FIO = models.CharField(max_length=512)
    birthday = models.DateField(null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Photo")
    telefon = models.CharField(max_length=512, blank=True)
    adress = models.CharField(max_length=512, blank=True)
    comment = models.TextField(verbose_name="Comment")
    status = models.ForeignKey('status', on_delete=models.PROTECT)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name_plural = ('Cafedra teachers')

post_save.connect(journal_save_handler, sender=Teachers)
post_delete.connect(journal_delete_handler, sender=Teachers)


class Students(ChangeloggableMixin, models.Model):
    direction = models.CharField(max_length=512)
    group = models.CharField(max_length=512)
    FIO = models.CharField(max_length=512)
    birthday = models.DateField(null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="Photo")
    telefon = models.CharField(max_length=512, blank=True)
    adress = models.CharField(max_length=512, blank=True)
    comment = models.TextField(blank=True, verbose_name="Comment")
    status = models.ForeignKey('status', on_delete=models.PROTECT)

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name_plural = ('Students')

post_save.connect(journal_save_handler, sender=Students)
post_delete.connect(journal_delete_handler, sender=Students)


#-------- lessonsts base ---------------
class Types(ChangeloggableMixin, models.Model):
    title = models.CharField(max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ('Type list')

post_save.connect(journal_save_handler, sender=Types)
post_delete.connect(journal_delete_handler, sender=Types)


class Lessons(ChangeloggableMixin, models.Model):
    name = models.CharField(max_length=512, verbose_name="Name")
    text = models.TextField(blank=True, verbose_name="Text")
    datetime = models.DateTimeField(null=True, verbose_name="Create date")
    types = models.ForeignKey('types', on_delete=models.PROTECT, verbose_name="Types")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = ('Lessons list')
        ordering = ['-datetime']

post_save.connect(journal_save_handler, sender=Lessons)
post_delete.connect(journal_delete_handler, sender=Lessons)


class Referat(ChangeloggableMixin, models.Model):
    title = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    text = models.TextField(blank=True, verbose_name="Text")
    datetime = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = ('Referat list')
        ordering = ['-datetime']

post_save.connect(journal_save_handler, sender=Referat)
post_delete.connect(journal_delete_handler, sender=Referat)

