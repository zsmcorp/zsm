from django.db import models

class Timetable(models.Model):
    class_init = models.CharField('class init', max_length = 3)
    first_lesson = models.CharField('first lesson', max_length = 15)
    second_lesson = models.CharField('second lesson', max_length = 15)
    thrid_lesson = models.CharField('thrid lesson', max_length = 15)
    fourth_lesson = models.CharField('fourth lesson', max_length = 15)
    fifth_lesson = models.CharField('fifth lesson', max_length = 15)
    sixth_lesson = models.CharField('sixth lesson', max_length = 15)
    seventh_lesson = models.CharField('seventh lesson', max_length = 15)
    timetable_date = models.DateField('timetable date')
    short_lesson = models.BooleanField('short lesson')
    short_break = models.BooleanField('short break')

    def __str__(self):
        return self.class_init + ' ' + str(self.timetable_date)