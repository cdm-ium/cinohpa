from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from core.models import Post
from core.models import Entry
from django.http import HttpResponse
from django.template import Context, loader
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator, InvalidPage

def display(request):
    item= Entry.objects.filter(readable_id='178j7b')

    t=loader.get_template('index.html')
    c=Context({'items' : item, })
    return HttpResponse(t.render(c))

def status(request):
    return render_to_response('status.html', 
    context_instance=RequestContext(request))	

def bio(request):
    return render_to_response('bio.html',
    context_instance=RequestContext(request))	

def content(request, entry_id):
    if entry_id:
        items= Entry.objects.filter(readable_id=entry_id).exclude(hide=True)

        t=loader.get_template('content.html')
        c=Context({'items' : items, })
    else:
        import datetime
        items = Entry.objects.exclude(hide=True).order_by('-date')
        #paged = Paginator(items, 5)
        #page_one = paged.page(1)

        t=loader.get_template('content.html')
        c=Context({'items' : items #page_one.object_list, 
                   #'page' : page_one, 
        })
    return HttpResponse(t.render(c))

def content_ajax(request, page):
    import datetime
    items = Entry.objects.exclude(hide=True).order_by('-date')

    paged = Paginator(items, 5)

    try:
        next_page = paginator.page(page)
    except InvalidPage:
        raise Http404

    context = { 
        "object_list": next_page.object_list,
        "page": next_page,
    }
    template = 'content_list.html'
    return direct_to_template(request, template, content, 'text/javascript')




def contact(request):  
    return render_to_response('contact.html',
    context_instance=RequestContext(request))
