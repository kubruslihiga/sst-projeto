from django import template
from django.forms import CheckboxInput, TextInput, Textarea, RadioSelect

register = template.Library()

@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

@register.filter(name='is_text')
def is_text(field):
    names = [TextInput().__class__.__name__, Textarea().__class__.__name__]
    return names in field.field.widget.__class__.__name__

@register.filter(name='is_radio')
def is_radio(field):
    names = [RadioSelect().__class__.__name__]
    return names in field.field.widget.__class__.__name__

@register.filter(name='is_checkbox_or_radio')
def is_checkbox_or_radio(field):
    names = [CheckboxInput().__class__.__name__, RadioSelect().__class__.__name__]
    return field.field.widget.__class__.__name__ in names
