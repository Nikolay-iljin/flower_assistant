# from django import template
#
# from flowers.models import Category, Flowers
#
# register = template.Library()
#
#
# @register.inclusion_tag('flowers/list_category.html')
# def flower_category(cat_select=0):
#     flower_cat = Category.objects.all()
#     return {'category': flower_cat, 'cat_select': cat_select}