{% macro dimension_number(COLUMN) %}
dimension: {{ COLUMN._name }} {
  type: number
  sql: ${TABLE}."{{ COLUMN._name }}"
  }
{% endmacro %}
