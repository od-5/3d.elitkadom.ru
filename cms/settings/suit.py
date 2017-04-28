# coding=utf-8

__author__ = 'alexy'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'Панель администратора',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        'sites',
        {'label': u'Перейти на сайт', 'icon': 'icon-eye-open', 'url': '/'},
        {'label': u'Пользователи', 'icon': 'icon-user', 'models': ('auth.user', 'auth.group',), 'permissions': (
            'auth.add_user', )},
        {'label': u'Настройки', 'icon': 'icon-cog', 'models': ('landing.setup',), 'permissions': (
            'landing.add_setup', )},
        {'label': u'Город', 'icon': 'icon-map-marker', 'models': ('landing.city',), 'permissions': (
            'landing.add_city', )},
        {'label': u'Контент', 'icon': 'icon-edit', 'models': (
            'landing.video', 'landing.why', 'landing.service', 'landing.review', 'landing.thanks', 'landing.gallery',
            'landing.client', 'landing.cost'
        ), 'permissions': 'landing.add_video'},
        {'label': u'Заявки', 'icon': 'icon-list-alt', 'models': ('ticket.ticket',)},
        {'label': u'Адреса', 'icon': 'icon-map-marker', 'models': ('landing.cityhouse',), },
    ),
}
