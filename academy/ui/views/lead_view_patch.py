lead_form_crm_patch = {
    "key": "lead_form_crm_enhancement",
    "name": "Lead Form - CRM Enhancement",
    "model": "crm.lead",
    "view_type": "form",
    "priority": 10,  # Higher priority (applied earlier)
    "inherit_mode": "extension",
    "inherit_id": "crm_lead_form_view",  # THIS IS THE KEY - points to target view
    "module": "crm",
    "inheritance_operations": [
        {
            "operation": "before",
            "target": "field[name=partner]",
            "content": {
                    "name": "courses",
                    "string": "Courses",
                    "widget": "relation",
                    "displayField": "name",
                    "required": False,
                    "readonly": False,
                    "multiSelect": True,
                    "help": "Courses",
                    "placeholder": "Search courses",
            }
        },
        {
            "operation": "before",
            "target": "field[name=probability]",
            "content": {
                    "name": "teacher",
                    "string": "Teacher",
                    "widget": "relation",
                    "displayField": "name",
                    "required": False,
                    "readonly": False,
                    "multiSelect": False,
                    "help": "Teacher",
                    "placeholder": "Search teacher",
                    "domain": {
                        'filters':{
                            "operator": "and",
                            "filters": [
                                {"field": "teacher", "operator": "eq", "value": True}
                            ]
                        }
                    }
            }
        },
        {
            "operation": "after",
            "target": "field[name=probability]",
            "content": {
                    "name": "started_on",
                    "string": "Started On",
                    "widget": "date",
                    "required": False,
                    "readonly": False,
                    "help": "Started On",
                    "placeholder": "Enter started on",
            }
        },
        {
            "operation": "after",
            "target": "field[name=tags]",
            "content": {
                    "name": "last_action",
                    "string": "Last Action",
                    "widget": "relation",
                    "displayField": "name",
                    "required": False,
                    "readonly": False,
                    "multiSelect": False,
                    "help": "Last Action",
                    "placeholder": "Enter last action",
            }
        },
        {
            "operation": "remove",
            "target": "field[name=expected_revenue]"
        },
        {
            "operation": "remove",
            "target": "field[name=expected_closing]"
        },
    ]
}

