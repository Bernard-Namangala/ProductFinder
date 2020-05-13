"""
views for stores app
"""

from django.shortcuts import render
from .models import Store

def storeview(request, store_name):
    """
    store view
    """
    store = Store.objects.get(slug=store_name)
    context = {"store":store}
    return render(request, template_name="stores/store.html", context=context)