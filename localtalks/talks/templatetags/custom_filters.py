from django import template

# Create a new template library to register our custom filter
register = template.Library()


# Register the custom filter using the @register.filter decorator
# The function takes a form as input and renders it as an unordered list
@register.filter
def render_as_list_items(form):
    return form.as_ul()
