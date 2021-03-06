import pyparsing as pp

operator = pp.Regex(">=|<=|!=|>|<|=").setName("operator")
number = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")
identifier = pp.Word(pp.alphas, pp.alphanums + "_")
comparison_term = identifier | number 
condition = pp.Group(comparison_term + operator + comparison_term)

expr = pp.operatorPrecedence(condition,[
                            ("NOT", 1, pp.opAssoc.RIGHT, ),
                            ("AND", 2, pp.opAssoc.LEFT, ),
                            ("OR", 2, pp.opAssoc.LEFT, ),
                            ])

print expr.parseString("NOT x > 7 AND x < 8 OR x = 4")