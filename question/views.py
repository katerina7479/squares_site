from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseBadRequest


def main(request):
    if request.method == 'GET':
        template = loader.get_template('form.html')

        # The form need the csrf token, so must use RequestContext
        context = RequestContext(request, {})

        # Render and return
        return HttpResponse(template.render(context))

    elif request.method == 'POST':
        # request value returns a string.
        my_int = int(request.POST['num'])

        # Check for valid number
        if my_int > 0 and my_int <= 100:
            template = loader.get_template('squares.html')
            context = RequestContext(request, {'my_int': my_int})
            return HttpResponse(template.render(context))
        else:
            return HttpResponseBadRequest("The number you entered, %s,\
                                          was not between 1 and 100."
                                          % my_int)
