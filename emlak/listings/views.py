from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    sorgu_listesi = Listing.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            sorgu_listesi = sorgu_listesi.filter(description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            sorgu_listesi = sorgu_listesi.filter(city__iexact=city)
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            sorgu_listesi = sorgu_listesi.filter(state__iexact=state)
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            sorgu_listesi = sorgu_listesi.filter(bedrooms__lte=bedrooms)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            sorgu_listesi = sorgu_listesi.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': sorgu_listesi,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)