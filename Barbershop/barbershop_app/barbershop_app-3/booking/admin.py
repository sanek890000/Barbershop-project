from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from datetime import timedelta
from django.utils.timezone import now


class ЗаявкаАдмин(admin.ModelAdmin):
    # Новое действие: массовое изменение статуса
    actions = ['массовое_изменение_статуса']

    def массовое_изменение_статуса(self, request, queryset):
        rows_updated = queryset.update(статус='новый_статус')
        self.message_user(request, f'{rows_updated} заявок было обновлено.')
    массовое_изменение_статуса.short_description = _('Массовое изменение статуса')

    list_editable = ['статус']

    # Новый столбец, вычисляемое значение: например, возраст заявки
    def возраст_заявки(self, obj):
        return (now() - obj.дата_создания).days
    возраст_заявки.short_description = _('Возраст заявки (дней)')

    list_display = ['id', 'клиент', 'услуга', 'статус', 'дата_создания', 'возраст_заявки']

    # Кастомный фильтр по дате создания
    class ДатаСозданияФильтр(admin.SimpleListFilter):
        title = _('Дата создания')
        parameter_name = 'дата_создания'

        def lookups(self, request, model_admin):
            return (
                ('последняя_неделя', _('Последняя неделя')),
                ('последний_месяц', _('Последний месяц')),
            )

        def queryset(self, request, queryset):
            if self.value() == 'последняя_неделя':
                return queryset.filter(дата_создания__gte=now() - timedelta(weeks=1))
            if self.value() == 'последний_месяц':
                return queryset.filter(дата_создания__gte=now() - timedelta(days=30))

    # Добавление фильтров
    list_filter = ['статус', ДатаСозданияФильтр]

admin.site.register(ЗаявкаАдмин)