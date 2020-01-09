with src_{{ TABLE._schema._name }}_{{ TABLE._name }} as (
	select * from 
	{{ '{{' }} 
	source(
		"{{ TABLE._schema._name }}_{{ TABLE._schema._database._name }}",
		"{{ TABLE._name}}"
	      )
	{{ '}}' }}
),
renamed_{{ TABLE._schema._name }}_{{ TABLE._name }} as (
	select
	{% for __column__ in TABLE._columns -%}
