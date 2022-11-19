from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 3, verbose_name = 'Класс')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

class Timetable(models.Model):
    class_init = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Класс')

    first_lesson = models.CharField('first lesson', max_length = 15, null=True, blank=True)
    first_cabinet = models.CharField('first cabinet', max_length = 3, null = True, blank = True)

    second_lesson = models.CharField('second lesson', max_length = 15, null=True, blank=True)
    second_cabinet = models.CharField('second cabinet', max_length = 3, null = True, blank = True)

    thrid_lesson = models.CharField('thrid lesson', max_length = 15, null=True, blank=True)
    thrid_cabinet = models.CharField('thrid cabinet', max_length = 3, null = True, blank = True)

    fourth_lesson = models.CharField('fourth lesson', max_length = 15, null=True, blank=True)
    fourth_cabinet = models.CharField('fourth cabinet', max_length = 3, null = True, blank = True)

    fifth_lesson = models.CharField('fifth lesson', max_length = 15, null=True, blank=True)
    fifth_cabinet = models.CharField('fifth cabinet', max_length = 3, null = True, blank = True)

    sixth_lesson = models.CharField('sixth lesson', max_length = 15, null=True, blank=True)
    sixth_cabinet = models.CharField('sixth cabinet', max_length = 3, null = True, blank = True)

    seventh_lesson = models.CharField('seventh lesson', max_length = 15, null=True, blank=True)
    seventh_cabinet = models.CharField('second cabinet', max_length = 3, null = True, blank = True)

    timetable_date = models.DateField('timetable date')

    short_lesson = models.BooleanField('short lesson')

    short_break = models.BooleanField('short break')