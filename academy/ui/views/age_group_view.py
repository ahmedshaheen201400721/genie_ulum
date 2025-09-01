# -*- coding: utf-8 -*-
# UI Views for academy module
from django.utils.translation import gettext as _

academy_age_group_list_view = {
    "key": "academy_age_group_list_view",
    "name": "Academy Age Group List View",
    "model": "academy.agegroup",
    "view_type": "list",
    "menu_item": "academy_main_menu_age_groups",
    "priority": 20,
    'module': 'crm',
    "body": {
        "tree": {
            "fields": [
                {
                    "name": "id",
                    "widget": "number",
                    "string": _("ID"),
                    "help": True,
                    "formatter": "number"
                },
                {
                    "name": "name", 
                    "widget": "text",
                    "string": _("Name"),
                    "help": " name",
                },
                {
                    "name": "description", 
                    "widget": "text",
                    "string": _("Description"),
                    "help": "description",
                },
            ]
        }
    }
}

academy_age_group_form_view = {
    "key": "academy_age_group_form_view",
    "name": "Academy Age Group Form View",
    "model": "academy.agegroup",
    "menu_item": "academy_main_menu_age_groups",
    "view_type": "form",
    "priority": 10,
    "module": "crm",
    "body": {
        "sheet": {
            "groups": [
                {
                    "title": "Age Group Information",
                    "groups": [
                        {
                            "title": "",
                            "fields": [
                                {
                                    "name": "name",
                                    "string": _("Age Group Name"),
                                    "widget": "text",
                                    "required": True,
                                    "readonly": False,
                                    "help": _("Age Group name"),
                                    "placeholder": "",
                                    "minLength": None,
                                    "maxLength": 250,
                                    "pattern": None,
                                    "showLengthCounter": True
                                },
                               
                            ],
                    
                        },
                        {
                            "title": "",
                            "fields": [
                                 {
                                    "name": "description",
                                    "string": _("Age Group Description"),
                                    "widget": "textarea",
                                    "required": False,
                                    "readonly": False,
                                    "help": _("Age Group description"),
                                    "placeholder": "",
                                },
                                
                            ],
                        }
                    ]
                }
            ],
            "tabs": []
        }
    }
}