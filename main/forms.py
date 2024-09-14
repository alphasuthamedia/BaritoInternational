from django.forms import ModelForm
from main.models import Product

# class MoodEntryForm(ModelForm):
#     class Meta:
#         model = MoodEntry
#         fields = ["mood", "feelings", "mood_intensity"]

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "quantity"]