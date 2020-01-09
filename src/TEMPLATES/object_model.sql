with src_{{ TABLE._schema._name }}_{{ TABLE._name }} as (
	select * from 
	{{- '{{' -}} 
	source(
		"{{ TABLE._schema._name }}_{{ TABLE._schema._database._name }}",
		"{{ TABLE._name }}"
	      )
	{{ '}}' }}
),
renamed_{{ TABLE._schema._name }}_{{ TABLE._name }} as (
	select
	{% for COLUMN in TABLE._columns -%}
		"{{ COLUMN._name }}" as {{ TABLE._schema._name | lower}}__
					    {{- TABLE._name | lower }}__
					    {{- COLUMN._name | lower }}
					    {%- if not loop.last -%} , {%- endif %}
	{% endfor %}
	from 
	src_{{ TABLE._schema._name }}_{{ TABLE._name }}
)
select * from renamed_{{ TABLE._schema._name }}_{{ TABLE._name }}
