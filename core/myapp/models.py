from django.db import models


class Division(models.Model):
    
    name = models.CharField(
        'Название дивизиона',
        max_length=35,
    )
    
    class Meta:
        verbose_name = 'Дивизион'
        verbose_name_plural = 'Дивизионы'
    
    def __str__(self):
        return self.name


class Company(models.Model):  

    name = models.CharField(
        'Наименование предприятия',
        max_length=35,
    )

    division = models.ForeignKey(
        Division,
        verbose_name='Дивизион',
        on_delete=models.CASCADE,
        related_name="companies"
    )
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
    
    


class Question(models.Model):
     
    company = models.ForeignKey(
        Company,
        verbose_name='Предложенные предприятия',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )


    time_create = models.DateTimeField(
        verbose_name="Время создания",
        auto_now_add=True,
        editable = True
    )

    email = models.EmailField(
        max_length = 254,
        blank = True,
        editable = True
    )

    content = models.TextField(
        verbose_name = 'Ваш вопрос или пожелание',
        max_length = 500,
    )


    class Meta:
        verbose_name = 'Вопрос'
        ordering = ('-time_create',)
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.content
