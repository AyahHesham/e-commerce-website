from itertools import product
from multiprocessing import get_context
from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import items,itemimages,cateogry,brand
from django.db.models import Count,Q


def postList(requset):
    objects=items.objects.all()
    #use filter
    #gt=greater than
    #lt=lettle than
    #lte=lettle than or equal the same in gte
    #objects=items.objects.filter(price__gt=30)
    #objects=items.objects.filter(price__range=[30,100])
    #objects=items.objects.filter(cateogry__id__gt=10)
    #objects=items.objects.filter(cateogry__id__lt=10)
    #objects=items.objects.filter(name__contains='k')
    #objects=items.objects.filter(name__startswith='k')
    #objects=items.objects.filter(name__endswith='r')
    #objects=items.objects.filter(name__isnull=True)
    #or
    #objects=items.objects.filter(Q(price__gt=30)|Q(name__startswith='k'))
    #not and
    #objects=items.objects.filter(Q(price__gt=30)&~Q(name__startswith='k'))
    #and
    #objects=items.objects.filter(Q(price__gt=30)&Q(name__startswith='k'))


    return render(requset,'prouducts/test_list.html',{'items':objects})
# Create your views here.
class items_list(ListView):
    model=items
    #paginate is function in cbv
    paginate_by=20
# there are method in detail veiw contain the context two get details of the model but i want show the image from the second
#model in second class "proudct image " to show them by other context so i will make override
class itemsDetail(DetailView):
    model=items
    #override to immplemnt the fun in the two classes
    def get_context_data(self, **kwargs):
        #super responsable of implemint the context in the first class then implement the other context
        # detail , edit ,delete that deploy on one thing there are function speacial for them ----> get_object
        context=super().get_context_data(**kwargs)
        #item isthe product with the the id in url
        myitem=self.get_object()
        #the second fun will immplement by second contesxt from other class
        context["image"]=itemimages.objects.filter(items=myitem)
        context["related"]=items.objects.filter(cateogry=myitem.cateogry)#[1:10]#toslice
        return context

class brand_list(ListView):
    model=brand
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["brands"]=brand.objects.all().annotate(items_count=Count('brand_item'))
        return context


class brand_detail(DetailView):
    model=brand
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        brand=self.get_object()
        context["brand_product"]=items.objects.filter(brand=brand)
        return context

class category_list(ListView):
    model=cateogry
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["cateogry"]=cateogry.objects.all().annotate(items_count=Count('cateogry_item'))
        return context