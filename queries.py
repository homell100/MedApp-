
CHECK_RECORDS_EXIT_PARAM = "*"
COMMA_SEPARATOR = ","
AND_SEPARATOR = " AND "

#---------------------
#INSERT
#---------------------

TEMPLATE_QUERY_INSERT_TABLE = """
INSERT INTO {table} ({list_col_names})
"""

TEMPLATE_QUERY_INSERT_VALUES = """
VALUES({list_values})
"""

TEMPLATE_QUERY_CHECK_RECORDS_EXIST = """
SELECT
""" + CHECK_RECORDS_EXIT_PARAM + """
FROM
	{table}
WHERE 
"""

CLAUSE_WHERE_VALUE = """
{column_name} = {value}
"""

CLAUSE_WHERE_NULL = """
{column_name} IS NULL
"""
