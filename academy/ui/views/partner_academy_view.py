partner_academy_form_view = {
    "key": "partner_academy_form_view",
    "name": "Partner Academy Form View",
    "model": "base.partner",
    "view_type": "form",
    "priority": 10,  # Higher priority (applied earlier)
    "inherit_mode": "extension",
    "inherit_id": "base_partner_form_view",  # THIS IS THE KEY - points to target view
    "module": "contacts",
    "inheritance_operations": [
        
        {
            "operation": "before",
            "target": "field[name=parent_id]",
            "content": {
                    "name": "teacher",
                    "string": "Is Teacher",
                    "widget": "switch",
                    "required": False,
                    "readonly": False,
                    "help": "Is Teacher",
            },
            
        },
        {
             "operation": "after",
            "target": "field[name=country_id]",
            "content": {
                    "name": "address",
                    "string": "Address",
                    "widget": "text",
                    'maxLength': 255,
                    "required": False,
                    "readonly": False,
                    "help": "Address",
                    "placeholder": "Enter address",
            },

        },
        {
            "operation": "after",
            "target": "field[name=parent_id]",
            "content": {
                    "name": "age_group",
                    "string": "Age Group",
                    "widget": "relation",
                    "displayField": "name",
                    "required": False,
                    "readonly": False,
                    "help": "Age Group",
                    "placeholder": "Enter age group",
            },

        },
        {
            "operation": "remove",
            "target": "field[name=supplier]"
        },
        {
            "operation": "remove",
            "target": "field[name=industry_id]"
        },
        {
            "operation": "remove",
            "target": "field[name=street]"
        },
         {
            "operation": "remove",
            "target": "field[name=street2]"
        },
         {
            "operation": "remove",
            "target": "field[name=city]"
        },
        {
            "operation": "remove",
            "target": "field[name=state_name]"
        },
        {
            "operation": "remove",
            "target": "field[name=zip]"
        },
    ]
}

