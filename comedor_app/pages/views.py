from django.shortcuts import render # type: ignore
from datetime import date, timedelta
from .models import DailyMenu, Menu
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # Get the current date
    today = date.today()
    
    # Find the Monday of the current week
    monday = today - timedelta(days=today.weekday())
    
    # Create a list of weekdays (Monday to Friday)
    week_days = []
    for i in range(5):  # 0 = Monday, 4 = Friday
        current_date = monday + timedelta(days=i)
        day_name = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'][i]
        
        # Try to get the menu for this day
        try:
            daily_menu = DailyMenu.objects.get(date=current_date)
        except DailyMenu.DoesNotExist:
            daily_menu = None
            
        week_days.append({
            'date': current_date,
            'name': day_name,
            'menu': daily_menu
        })
    
    # Create a dictionary of all meals for lookup in the template
    meals = {menu.menu_id: menu for menu in Menu.objects.all()}
    
    context = {
        'week_days': week_days,
        'meals': meals,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def history(request):
    # Get all menus up to today, ordered by date descending
    daily_menus = DailyMenu.objects.filter(
        date__lte=date.today()
    ).order_by('-date')
    
    # Create a dictionary of all meals for lookup in the template
    meals = {menu.menu_id: menu for menu in Menu.objects.all()}
    
    context = {
        'daily_menus': daily_menus,
        'meals': meals,
    }
    return render(request, 'history.html', context)

def contact(request):
    return render(request, 'contact.html')

@login_required
def menus_view(request):
    # Get all menus with their categories
    menus = Menu.objects.select_related('category').all()
    
    context = {
        'menus': menus,
        'active_tab': 'menus'  # For highlighting the active sidebar item
    }
    return render(request, 'menus.html', context)
