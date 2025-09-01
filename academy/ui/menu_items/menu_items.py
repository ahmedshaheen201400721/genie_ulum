# -*- coding: utf-8 -*-
# Menu items for academy module

{
    "academy_main_menu": {
        "name": "Academy",
        "icon": "School",
        "module": "crm",
        "sequence": 50,
        "parent_key": "crm_main_menu",
        "view_type": "list,form",
        "children": {
            "academy_main_menu_courses": {
                "name": "Courses",
                "icon": "School",
                "module": "crm",
                "sequence": 10,
                "model":"academy.course",
                "view_type": "list,form",
            },
            "academy_main_menu_age_groups": {
                "name": "Age Groups",
                "icon": "Monitor",
                "module": "crm",
                "sequence": 20,
                "model":"academy.agegroup",
                "view_type": "list,form",
            },
            "academy_main_menu_last_actions": {
                "name": "Last Actions",
                "icon": "Group",
                "module": "crm",
                "sequence": 30,
                "model":"academy.lastaction",
                "view_type": "list,form",
            },
        }
        
    }
}
