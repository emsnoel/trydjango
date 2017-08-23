from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

#from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm

USER_DONT = ['create']
def create_restaurant(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RestaurantLocationCreateForm(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # obj = RestaurantLocation.objects.create(
            #     name = form.cleaned_data['name'],
            #     location = form.cleaned_data['location'],
            #     category = form.cleaned_data['category']
            # )
            form.save()
            return HttpResponseRedirect('/restaurants/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RestaurantLocationCreateForm()

    return render(request, 'restaurants/form.html', {'form': form}) 

def restaurant_listview(request):
    template_name   = 'restaurants/restaurants_list.html'
    queryset        = RestaurantLocation.objects.all()
    context         = {
        'object_list': queryset
    }
    return render(request, template_name, context)  

class RestaurantListView(ListView):
    template_name   = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()

    def get_queryset(self):       
        print(self.kwargs)
        slug = self.kwargs.get('slug')
        print('This slug is : '+slug)
        if slug not in USER_DONT:
            if slug:
                queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                    )
            else:
                queryset = RestaurantLocation.objects.all()

            return queryset
        else:
            return HttpResponseRedirect('/restaurants/r/create/')


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    """
    def get_context_data(self, *args, **kwargs):
        
        print(self.kwargs)
        context     = super(RestaurantDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    
    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj     = get_object_or_404(RestaurantLocation, id = rest_id)
        return obj
    """


class RestaurantLocationCreateView(CreateView):
    form_class = RestaurantCreateForm
    template_name = 'restaurants/form.html'