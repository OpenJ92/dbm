{% macro dimension_group_time(COLUMN) %}
  dimension_group: {{ COLUMN._name }} {
    type: time
    timeframes: [
      raw,
      time,
      date,
      week,
      month,
      quarter,
      year
    ]
    sql: ${TABLE}."{{ COLUMN._name }}";;
  }
{% endmacro %}

