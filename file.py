import sqlparse
import re

def obfuscate_query(sql_query):
    parsed = sqlparse.parse(sql_query)
    
    obfuscated_query = ""
    
    for statement in parsed:
        for token in statement.tokens:
            if isinstance(token, sqlparse.sql.IdentifierList):
                obfuscated_query += obfuscate_identifiers(token)
            else:
                obfuscated_query += str(token)
    
    return obfuscated_query

def obfuscate_identifiers(identifier_list):
    obfuscated_identifiers = []
    
    for identifier in identifier_list.get_identifiers():
        obfuscated_identifiers.append("x" + str(len(obfuscated_identifiers) + 1))
    
    return ", ".join(obfuscated_identifiers)

# Example usage
original_query = "SELECT id, username FROM users WHERE status = 'active';"
obfuscated_query = obfuscate_query(original_query)
print("Original Query:", original_query)
print("Obfuscated Query:", obfuscated_query)