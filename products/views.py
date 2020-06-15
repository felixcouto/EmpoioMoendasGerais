from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

# Create your views here.

#Class Based View
class ProductListView(ListView):
    #traz todos os produtos do banco de dados sem filtrar nada 
    queryset = Product.objects.all()
    template_name = "products/list.html"
    # def get_context_data(self, *args, **kargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kargs)
    #     print(context)
    #     return context

#Function Based View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)