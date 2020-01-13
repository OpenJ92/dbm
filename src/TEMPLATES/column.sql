{% macro _column(TABLE, COLUMN) -%}
"{{ COLUMN._name }}" as 
{{- TABLE._schema._name | lower}}__
{{- TABLE._name | lower }}__
{{- COLUMN._name | lower }}
{%- endmacro %}


{% macro policy_column(COLUMN) -%}
{{- '{{' -}} 
{{ COLUMN.policy._name }}({{ args }}) as 
{{- COLUMN._name }}_{{ COLUMN.policy._name }}
{{ '}}' }}
{%- endmacro %}
