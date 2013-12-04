from django.shortcuts import render
from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpRequest


def main(request):
    if request.method == 'GET':
        return show_form(request)
    elif request.method == 'POST':
        return show_result(request)


def show_form(request):
    template = loader.get_template('form.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def show_result(request):
    my_int = request.POST['num']
    # mystring = "You requested %s" % my_int
    template = loader.get_template('squares.html')
    context = RequestContext(request, {'my_int': my_int })
    return HttpResponse(template.render(context))
