from django.db import models


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Bb(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Товар',
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
    )

    price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=13,
        decimal_places=2,
        verbose_name='Цена',
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='Опубликовано',
    )

    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published']

from django.db import models


class Kiosk(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Parent(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name