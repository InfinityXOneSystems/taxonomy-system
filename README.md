# Taxonomy System

This repository contains the definition and governance for the global semantic taxonomy.

## Structure

- `taxonomy.schema.yaml`: Defines the schema for taxonomy items.
- `rules/`: Directory for validation rules.
- `examples/`: Directory for example taxonomy data.
- `validation.py`: A Python script to validate taxonomy data against the schema and rules.

## Taxonomy Schema (`taxonomy.schema.yaml`)

```yaml
type: object
properties:
  id:
    type: string
    description: Unique identifier for the taxonomy item
  name:
    type: string
    description: Display name of the taxonomy item
  description:
    type: string
    description: Detailed description of the taxonomy item
  parent_id:
    type: string
    description: ID of the parent taxonomy item, if any
  metadata:
    type: object
    additionalProperties: true
    description: Additional metadata for the taxonomy item
required:
  - id
  - name
```

## Validation

Taxonomy data can be validated using the `validation.py` script. This script checks against `taxonomy.schema.yaml` and any custom rules defined in the `rules/` directory.

### Usage

```bash
python validation.py <path_to_taxonomy_data.json>
```

## Examples

See the `examples/` directory for valid and invalid taxonomy data examples.
