{% macro column_(TABLE, COLUMN) -%}
"{{ COLUMN._name }}" as {{ TABLE._schema._name | lower}}__
			{{- TABLE._name | lower }}__
		        {{- COLUMN._name | lower }}
{%- endmacro %}


{% macro policy_column(COLUMN) -%}
	{{- '{{' -}} 
	{{ '}}' }}
{%- endmacro %}

