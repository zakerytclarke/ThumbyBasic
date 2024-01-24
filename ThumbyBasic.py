import time
import os

PATH = "./"

def refresh_display():
    print("THUMBY BASIC")

def input_select(options):
    return input("Filename:")

def find_basic_files(path):
    return []


try: # Running on Thumby
    import thumby

    PATH = "./Games/ThumbyBasic"
    thumby.display.setFont("/lib/font5x7.bin", 5, 7, 1)

    print_values = ["THUMBY BASIC","LOADING...","",""]
    INPUT_STRING = "9876543210 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"

    input_values = [10]

    def find_basic_files(path):
        output = []
        try:
            for x in os.listdir(path):
                if ".bas" in x:
                    output.append(x.split("/")[-1])
        except:
            print("ERR Loading Program")
            
        return output
    def input_select(options):
        input_cursor = 0
        def update():
            print("THUMBY BASIC")
            print("SELECT PRGM")
            print(options[input_cursor])
            print(" <--------> ")
            
        update()
        while not thumby.buttonA.pressed():
            if thumby.buttonL.pressed():
                if input_cursor > 0:
                    input_cursor -= 1
                else:
                    input_cursor = len(options) - 1  # Loop to the last element
                update()
            if thumby.buttonR.pressed():
                if input_cursor < len(options) - 1:
                    input_cursor += 1
                else:
                    input_cursor = 0  # Loop to the first element
                update()
                                
            refresh_display()
            time.sleep(0.2)
                    
        return options[input_cursor]

    def refresh_display():
        thumby.display.fill(0)
        thumby.display.drawText(print_values[0], 0, 0, 1)
        thumby.display.drawText(print_values[1], 0, 8, 1)
        thumby.display.drawText(print_values[2], 0, 16, 1)
        thumby.display.drawText(print_values[3], 0, 24, 1)
        thumby.display.drawText("?" + "".join(map(lambda x:INPUT_STRING[x], input_values)), 0, 32, 1)
        thumby.display.update()
        

    def print(txt=""):
        print_values[0] = print_values[1]
        print_values[1] = print_values[2]
        print_values[2] = print_values[3]
        print_values[3] = str(txt)
        refresh_display()
        

    def input(txt=""):
        global input_values
        input_cursor = 0
        while not thumby.buttonA.pressed():
            if thumby.buttonD.pressed():
                if input_values[input_cursor] < len(INPUT_STRING):
                    input_values[input_cursor] += 1
            if thumby.buttonU.pressed():
                if input_values[input_cursor] > 0:
                    input_values[input_cursor] -= 1
            if thumby.buttonL.pressed():
                if input_cursor > 0:
                    input_cursor -= 1
            if thumby.buttonR.pressed():
                if input_cursor < len(input_values):
                    input_values.append(10)
                    input_cursor += 1
            refresh_display()
            time.sleep(0.2)
        
        input_txt = "".join(map(lambda x:INPUT_STRING[x], input_values))
        input_values = [10]
        return input_txt
        


        
except:
    pass # Running on computer


class Terminal:
    def __init__(self, token):
        self.token = token

def unwrap_singleton_list(input_list):
    while isinstance(input_list, list) and len(input_list) == 1:
        input_list = input_list[0]
    if(len(input_list)) > 1:
        return input_list
    else:
        return [input_list]

class NonTerminal:
    def __init__(self, rules, fn=unwrap_singleton_list, parse_fn=None):
        self.rules = rules  # List of Rules to OR Match
        self.fn = fn
        self.parse_fn = parse_fn

def infixoperation(tokens):
    if(len(tokens)==3 and isinstance(tokens[1], str)):
        return {
            "op":tokens[1].strip(),
            "args":[
                unwrap_singleton_list(tokens[0])[0] if(isinstance(tokens[0], list)) else tokens[0],
                unwrap_singleton_list(tokens[2])[0] if(isinstance(tokens[2], list)) else tokens[2]
            ]
        }
    else:
        return unwrap_singleton_list(tokens)
    
def infixstatement(tokens):
    if(len(tokens)==3 and isinstance(tokens[1], str)):
        return {
            "action":tokens[1].strip(),
            "args":[
                unwrap_singleton_list(tokens[0])[0] if(isinstance(tokens[0], list)) else tokens[0],
                unwrap_singleton_list(tokens[2])[0] if(isinstance(tokens[2], list)) else tokens[2]
            ]
        }
    else:
        return unwrap_singleton_list(tokens)


