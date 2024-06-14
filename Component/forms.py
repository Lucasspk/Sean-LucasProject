# forms.py
from django import forms
from .models import GPU, CPU, PSU, Motherboard

class GPUWeightForm(forms.Form):
    rasterization_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Rasterization Weight')
    raytracing_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Raytracing Weight')
    value_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Value Weight')
    max_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False, label='Max Price')


class CPUWeightForm(forms.Form):
    performance_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Performance Weight')
    gaming_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Gaming Weight')
    value_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Value Weight')
    max_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False, label='Max Price')

class PSUWeightForm(forms.Form):
    efficiency_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Efficiency Weight')
    max_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False, label='Max Price')

class MotherboardWeightForm(forms.Form):
    feature_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=True, initial=1, label='Feature Weight')
    max_price = forms.DecimalField(max_digits=9, decimal_places=2, required=False, label='Max Price')



COMPONENT_CHOICES = [
    ('gpu', 'GPU'),
    ('cpu', 'CPU'),
    ('psu', 'PSU'),
    ('motherboard', 'Motherboard'),
]

class ComponentSelectionForm(forms.Form):
    component_type = forms.ChoiceField(choices=COMPONENT_CHOICES, label="Select Component Type")
