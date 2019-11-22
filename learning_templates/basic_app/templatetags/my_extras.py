from django import template

register = template.Library()

@register.filter(name = 'cut')

def cut(value, arg):
	""" 
	This cuts out all the value of arg from string
	"""
	return value.replace(arg, '')
# register this ,alternate this or the below 
#register.filter('cut', cut)
#another way to register 
# @register.filter(name = 'cut')
