with src_{{ TABLE._parent._name }}_{{ TABLE._name }} as (
	select * from 
	{{- '{{' -}} 
	source(
		"{{ TABLE._parent._name }}_
		 {{- TABLE._parent._parent._name }}",
		"{{ TABLE._name }}"
	      )
	{{ '}}' }}
),
renamed_{{ TABLE._parent._name }}_{{ TABLE._name }} as (
	select
	{% for COLUMN in TABLE._children -%}
		"{{ COLUMN._name }}" as {{ TABLE._parent._name | lower}}__
		{{- TABLE._name | lower }}__
		{{- COLUMN._name | lower }}
		{%- if not loop.last -%} , {%- endif %}
	{% endfor %}
	from 
	src_{{ TABLE._parent._name }}_{{ TABLE._name }}
)
select * from renamed_{{ TABLE._parent._name }}_{{ TABLE._name }}
