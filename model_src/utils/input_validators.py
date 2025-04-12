def validate_non_empty_string(input_str):
    return isinstance(input_str, str) and bool(input_str.strip())
