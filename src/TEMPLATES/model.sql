with src_{{ TABLE_SCHEMA }}_{{ TABLE_NAME }} as (
	select * from {{ "{{" }} source( "{{ TABLE_SCHEMA }}_{{ TABLE_CATALOG}}" , "{{ TABLE_NAME }}" ) {{ "}}" }}
),
renamed_{{ TABLE_SCHEMA }}_{{ TABLE_NAME }} as (
	select
	{% for __column__ in COLUMN_NAME -%}
		"{{ __column__ }}" as {{ TABLE_SCHEMA | lower }}__{{ TABLE_NAME | lower }}__{{ __column__ | lower }}{%- if not loop.last -%} , {%- endif %}
	{% endfor %}
	from
		src_{{ TABLE_SCHEMA }}_{{ TABLE_NAME }}
)
select * from renamed_{{ TABLE_SCHEMA }}_{{ TABLE_NAME }}
