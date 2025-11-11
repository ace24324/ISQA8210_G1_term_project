from django.shortcuts import render

# Create your views here.
from .models import Listing
from .models import Events
from django.shortcuts import render
from .models import FilterSelection

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

def index(request):
    objects = Listing.objects.all()  # Fetch all objects from the model
    return render(request, 'index.html', {'objects': objects})

def profile(request):
    """View function for event page of site."""
    # Render the HTML template events_list.html with the data in the context variable
    return render(request, 'G1_term_project/profile.html')

from django.views import generic

class PropListView(generic.ListView):
    model = Listing

class PropDetailView(generic.DetailView):
    model = Listing

class PropDetailCreate(CreateView):
    model = Listing
    fields = ['listing_id', 'description', 'city', 'state', 'zip', 'street_address', 'price', 'prop_features',
    'featured', 'status', 'type', 'prop_neighborhood', 'prop_image1', 'prop_image2', 'prop_image3', 'prop_image4' ]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('listing_list'))


class PropDetailUpdate(UpdateView):
    model = Listing
    fields = ['listing_id', 'description', 'city', 'state', 'zip', 'street_address', 'price', 'prop_features',
              'featured', 'status', 'type', 'prop_neighborhood','prop_image1', 'prop_image2', 'prop_image3', 'prop_image4']
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('listing_detail'))

class EventsListView(generic.ListView):
    model = Events

class EventsDetailView(generic.DetailView):
    model = Events

class EventsDetailCreate(CreateView):
    model = Events
    fields = ['event_id', 'event_identifier', 'event_name', 'event_date', 'event_desc', 'event_link' ]

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('events_list'))


class EventsDetailUpdate(UpdateView):
    model = Events
    fields = ['event_id', 'event_identifier', 'event_name', 'event_date', 'event_desc', 'event_link']
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return HttpResponseRedirect(reverse('events_detail'))

# views.py
from django.shortcuts import render
from django_filters.views import FilterView
from .filters import ListingFilter

class FilteredResultsView(FilterView):
    model = Listing
    filterset_class = ListingFilter
    template_name = 'G1_term_project/filtered_results.html'


# views.py
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from .forms import ListContact


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=['michaelsorum219@gmail.com'],  # Replace with your email
            )
            return render(request, 'G1_term_project/contact_success.html')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'G1_term_project/contact.html', {'form': form})

def list_contact(request):
    if request.method == 'POST':
        form = ListContact(request.POST)
        if form.is_valid():
            # Extract form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=['michaelsorum219@gmail.com'],  # Replace with your email
            )
            return render(request, 'G1_term_project/contact_success.html')  # Redirect to a success page
    else:
        form = ListContact()
    return render(request, 'G1_term_project/list_contact.html', {'form': form})

def contact_success(request):
    # Render the HTML template events_list.html with the data in the context variable
    return render(request, 'G1_term_project/contact_success.html')

