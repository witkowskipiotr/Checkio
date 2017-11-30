from django.http import JsonResponse
from permission.compat import get_model

from core.models import CustomUser as User


def validate_username(request):
    if request.is_ajax():
        print(23)
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def autocomplete_name(request):
    name = request.GET.get('name', None)

    result = User.objects.all()
    name = []
    for record in result:
        name.append(record.username + '1')
    name.append('a')
    name.append('ab')
    name.append('abc')
    name.append('abcd')
    name.append('abcde')
    name.append('abcdef')
    data = {'source': name}
    return JsonResponse(data)


def autocomplete_lookup(request, table_lookups):
    term = request.GET.__getitem__('term')
    vals = []
    tables = table_lookups.split(',')
    for table_and_field in tables:
        table, field = table_and_field.split('__')
        model = get_model('sequencing', table)
        filt = {("%s__icontains" % field): term}
        data = list(model.objects.filter(**filt).values_list(field, flat=True))
        vals.extend(data)
    return JsonResponse(vals)
