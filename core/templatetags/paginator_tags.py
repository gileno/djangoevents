#encoding: utf-8

from django.template import Library

register = Library()

@register.inclusion_tag('templatetags/paginate.html')
def paginate(request, paginator, page_obj):
    context = {
        'paginator': paginator,
        'page_obj': page_obj,
    }
    getvars = request.GET.copy()
    if 'page' in getvars:
       del getvars['page']
    if len(getvars.keys()) > 0:
       context['getvars'] = "&%s" % getvars.urlencode()
    else:
       context['getvars'] = ''
    return context