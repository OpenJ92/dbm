with src_{{ OBJECT._parent._name }}_{{ OBJECT._name }} as (
	select * from 
	{{- '{{' -}} 
	source(
		"{{ OBJECT._parent._name }}_
		 {{- OBJECT._parent._parent._name }}",
		"{{ OBJECT._name }}"
	      )
	{{ '}}' }}
),
renamed_{{ OBJECT._parent._name }}_{{ OBJECT._name }} as (
	select
	{% for COLUMN in OBJECT._children -%}
		"{{ COLUMN._name }}" as {{- OBJECT._name | lower }}__
		{{- COLUMN._name | lower }}
		{%- if not loop.last -%} , {%- endif %}
	{% endfor %}
	from 
	src_{{ OBJECT._parent._name }}_{{ OBJECT._name }}
)
select * from renamed_{{ OBJECT._parent._name }}_{{ OBJECT._name }}
