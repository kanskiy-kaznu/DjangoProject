from django.db import models

# Create your models here.

# class Jobs(models.Model):
#     #Заголовок
#     title
#     #Зарплата от
#     salary_from
#     # Зарплата до
#     salary_before
#     # Тип занятости
#     type_of_employment
#     #график работа
#     work_schedule
#     #Опыт работы
#     work_experience
#     #Название компаний
#     name_company
#     #Адрес компаний
#     adress_company
#     #Описание
#     descriptions


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Категорий'
        verbose_name_plural = 'Категорий'


class Task_Models(models.Model):
    title = models.CharField(max_length=150)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    descriptions = models.TextField()
    price = models.IntegerField()


    def __str__(self):
        return '{} {}'.format(self.title, self.categories)

    class Meta():
        verbose_name = "Задание"
        verbose_name_plural = "Заданий"