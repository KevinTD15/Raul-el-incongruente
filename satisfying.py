from logic import logic

def unit_clause(formula):
    """
    Takes a formula and returns a list of unit clauses. If none exist, then
    return an empty list
    """
    if formula is None:
        return []

    unit_clauses = []
    for clause in formula:
        if len(clause) == 1:
            unit_clauses.append(clause[0])

    if not unit_clauses:
        return []

    else:
        return unit_clauses

def satisfying_converter(formula):
    form = []
    for i in formula:
        f = []
        for j in i:
            x = False if(j.val) else True
            f.append([j.var, x])
        form.append(f)
    return satisfying_assignment(form)

def satisfying_assignment(formula):
    """
    Find a satisfying assignment for a given CNF formula.
    Returns that assignment if one exists, or None otherwise.

    >>> satisfying_assignment([])
    {}
    >>> x = satisfying_assignment([[('a', True), ('b', False), ('c', True)]])
    >>> x.get('a', None) is True or x.get('b', None) is False or x.get('c', None) is True
    True
    >>> satisfying_assignment([[('a', True)], [('a', False)]])
    """
    
    
    # base case #1
    if formula == []:
        return {}

    # base case #2
    if [] in formula:
        return None

    soln = {}
    unit_clauses = unit_clause(formula)
    # while loop only executes if bool evaluates to true
    while unit_clauses:
        # this will update the formula
        for literal in unit_clauses:
            formula = help_update(formula, (literal[0], literal[1]))
            
            #restate base cases for updated formula
            if [] in formula:
                return None

            soln.setdefault(literal[0], literal[1])
            
            #restated base case for updated formula
            if formula == []:
                return soln
        #recheck if there are any unit clauses in the updated formula
        unit_clauses = unit_clause(formula)

    # the first statement of the formula
    literal = formula[0][0]

    if literal[1] is True:
        switch_bool = False
    else:
        switch_bool = True

    #checking both True and False scenarios
    nu_form = help_update(formula, literal)
    nu_form2 = help_update(formula, (literal[0], switch_bool))

    rec = satisfying_assignment(nu_form)
    if rec is not None:
        soln.update({literal[0]: literal[1]})
        return soln | rec

    rec2 = satisfying_assignment(nu_form2)
    if rec2 is not None:
        soln.update({literal[0]: switch_bool})
        return soln | rec2

    return None

def help_update(formula, literal):
    """
    Given a formula, and a tuple of a variable and its boolean value,
    return an updated formula that simplifies the initial formula, as well
    as a dictionary which has values that are apart of the solution.
    """
    new_formula = []
    for chain in formula:
        new_chain = []
        literal_found = False
        for statement in chain:
            # if the literal is satisfied, then chain does not need to be considered
            if literal in chain:
                literal_found = True

            # if the literal is the opposite of the existing boolean, then the boolean
            # value of the chain is dependent on every OTHER literal
            elif statement[0] == literal[0]:
                continue

            # if not related to the literal, then just add it into the new formula
            new_chain.append(statement)

        # if the literal was not found in the formula, then the chain must be considered
        if not literal_found:
            new_formula.append(new_chain)

    return new_formula