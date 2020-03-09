{% macro looker_factory(COLUMN) %}
{% if COLUMN._data['DATA_TYPE'] == 'NUMBER' %}
{{ dimension_number(COLUMN) }}
{% endif %}
{% if COLUMN._data['DATA_TYPE'] == 'TEXT' %}
{{ dimension_string(COLUMN) }}
{% endif %}
{% if COLUMN._data['DATA_TYPE'] == 'TIMESTAMP_TZ' %}
{{ dimension_group_time(COLUMN) }}
{% endif %}
{% endmacro %}
