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
    ]
}