def statementoperation(tokens):
    if tokens[0] == "GOTO ":
        return {
        "action":tokens[0].strip(),
            "args": tokens[1][0]
        }
    if tokens[0] == "PRINT ":
        return {
        "action":tokens[0].strip(),
            "args": list(map(lambda x: unwrap_singleton_list(x)[0] if(isinstance(x, list)) else x ,tokens[1:][0]))
        }
    
    return {
        "action":tokens[0].strip(),
        "args": list(map(lambda x: unwrap_singleton_list(x)[0] if(isinstance(x, list)) else x ,tokens[1:]))
    }
# def prefixoperation(tokens):
#     if(isinstance(tokens[0], str)):
#         return {
#             "op":tokens[0],
#             "args":[
#                 unwrap_singleton_list(tokens[0])[0] if(isinstance(tokens[0], list)) else tokens[0],
#                 unwrap_singleton_list(tokens[2])[0] if(isinstance(tokens[2], list)) else tokens[2]
#             ]
#         }
#     else:
#         return unwrap_singleton_list(tokens)

def if_parser(tokens):
    if len(tokens)==4:
        return {
            "op":"IF",
            "args":[
                unwrap_singleton_list(tokens[1]),
                unwrap_singleton_list(tokens[3])
            ]
        }
    elif len(tokens)==6:
        result =  {
            "op":"IF",
            "args":[
                unwrap_singleton_list(tokens[1]),
                unwrap_singleton_list(tokens[3]),
                unwrap_singleton_list(tokens[5])
            ]
        }
        return result
    return unwrap_singleton_list(tokens)

def parse_terminals_many(allowed_characters):
    def inner(input_str):
        parsed_characters = ""
        
        while(len(input_str)>0 and input_str[0] in allowed_characters):
            parsed_characters += input_str[0]
            input_str = input_str[1:]
        
        if parsed_characters=="":
            return None
        return ([parsed_characters], input_str)
    return inner

def temp_parser(tokens):
    # breakpoint()
    if len(tokens)==3:
        return [unwrap_singleton_list(tokens[0][0]), unwrap_singleton_list(tokens[2][0])]
    return [unwrap_singleton_list(tokens)]

