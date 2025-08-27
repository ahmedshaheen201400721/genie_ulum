# -*- coding: utf-8 -*-
# UI Views for academy module
from django.utils.translation import gettext as _

academy_course_list_view = {
    "key": "academy_course_list_view",
    "name": "Academy Course List View",
    "model": "academy.course",
    "view_type": "list",
    "menu_item": "academy_main_menu",
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
                    "help": "Course name",
                },
                {
                    "name": "description", 
                    "widget": "text",
                    "string": _("Description"),
                    "help": "Course description",
                },
                {
                    "name": "instructor",
                    "string": _("Instructor"),
                    "help": "Instructor",
                    "widget": "relation",
                    "displayField": "name",
                },
               
            ]
        }
    }
}

academy_course_form_view = {
    "key": "academy_course_form_view",
    "name": "Academy Course Form View",
    "model": "academy.course",
    "menu_item": "academy_main_menu",
    "view_type": "form",
    "priority": 10,
    "module": "crm",
    "body": {
        "sheet": {
            "groups": [
                {
                    "title": "Course Information",
                    "groups": [
                        {
                            "title": "General Information",
                            "fields": [
                                {
                                    "name": "instructor",
                                    "string": _("Instructor"),
                                    "widget": "relation",
                                    "required": False,
                                    "readonly": False,
                                    "help": _("Instructor"),
                                    "placeholder": "Search...",
                                    "domain": "",
                                    "context": {},
                                    "multiSelect": False,
                                    "creatable": False
                                },
                                {
                                    "name": "name",
                                    "string": _("Course Name"),
                                    "widget": "text",
                                    "required": True,
                                    "readonly": False,
                                    "help": _("Course name"),
                                    "placeholder": "",
                                    "domain": "",
                                    "minLength": None,
                                    "maxLength": 250,
                                    "pattern": None,
                                    "showLengthCounter": True
                                },
                               
                            ],
                    
                        },
                        {
                            "title": "General Information",
                            "fields": [
                                 {
                                    "name": "description",
                                    "string": _("Description"),
                                    "widget": "textarea",
                                    "required": False,
                                    "readonly": False,
                                    "help": _("Course description"),
                                    "placeholder": "",
                                    "domain": "",
                                    "presets": "medium",
                                    "showColorName": True
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