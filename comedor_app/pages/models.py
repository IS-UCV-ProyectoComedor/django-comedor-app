from django.db import models # type: ignore

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=50)  # For categories like "Desayuno", "Almuerzo", "Cena"

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Menu categories"

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    principal = models.CharField(max_length=100)
    extra1 = models.CharField(max_length=100)
    extra2 = models.CharField(max_length=100)
    extra3 = models.CharField(max_length=100)
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.PROTECT,  # Prevent deletion of category if menu items exist
        related_name='menus'
    )

    def __str__(self):
        return f"{self.category.name} - {self.principal}"

    class Meta:
        verbose_name_plural = "Menus"

class DailyMenu(models.Model):
    date = models.DateField(unique=True)
    
    breakfast_meals = models.JSONField(null=True, blank=True)  # Store list of meal IDs
    breakfast_drink = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='breakfast_drinks', null=True, blank=True)
    breakfast_servings = models.PositiveIntegerField(default=200)
    
    lunch_meals = models.JSONField(null=True, blank=True)  # Store list of meal IDs
    lunch_drink = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='lunch_drinks', null=True, blank=True)
    lunch_servings = models.PositiveIntegerField(default=1000)
    
    dinner_meals = models.JSONField(null=True, blank=True)  # Store list of meal IDs
    dinner_drink = models.ForeignKey(Menu, on_delete=models.PROTECT, related_name='dinner_drinks', null=True, blank=True)
    dinner_servings = models.PositiveIntegerField(default=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Menu for {self.date}"

    class Meta:
        ordering = ['-date']
        verbose_name = "Daily Menu"
        verbose_name_plural = "Daily Menus"
