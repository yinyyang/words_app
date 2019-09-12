from django.shortcuts import render

# Create your views here.
from word import models


def band_listing(request):
    """A view of all bands."""
    words = models.Word.objects.all()
    return render(request, 'word_list.html', {'words': words})
