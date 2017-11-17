from django.db import models


class Product(models.Model):
    LIGHT_SABERS = (
        (1, "Red"),
        (1, "Blue"),
        (1, "Green"),
        (1, "Purple"),
    )

    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    available_from = models.DateField(null=True)
    saber = models.IntegerField(choices=LIGHT_SABERS, null=True)


PIZZA_SIZES = (
    (1, "small"),
    (2, "medium"),
    (3, "big"),
)


class Topping(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()


class Pizza(models.Model):
    size = models.IntegerField(choices=PIZZA_SIZES)
    toppings = models.ManyToManyField(Topping, through='PizzaTopps')


TOP_AMOUNT = (
    ('h', 'half'),
    ('n', 'normal'),
    ('d', 'double'),
    ('t', 'triple'),
)


class PizzaTopps(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.CharField(
        max_length=1, choices=TOP_AMOUNT, default='n')
