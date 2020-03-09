{% macro dimension_string(COLUMN) %}
dimension: {{ COLUMN._name }} {
  type: string
  sql: ${TABLE}."{{ COLUMN._name }}"
  }
{% endmacro %}
