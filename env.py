from src.CONNECT import CONNECT

from jinja2 import Environment, PackageLoader
import os

if __name__ == '__main__':
    dbt = '/Users/jacobvartuli-schonberg/Knotel/dbt'

    # make connecitons to the raw and analytics databases
    with CONNECT('raw') as raw, CONNECT('analytics') as analytics:

        # pull column information into env from each table
        columns_raw = raw._extract('select * from columns;')
        # columns_analytics = analytics._extract('select * from columns;')
        # columns_dev_analytics = columns_analytics\
        sc = {                                                           \
                f"{schema}"                                              \
                :                                                        \
                {                                                        \
                    f"{table}"                                           \
                    :                                                    \
                    columns_raw[                                         \
                        (columns_raw['TABLE_SCHEMA'] == schema)          \
                        &                                                \
                        (columns_raw['TABLE_NAME'] == table)             \
                               ]                                         \
                    for table in                                         \
                    columns_raw[columns_raw['TABLE_SCHEMA'] == schema]   \
                    ['TABLE_NAME'].unique()                              \
                }                                                        \
                for schema in                                            \
                columns_raw['TABLE_SCHEMA'].unique()                     \
             }

        # operation on segregated table -- dbt file construction

        env = Environment(
                            loader=PackageLoader('src', 'TEMPLATES')
                         )

        TABLE_CATALOG = "RAW"

        for schema, tables in sc.items():
            os.mkdir(f'{dbt}/models/{TABLE_CATALOG}_{schema}/')
            os.mkdir(f'{dbt}/models/{TABLE_CATALOG}_{schema}/base/')
            os.mkdir(f'{dbt}/models/{TABLE_CATALOG}_{schema}/transformed/')
            template = env.get_template('schema.yml')
            with open(f'{dbt}/models/{TABLE_CATALOG}_{schema}/base/schema.yml',\
                    'w+') as a:
                rendered = template.render(                           \
                                 TABLE_SCHEMA=schema,                 \
                                 TABLE_CATALOG=TABLE_CATALOG,         \
                                 TABLES=tables                        \
                               )                                     
                a.write(rendered)

            for name, table in tables.items():
                template = env.get_template('model.sql')
                with open(f'{dbt}/models/{TABLE_CATALOG}_{schema}/base/{schema}_{name}.sql',\
                        'w+') as b:
                    rendered = template.render(                       \
                                    TABLE_SCHEMA=schema,              \
                                     TABLE_NAME=name,                 \
                                     COLUMN_NAME=table['COLUMN_NAME'],\
                                     TABLE_CATALOG=TABLE_CATALOG      \
                                    )                                
                    b.write(rendered)

        # get existing dbt files and place them into an identical structure 
        # as the above query

        # with the files written, we can now move torwards construction of 
        # policy elements for the schema tables and columns. These will dictate 
        # the form of the generation of the schema and model files.

        files = {                                                    \
                    schema                                           \
                    :                                                \
                    [                                                \
                        f'../dbt/models/{schema}/base/'+f            \
                        for f in                                     \
                        os.listdir(f'../dbt/models/{schema}/base/')  \
                        if '.sql' in f                               \
                    ]                                                \
                    for schema in                                    \
                    [                                                \
                        schema                                       \
                        for schema in os.listdir('../dbt/models')    \
                        if "RAW_" in schema                          \
                    ]                                                \
                 }                                                   

        # there's no need to parse the dbt files, because we have a progmatic means
        # of naming convention -- __column__ -> schema__table__column

