from django.db import models

class Sweet(models.Model):
    CATEGORY_CHOICES = [
        ('chocolate', 'Chocolate'),
        ('candy', 'Candy'),
        ('cake', 'Cake'),
        ('cookie', 'Cookie'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(self.name)