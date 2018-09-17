from django.contrib import admin
from django.apps import apps
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Permission, ContentType
from django.template import Template, Context


def render(src, request=None, **kwargs):
    return Template(src).render(Context(kwargs))


class CorelatedFilter(admin.RelatedFieldListFilter):

    def field_choices(self, field, request, model_admin):
        name = "{}__{}".format(field.name, self.cofield)
        covalue = request.GET.get(name, '')
        if not covalue:
            return field.get_choices(include_blank=False)
        return field.get_choices(
            include_blank=False,
            limit_choices_to={self.cofield: covalue})


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_i18n', 'codename', 'content_type')
    list_filter = [
        # 'group',
        'content_type__app_label',
        ('content_type',
         type('', (CorelatedFilter,), {'cofield': 'app_label'})),
    ]
    search_fields = [
        'name', 'codename', 'content_type__app_label']
    readonly_fields = [
        'name', 'codename', 'content_type_link',
        'name_i18n', 'natural_key',
        'users_list', 'groups_list', ]
    exclude = ['content_type']

    def content_type_link(self, obj):
        ct = obj.content_type
        link = "admin:{}_{}_change".format(
            ct._meta.app_label, ct._meta.model_name)
        modellink = "admin:{}_{}_changelist".format(
            ct.app_label, ct.model)

        return render(
            ''' <a href="{% url link ct.id %}">{{ ct }}</a>
                /<a href="{% url modellink %}">{{ name }}</a>
            ''',
            ct=ct, link=link,
            modellink=modellink, name=str(ct.model_class()))

    content_type_link.short_description = _('Model')
    content_type_link.allow_tags = True

    def name_i18n(self, obj):
        return _(obj.name)

    name_i18n.short_description = _('Name i18n')
    name_i18n.allow_tags = True

    def users_list(self, obj):
        return render('''
        <ul> {% for user in instances %} <li>{{ user }}</li> {% endfor %} </ul>
            ''', instances=obj.user_set.all(), is_admin=True)

    users_list.short_description = _('Users')
    users_list.allow_tags = True

    def groups_list(self, obj):
        return render('''
        <ul> {% for user in instances %} <li>{{ user }}</li> {% endfor %} </ul>
        ''', instances=obj.group_set.all(), is_admin=True)

    groups_list.short_description = _('Groups')
    groups_list.allow_tags = True


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ('app_label', 'model_name', 'model')
    list_filter = ['app_label', ]
    readonly_fields = ('app_label', 'model', 'model_link')

    def model_name(self, obj):
        mc = obj.model_class()
        return mc and mc._meta.verbose_name

    def model_link(self, obj):
        opt = obj.model_class()._meta
        link = "admin:{}_{}_changelist".format(opt.app_label, opt.model_name)
        return render(
            ''' <a href="{% url link %}">{{ opt.verbose_name }}</a>''',
            opt=opt, link=link)

    model_link.short_description = _('Model')
    model_link.allow_tags = True


def register_base():
    admin.site.register(Permission, PermissionAdmin)
    admin.site.register(ContentType, ContentTypeAdmin)