from django import forms
from category_app.models import Locations, SubCategory


class locationviewform(forms.ModelForm):
    class Meta:
        model = Locations
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subcategories'].queryset = SubCategory.objects.none()

        if 'category_id' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategories'].queryset = SubCategory.objects.filter(category=category_id).order_by('category')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['category'].queryset = self.instance.category.order_by('category')