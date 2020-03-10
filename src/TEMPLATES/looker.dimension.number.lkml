{% macro dimension_number(COLUMN) %}
dimension: {{ COLUMN._name }} {
  type: number
  sql: ${TABLE}."{{ COLUMN._name }}__{{ COLUMN._parent._name }}" ;;
  }
{% endmacro %}
