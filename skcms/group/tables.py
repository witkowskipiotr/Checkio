import django_tables2 as tables
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django_tables2 import LinkColumn
from django_tables2 import ManyToManyColumn
from django_tables2.columns.linkcolumn import BaseLinkColumn

from .models import Person
from group.models import GroupPerson, Group
from django_tables2.utils import A, Accessor


class ManyToManyColumnUrl(ManyToManyColumn, BaseLinkColumn):

    def transform(self, obj):
        '''
        Override method ManyToManyColumn to use links
        '''
        result = self.render_link(uri=obj.get_absolute_url(), record=obj, value=force_text(obj))
        return result


class ListGroupTable(tables.Table):
    name = tables.LinkColumn('group:group_detail', args=[A('pk')])
    person = ManyToManyColumnUrl(verbose_name='Personons')
    group = ManyToManyColumn()

    class Meta:
        sequence = ('id', 'name', 'alias', 'secret_key', 'person')
        model = Group
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        exclude = ('group', )