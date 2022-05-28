from django import template

register = template.Library()

@register.filter
def index(my_list, index):
    return my_list[index]

@register.filter
def get_file_name(file_path):
    return str(file_path).split('/')[-1]   

@register.simple_tag
def get_number(all,count,page):
    # return 5 * int(page-1) + int(count)
    return all - 5*int(page-1) - int(count)


@register.simple_tag
def get_number(all,count,page):
    # return 5 * int(page-1) + int(count)
    return all - 10*int(page-1) - int(count)

@register.filter
def sub(value,arg):
    return value - arg




