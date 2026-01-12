import json
import yaml
from jsonschema import validate, ValidationError
import os

def load_schema(schema_path):
    with open(schema_path, 'r') as f:
        return yaml.safe_load(f)

def load_data(data_path):
    with open(data_path, 'r') as f:
        return json.load(f)

def validate_taxonomy_data(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("Validation successful!")
        return True
    except ValidationError as e:
        print("Validation failed:")
        print(e.message)
        return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python validation.py <path_to_taxonomy_data.json>")
        sys.exit(1)

    data_file = sys.argv[1]
    schema_file = os.path.join(os.path.dirname(__file__), 'taxonomy.schema.yaml')

    if not os.path.exists(data_file):
        print(f"Error: Data file '{data_file}' not found.")
        sys.exit(1)
    if not os.path.exists(schema_file):
        print(f"Error: Schema file '{schema_file}' not found.")
        sys.exit(1)

    schema = load_schema(schema_file)
    data = load_data(data_file)

    validate_taxonomy_data(data, schema)
