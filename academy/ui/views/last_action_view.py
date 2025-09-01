# -*- coding: utf-8 -*-
# UI Views for academy module
from django.utils.translation import gettext as _

academy_last_action_list_view = {
    "key": "academy_last_action_list_view",
    "name": "Academy Last Action List View",
    "model": "academy.lastaction",
    "view_type": "list",
    "menu_item": "academy_main_menu_last_actions",
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

academy_last_action_form_view = {
    "key": "academy_last_action_form_view",
    "name": "Academy Last Action Form View",
    "model": "academy.lastaction",
    "menu_item": "academy_main_menu_last_actions",
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
                                    "string": _("Last Action Name"),
                                    "widget": "text",
                                    "required": True,
                                    "readonly": False,
                                    "help": _("Last Action name"),
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
                                    "string": _("Last Action Description"),
                                    "widget": "textarea",
                                    "required": False,
                                    "readonly": False,
                                    "help": _("Last Action description"),
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