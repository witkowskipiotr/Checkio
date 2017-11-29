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



class ListBookTable(tables.Table):
    # address = tables.RelatedLinkColumn()
    # user = tables.RelatedLinkColumn()
    user_id = tables.Column('User id', accessor='user.id')
    names = tables.LinkColumn(
        'person', args=[A('pk')],
        text=lambda record: record.name.capitalize() + ' ' + record.surname.capitalize(),

    )
    description = tables.Column()
    user_name_created = tables.Column(accessor='user.username', verbose_name="create user")
    # group = tables.Column(accessor='person.group_set.all()', verbose_name="group")
    # group = ManyToManyColumn(GroupPerson, verbose_name='Groups')
    groups = tables.TemplateColumn(
        template_name="group/table_persons_list_group.html",
        orderable=False)
    detail = tables.TemplateColumn(
        template_name="group/table_persons_detail.html",
        orderable=False)

    # edit = tables.LinkColumn(viewname='Person', urlconf='')
    # addres = tables.Column(accessor='address.city', order_by=('name', 'surname'))

    class Meta:
        model = Person
        template = 'django_tables2/bootstrap.html'
        attrs = {'class': 'table table-bordered table-striped table-hover'}
        # exclude = ('address', 'name', 'surname')
        fields = ('id', 'names', 'user_id', 'groups')
        # sequence = ('id', 'names', 'description', 'user_name_created')


#
# class ListBookTable(tables.Table):
#     # person = tables.RelatedLinkColumn()
#     # group = tables.RelatedLinkColumn()
#
#     person = tables.ManyToManyColumn(transform=lambda person: person.name)
#     group = tables.ManyToManyColumn(transform=lambda group: group.name)
#
#     description = tables.Column(accessor='person.description', orderable=False, )
#     user = tables.Column(accessor='person.user.username', verbose_name="create user", )
#     data_join = tables.DateColumn(format='Y-m-d', verbose_name="Join", order_by='person.name', )
#
#
#     # edit = tables.LinkColumn(viewname='Person', urlconf='')
#     # addres = tables.Column(accessor='address.city', order_by=('name', 'surname'))
#
#     class Meta:
#         model = GroupPerson
#         template = 'django_tables2/bootstrap.html'
#         # attrs = {'class': 'paleblue'}
#         # attrs = {'class': 'paleblue'}
#         attrs = {'class': 'table table-bordered table-striped table-hover'}
#         # exclude = ('id', )
#
#     # def before_render(self, request):
#     #     if request.user.has_perm('foo.delete_bar'):
#     #         self.columns.hide('country')
#     #     else:
#     #         self.columns.show('country')


class ManyToManyColumnUrl(ManyToManyColumn, BaseLinkColumn):

    def transform(self, obj):
        '''
        Override method ManyToManyColumn to use links
        '''
        result = self.render_link(uri=obj.get_absolute_url(), record=obj, value=force_text(obj))
        return result

#
# class ListGroupTable(tables.Table):
#     name = tables.LinkColumn('group:group_detail', args=[A('pk')])
#     person = ManyToManyColumnUrl(verbose_name='Personons')
#     group = ManyToManyColumn()
#     test_template = tables.TemplateColumn("{{ record.id }}", orderable=False)
#
#     class Meta:
#         sequence = ('id', 'name', 'alias', 'secret_key', 'person')
#         model = Group
#         template = 'django_tables2/bootstrap.html'
#         attrs = {'class': 'table table-bordered table-striped table-hover'}
#         exclude = ('group', )

