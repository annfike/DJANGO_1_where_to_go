from django.http import HttpResponse
from django.template import loader

def show_map(request):
    #print('Кто-то зашёл на главную!')
    #return HttpResponse('Здесь будет карта')
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
    #или return render(request, 'index.html')