GRAMMAR = {
    "LETTER": NonTerminal([
        [Terminal("A")],
        [Terminal("B")],
        [Terminal("C")],
        [Terminal("D")],
        [Terminal("E")],
        [Terminal("F")],
        [Terminal("G")],
        [Terminal("H")],
        [Terminal("I")],
        [Terminal("J")],
        [Terminal("K")],
        [Terminal("L")],
        [Terminal("M")],
        [Terminal("N")],
        [Terminal("O")],
        [Terminal("P")],
        [Terminal("Q")],
        [Terminal("R")],
        [Terminal("S")],
        [Terminal("T")],
        [Terminal("U")],
        [Terminal("V")],
        [Terminal("W")],
        [Terminal("X")],
        [Terminal("Y")],
        [Terminal("Z")],
        [Terminal("a")],
        [Terminal("b")],
        [Terminal("c")],
        [Terminal("d")],
        [Terminal("e")],
        [Terminal("f")],
        [Terminal("g")],
        [Terminal("h")],
        [Terminal("i")],
        [Terminal("j")],
        [Terminal("k")],
        [Terminal("l")],
        [Terminal("m")],
        [Terminal("n")],
        [Terminal("o")],
        [Terminal("p")],
        [Terminal("q")],
        [Terminal("r")],
        [Terminal("s")],
        [Terminal("t")],
        [Terminal("u")],
        [Terminal("v")],
        [Terminal("w")],
        [Terminal("x")],
        [Terminal("y")],
        [Terminal("z")],
    ]),
    "DIGIT": NonTerminal([
        [Terminal("0")],
        [Terminal("1")],
        [Terminal("2")],
        [Terminal("3")],
        [Terminal("4")],
        [Terminal("5")],
        [Terminal("6")],
        [Terminal("7")],
        [Terminal("8")],
        [Terminal("9")],
    ]),

    "VARIABLE": NonTerminal([
        ["LETTER", "VARIABLE"],
        ["LETTER"],
    ], fn=(lambda tokens: tokens[0] if len(tokens)==1 else ["".join(list(map(lambda x:x[0], tokens)))]), parse_fn=parse_terminals_many(["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])),
    "INTEGER": NonTerminal([
        ["DIGIT", "INTEGER"],
        ["DIGIT"],
    ], fn=(lambda tokens: tokens[0] if len(tokens)==1 else ["".join(list(map(lambda x:x[0], tokens)))]), parse_fn=parse_terminals_many(["0","1","2","3","4","5","6","7","8","9"])),
    "FLOAT": NonTerminal([
        ["INTEGER", Terminal(".") ,"INTEGER"],
        ["INTEGER"],
    ], (lambda tokens: tokens[0] if len(tokens)==1 else ["".join(list(map(lambda x:x[0], tokens)))])),
    "BOOLEAN": NonTerminal([
        [Terminal("TRUE")],
        [Terminal("FALSE")],
    ]),

    'CONSTANT': NonTerminal([
        ["FLOAT"],
        ["VARIABLE"]
    ]),


    "FUNC_NAME":NonTerminal([
        [Terminal("STR")],
        [Terminal("INT")],
        [Terminal("SIN")],
        [Terminal("COS")],
        [Terminal("TAN")],
        [Terminal("ASIN")],
        [Terminal("ACOS")],
        [Terminal("ATAN")],        
        [Terminal("CEIL")],
        [Terminal("FLOOR")],
        [Terminal("ROUND")],
    ]),

    "FUNCTION": NonTerminal([
        ["FUNC_NAME", Terminal("("), "EXPRESSION", Terminal(")")],
        [Terminal("("), "EXPRESSION", Terminal(")")],
        ["CONSTANT"]
    ]),    
    "FACTOR": NonTerminal([
        ["FUNCTION", Terminal("^"), "FACTOR"],
        ["FUNCTION"],
    ], infixoperation),    
    "TERM": NonTerminal([
        ["FACTOR", Terminal("*"), "TERM"],
        ["FACTOR", Terminal("/"), "TERM"],
        ["FACTOR"],
    ], infixoperation),
    "EXPRESSION": NonTerminal([
        ["TERM", Terminal("+"), "EXPRESSION"],
        ["TERM", Terminal("-"), "EXPRESSION"],
        ["TERM"],
    ], infixoperation),



    "BOOLOP": NonTerminal([
        [Terminal("("), "BOOLEXPRESSION", Terminal(")")],
        ["EXPRESSION", Terminal("="), "EXPRESSION"],
        ["EXPRESSION", Terminal("!="), "EXPRESSION"],
        ["BOOLEAN"],
    ], infixoperation),
    "BOOLFACTOR": NonTerminal([
        [Terminal("NOT"), "BOOLOP"],
        ["BOOLOP"],
    ]),
    "BOOLTERM": NonTerminal([
        ["BOOLFACTOR", Terminal(" AND "), "BOOLTERM"],
        ["BOOLFACTOR"],
    ], infixoperation),
    "BOOLEXPRESSION": NonTerminal([
        ["BOOLTERM", Terminal(" OR "), "BOOLEXPRESSION"],
        ["BOOLTERM"],
    ], infixoperation),

    
    "GOTOSTATEMENT": NonTerminal([
        [Terminal("GOTO "), "INTEGER"],
    ], statementoperation),
    "ASSIGNMENT": NonTerminal([
        ["VARIABLE", Terminal("="), "EXPRESSION"],
        ["GOTOSTATEMENT"],
        ["PRINTSTATEMENT"],
        ["INPUTSTATEMENT"],
    ], infixstatement),
    "INPUTSTATEMENT": NonTerminal([
        [Terminal("INPUT "), "VARIABLE"],
    ], statementoperation),
    "PRINTEXPRESSION": NonTerminal([
        ["EXPRESSION", Terminal(", "), "PRINTEXPRESSION"], # Allows print multiple comma separateed expression
        ["EXPRESSION"]
    ], temp_parser),
    "PRINTSTATEMENT": NonTerminal([
        [Terminal("PRINT "), "PRINTEXPRESSION"],
    ], statementoperation),
    "IFSTATEMENT": NonTerminal([
        [Terminal("IF "), "BOOLEXPRESSION", Terminal(" THEN "), "ASSIGNMENT", Terminal(" ELSE "), "ASSIGNMENT"],
        [Terminal("IF "), "BOOLEXPRESSION", Terminal(" THEN "), "ASSIGNMENT"],
        ["ASSIGNMENT"]
    ], if_parser),
    "CLSSTATEMENT": NonTerminal([
        [Terminal("CLS")],
    ], statementoperation),
    "ENDSTATEMENT": NonTerminal([
        [Terminal("END")],
    ], statementoperation),
    "STATEMENT": NonTerminal([
        ["CLSSTATEMENT"],
        ["ENDSTATEMENT"],
        ["PRINTSTATEMENT"],
        ["INPUTSTATEMENT"],
        ["IFSTATEMENT"],
    ]),
    "LINESTATEMENT": NonTerminal([
        ["INTEGER", Terminal(" "), "STATEMENT"],
    ], lambda tokens: dict({tokens[0][0]:tokens[2]})),
    
}


def parse(input_str, rule, depth=0):
    def parse_terminal(input_str, token):
        if input_str.startswith(token):
            return (token, input_str[len(token):])
        else:
            return None

    if isinstance(rule, Terminal):
        result = parse_terminal(input_str, rule.token)
        if result is not None:
            token, remaining_input = result
            return (rule.token, remaining_input)
        else:
            return None

    elif isinstance(rule, NonTerminal):
        if rule.parse_fn is None:
            for ruleset in rule.rules:
                remaining_input = input_str
                output = []
                for subrule in ruleset:
                    result = parse(remaining_input, subrule, depth=depth+1)
                    if result is not None:
                        matched_token, remaining_input = result
                        output.append(matched_token)
                    else:
                        break  # If any subrule fails, break out of this ruleset
                if len(output) == len(ruleset):
                    return (rule.fn(output), remaining_input)
        else:
            return rule.parse_fn(input_str)

    elif isinstance(rule, str):
        return parse(input_str, GRAMMAR[rule])

def parse_statement(statement):
    result = parse(statement, GRAMMAR["LINESTATEMENT"])
    if result is not None:
        matched_tokens, remaining_input = result
        if len(remaining_input) == 0:
            return matched_tokens
        else:
            print("Err: Parsing failed")
            print(statement)
            print("".join([" "]*(len(statement)-len(remaining_input)))+"".join(["^"]*len(remaining_input)))
    else:
        print("Err: Parsing failed, no match found.")
        print(statement)
        print("".join(["^"]*len(statement)))
        



def parse_numbers_variables(x, state):
    try: # Identifier is a number
        return float(x)
    except ValueError: # Variable
        if x in state['variables']:
            return state['variables'][x]
        else: # String
            return x
            print(f"ERR: Var {x} not defined")
            raise BaseException(f"Variable {x} not defined")


def evaluate(node, state):
    if isinstance(node, str):
        return parse_numbers_variables(node, state)
    if "action" in node:
        if node["action"] == "CLS":
            pass
        if node["action"] == "END":
            pass
        if node["action"] == "INT":
            pass
        if node["action"] == "STR":
            pass
        if node["action"] == "PRINT":
            print("".join(list(map(lambda x:str(evaluate(x,state)), node["args"]))))
        if node["action"] == "INPUT":
            result = input()
            try: # Valid integer
                result = float(result)
            except ValueError: # String
                pass

            state["variables"][node["args"][0]] = result
            
        if node["action"] == "=": # Assignment
            state["variables"][node["args"][0]] = parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["action"] == "GOTO":
            state["line_number"] = node["args"]
    
    if "op" in node:
        if node["op"] == "=":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) == parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "+":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) + parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "-":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) - parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "*":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) * parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "/":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) / parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "^":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) ** parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "OR":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) or parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "AND":
            return parse_numbers_variables(evaluate(node["args"][0], state), state) and parse_numbers_variables(evaluate(node["args"][1], state), state)
        if node["op"] == "IF":
            if_expr = evaluate(node["args"][0], state)
            if if_expr:
                return evaluate(node["args"][1], state)
            else:
                if len(node["args"]) != 2: # Else statement included
                    return evaluate(node["args"][2], state)
            
    return state


