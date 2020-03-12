{% import 'looker.factory.lkml' as factory %}
view {{ OBJECT._parent._name }}_{{ OBJECT._name }} {
  sql_table_name:
    -- if dev -- {{ '{{' }}_user_attributes['dev_schema']{{ '}}' }}.{{ OBJECT._parent._name }}_{{ OBJECT._name }}
    -- if prod -- {{ '{{' }}_user_attributes['prod_schema']{{ '}}' }}.{{ OBJECT._parent._name }}_{{ OBJECT._name }}
  ;;

{% for COLUMN in OBJECT %}
{{ factory.looker_factory(COLUMN) }}
{% endfor %}

}
