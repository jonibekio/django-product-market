from django import forms
from .models import Product


class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if data in self.empty_values:
            return []

        if isinstance(data, (list, tuple)):
            return [single_file_clean(item, initial) for item in data if item]

        cleaned = single_file_clean(data, initial)
        return [cleaned] if cleaned else []


class ProductForm(forms.ModelForm):
    images = MultipleFileField(
        widget=MultipleFileInput(attrs={"multiple": True}), required=False
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "brand",
            "category",
            "price",
            "stock",
            "color",
            "warranty_months",
            "images",
        ]