def run_prgm(prgm_txt):
    print("THUMBY BASIC")
    print("LOADING...")
    print("")
    print("")
    refresh_display()
    
    parsed = {key: value for d in list(map(parse_statement, prgm_txt.strip().split("\n"))) for key, value in d.items()}
    
    print("")
    print("")
    
    line_numbers = list(map(str, sorted(list(map(int, parsed.keys())))))

    state = {"line_number":line_numbers[0],"variables":{}}
    
    # Fetch Current Statement
    while(1):
        current_line_number = state["line_number"]

        
        if current_line_number in parsed:
            current_statement = parsed[current_line_number]
        else:
            print(f"ERR: Line Number {current_line_number} not found ")
            return
        
        
        # EXECUTE STATEMENT
        state = evaluate(current_statement, state)
        if state["line_number"] == current_line_number: # GOTO not called
            next_line_idx = line_numbers.index(current_line_number) + 1
            if next_line_idx >= len(line_numbers):
                break
            else:
                state["line_number"] = line_numbers[next_line_idx]


refresh_display()



    


try: # Program Selector
    prgm_path = PATH + "/" + input_select(find_basic_files(PATH))
    prgm_txt = open(prgm_path, "r").read()
    try:
        run_prgm(prgm_txt)
    except Exception as e:
        print(f"ERR:{e}")
    
        
except Exception as e:
    print(e)
    print("File does not exist")


input("DONE")
time.sleep(1)


