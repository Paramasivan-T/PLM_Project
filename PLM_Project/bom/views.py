from django.shortcuts import render, get_object_or_404
from parts.models import Part
from .models import BOMItem
from django.db.models import Exists, OuterRef
from documents.models import Document  

def bom_detail(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    return render(request, 'bom/bom_detail.html', {'part': part})


def bom_home(request):
    # Get all unique parent part IDs from BOM items
    parent_ids = BOMItem.objects.values_list('parent_id', flat=True).distinct()

    # Annotate parts with a `has_documents` boolean
    parts = Part.objects.annotate(
        has_documents=Exists(
            Document.objects.filter(part=OuterRef('pk'))
        )
    ).filter(id__in=parent_ids).exclude(id__isnull=True)

    return render(request, 'bom/bom_home.html', {'parts': parts})

def get_bom_tree(part):
    """ Recursively fetch BOM tree with documents. """
    items = BOMItem.objects.filter(parent=part)
    tree = []

    for item in items:
        child = item.child
        documents = Document.objects.filter(part=child)
        children = get_bom_tree(child)
        tree.append({
            'item': item,
            'children': children,
            'documents': documents
        })

    return tree

def bom_detail(request, part_id):
    part = get_object_or_404(Part, id=part_id)
    bom_tree = get_bom_tree(part)
    return render(request, 'bom/bom_detail.html', {
        'part': part,
        'bom_tree': bom_tree
    })