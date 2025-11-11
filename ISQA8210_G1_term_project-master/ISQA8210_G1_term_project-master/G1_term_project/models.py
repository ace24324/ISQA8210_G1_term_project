from datetime import timezone

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from datetime import datetime, time

class UserSearches(models.Model):
    search_id = models.AutoField(primary_key=True)
    param_type = models.CharField(max_length=50)
    param_hood = models.CharField(max_length=50)
    param_price = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['created_at']

    def __int__(self):
        """String for representing the Model object."""
        return self.search_id


class FilterSelection(models.Model):
    filters = models.JSONField()  # Store filter selections as JSON
    timestamp = models.DateTimeField(auto_now_add=True)  # Track when the search was performed

def default_time():
    now = datetime.now()
    return datetime.combine(now.date(), time(22,0))

class Events(models.Model):
    """Model to hold events on event page"""
    event_id = models.AutoField(primary_key=True)
    event_identifier = models.CharField(max_length=8)
    event_name = models.CharField(max_length=50)
    event_date = models.DateTimeField(default=default_time())
    event_desc = models.CharField(max_length=500)
    event_link = models.CharField(max_length=500)

    class Meta:
        ordering = ['event_id']

    def get_absolute_url(self):
        """Returns the URL to access a particular listing instance."""
        return reverse('events_detail', args=[str(self.event_id)])


    def __str__(self):
        """String for representing the Model object."""
        return self.event_identifier


class Listing(models.Model):
    """Model representing a Listing."""
    listing_id = models.CharField(max_length=8)
    description = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    street_address = models.CharField(max_length=100)

    price = models.IntegerField()
    prop_features = models.CharField(max_length=200)
    featured = models.BooleanField(default=False)
    prop_image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    prop_image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    prop_image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    prop_image4 = models.ImageField(upload_to='images/', null=True, blank=True)

    property_status = (('a', 'Available'), ('p', 'Pending'), ('s', 'Sold'),)
    status = models.CharField(
        max_length=1,
        choices=property_status,
        blank=True,
        default='a',
        help_text='Property status',
    )
    property_type = (('t', 'Tudor'), ('r', 'Ranch'), ('s', 'Split-Level'), ('w', 'Townhome'), ('c', 'Condominium'),)
    type = models.CharField(
        max_length=1,
        choices=property_type,
        blank=True,
        default='r',
        help_text='Property type',
    )
    neighborhood = (('a', 'Applewood'), ('w', 'Whitehawk'), ('c', 'Canterbury'), ('b', 'Bellbrook'), ('f', 'Falcon Ridge'),
                    ('g', 'Greyhawk'), ('z', 'Zebra Point'))
    prop_neighborhood = models.CharField(
        max_length=1,
        choices=neighborhood,
        blank=True,
        default='a',
        help_text='Neighborhood',
    )
    class Meta:
        ordering = ['listing_id']

    def get_absolute_url(self):
        """Returns the URL to access a particular listing instance."""
        return reverse('listing_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.listing_id

