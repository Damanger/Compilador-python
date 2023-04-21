from analizadorLexico import tokens, hash_table, symbol_table
from analizadorSintactico import parse_result

def semantic_analysis(parse_result):
    symbol_table = {}
    type_stack = []
    operation_stack = []
    var_declared = {}
    type_check = {"+": ("ENTERO", "DECIMAL"), 
                  "-": ("ENTERO", "DECIMAL"), 
                  "*": ("ENTERO", "DECIMAL"), 
                  "/": ("ENTERO", "DECIMAL"), 
                  ">": ("ENTERO", "DECIMAL"), 
                  "<": ("ENTERO", "DECIMAL"), 
                  ">=": ("ENTERO", "DECIMAL"), 
                  "<=": ("ENTERO", "DECIMAL"), 
                  "==": ("ENTERO", "DECIMAL", "CADENA", "CARACTER"), 
                  "!=": ("ENTERO", "DECIMAL", "CADENA", "CARACTER")}
    
    for node in parse_result:
        if node[0] == "declare_var":
            var_type = node[1]
            var_name = node[2]
            if var_name in var_declared:
                raise Exception(f"Variable {var_name} already declared at line {var_declared[var_name]}")
            else:
                var_declared[var_name] = node[-1]
                symbol_table[var_name] = var_type
        elif node[0] == "assign_var":
            var_name = node[1]
            var_value = node[2:]
            if var_name not in var_declared:
                raise Exception(f"Variable {var_name} not declared")
            if var_value[0] == "IDENTIFICADOR":
                if var_value[1] not in symbol_table:
                    raise Exception(f"Variable {var_value[1]} not declared")
                var_type = symbol_table[var_value[1]]
            elif var_value[0] in ("NUMERO", "FLOTANTE"):
                var_type = "ENTERO" if var_value[0] == "NUMERO" else "DECIMAL"
            else:
                var_type = var_value[0]
            if symbol_table[var_name] != var_type:
                raise Exception(f"Incompatible types for variable {var_name}. Expected {symbol_table[var_name]} but got {var_type}")
        elif node[0] == "IF":
            if node[1][0] != "IDENTIFICADOR":
                raise Exception(f"Expected variable in condition but got {node[1][0]}")
            if node[1][1] not in symbol_table:
                raise Exception(f"Variable {node[1][1]} not declared")
            if symbol_table[node[1][1]] != "bool":
                raise Exception(f"Expected type bool for variable {node[1][1]} in condition but got {symbol_table[node[1][1]]}")
            if node[2] not in type_check:
                raise Exception(f"Invalid operator {node[2]} in condition")
            if node[3][0] == "IDENTIFICADOR":
                if node[3][1] not in symbol_table:
                    raise Exception(f"Variable {node[3][1]} not declared")
            if symbol_table[node[3][1]] not in type_check[node[2]]:
                raise Exception(f"Incompatible types for operator {node[2]} in condition")
            elif node[3][0] in ("NUMERO", "FLOTANTE"):
                if "ENTERO" not in type_check[node[2]] and "DECIMAL" not in type_check[node[2]]:
                    raise Exception(f"Incompatible types for operator {node[2]} in condition")
                else:
                    if node[3][0] not in type_check[node[2]]:
                        raise Exception(f"Incompatible types for operator {node[2]} in condition")
                    elif node[0] == "FOR":
                        if node[1][0] != "IDENTIFICADOR":
                            raise Exception(f"Expected variable in loop control but got {node[1][0]}")
                if node[1][1] not in symbol_table:
                    raise Exception(f"Variable {node[1][1]} not declared")
                if symbol_table[node[1][1]] != "ENTERO":
                    raise Exception(f"Expected type ENTERO for variable {node[1][1]} in loop control but got {symbol_table[node[1][1]]}")
                if node[2] not in type_check:
                    raise Exception(f"Invalid operator {node[2]} in loop control")
                if node[3][0] == "IDENTIFICADOR":
                    if node[3][1] not in symbol_table:
                        raise Exception(f"Variable {node[3][1]} not declared")
                if symbol_table[node[3][1]] != "ENTERO":
                    raise Exception(f"Expected type ENTERO for variable {node[3][1]} in loop control but got {symbol_table[node[3][1]]}")
                elif node[3][0] != "NUMERO":
                    raise Exception(f"Expected type ENTERO for value in loop control but got {node[3][0]}")
                elif node[0] == "PRENTERO":
                    if node[1][0] == "IDENTIFICADOR":
                        if node[1][1] not in symbol_table:
                            raise Exception(f"Variable {node[1][1]} not declared")
                        elif node[1][0] not in ("NUMERO", "FLOTANTE", "CADENA", "CARACTER"):
                            raise Exception(f"Invalid value for prENTERO statement: {node[1][0]}")
                        elif node[0] in ("+", "-", "*", "/"):
                            if len(type_stack) < 2:
                                raise Exception(f"Invalid expression: not enough operands for operator {node[0]}")
                                op2_type = type_stack.pop()
                                op1_type = type_stack.pop()
                                if (op1_type, op2_type) not in type_check[node[0]]:
                                    raise Exception(f"Incompatible types for operator {node[0]} in expression")
                                if op1_type == "ENTERO" and op2_type == "ENTERO":
                                    type_stack.append("ENTERO")
                                elif op1_type == "DECIMAL" or op2_type == "DECIMAL":
                                    type_stack.append("DECIMAL")
                                else:
                                    raise Exception(f"Invalid types for operator {node[0]} in expression")
                            else:
                                type_stack.append(symbol_table[node[1][1]])

    #Return the final type of the expression
    return type_stack.pop()