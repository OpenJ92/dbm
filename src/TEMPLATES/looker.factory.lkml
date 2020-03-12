{% import 'looker.dimension.number.lkml' as dimension_number %}
{% import 'looker.dimension.string.lkml' as dimension_string %}
{% import 'looker.dimension_group.time.lkml' as dimension_group_time %}

{% macro looker_factory(COLUMN) %}
{% if COLUMN._data['DATA_TYPE'] == 'NUMBER' %} {{ dimension_number.dimension_number(COLUMN) }} {% endif %}
{% if COLUMN._data['DATA_TYPE'] == 'TEXT' %} {{ dimension_string.dimension_string(COLUMN) }} {% endif %}
{% if COLUMN._data['DATA_TYPE'] == 'TIMESTAMP_TZ' %} {{ dimension_group_time.dimension_group_time(COLUMN) }} {% endif %}
{% endmacro %}
