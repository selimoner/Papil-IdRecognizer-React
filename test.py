import config

where_to_check = config.config_android

unique_names_with_ocr_type = {}

for inner_dict in where_to_check.values():
    for field_id, field_data in inner_dict["fields"].items():
        field_name = field_data["name"]
        ocr_type = field_data.get("ocr_type")
        if field_name not in unique_names_with_ocr_type:
            unique_names_with_ocr_type[field_name] = ocr_type

print(unique_names_with_ocr_type)
