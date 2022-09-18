from itertools import product
from multiprocessing import get_context
from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from .models import items,itemimages
# Create your views here.
class items_list(ListView):
    model=items
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
        return context
