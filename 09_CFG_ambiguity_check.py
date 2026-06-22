# 09. Write  a  Program  to  identify  if  a  CFG  is  ambiguous  or  not.  If  ambiguous, remove that and show the non-ambiguous grammar in the output. (any Lang)

class NonTerminal :
    def __init__(self, name) :
        self.name = name
        self.rules = []
    def addRule(self, rule) :
        self.rules.append(rule)
    def setRules(self, rules) :
        self.rules = rules
    def getName(self) :
        return self.name
    def getRules(self) :
        return self.rules
    def printRule(self) :
        print(self.name + " -> ", end = "")
        for i in range(len(self.rules)) :
            print(self.rules[i], end = "")
            if i != len(self.rules) - 1 :
                print(" | ", end = "")
        print()


class Grammar :
    def __init__(self) :
        self.nonTerminals = []

    def addRule(self, rule):
        arrowDefn = "->"
        arrowPos = rule.find(arrowDefn)
        if arrowPos == -1:
            print("Invalid rule format: missing '->'")
            return
        lhs = rule[:arrowPos].strip()
        rhs = rule[arrowPos+len(arrowDefn):].strip()

        prodrules = [alt.strip() for alt in rhs.split('|')]

        nt = NonTerminal(lhs)
        for alt in prodrules:
            nt.addRule(alt)
        self.nonTerminals.append(nt)

    def inputData(self) :
        self.addRule('S->Aa|b')
        self.addRule('A->Ac|Sd|ϵ')

    def printRules(self) :
        for nt in self.nonTerminals :
            nt.printRule()

    def solveNonImmediateLR(self, A, B) :
        nameA = A.getName()
        nameB = B.getName()

        rulesA = A.getRules()
        rulesB = B.getRules()
        newRulesA = []

        for rule in rulesA :
            if rule[0 : len(nameB)] == nameB :
                for rule1 in rulesB :
                    if rule1 == "ϵ":
                        newRulesA.append(rule[len(nameB) : ])
                    else:
                        newRulesA.append(rule1 + rule[len(nameB) : ])
            else :
                newRulesA.append(rule)
        A.setRules(newRulesA)

    def solveImmediateLR(self, A) :
        name = A.getName()
        newName = name + "'"

        alphas = []
        betas = []
        rules = A.getRules()
        newRulesA = []
        newRulesA1 = []

        for rule in rules :
            if rule[0 : len(name)] == name :
                alphas.append(rule[len(name) : ])
            else :
                betas.append(rule)

        if len(alphas) == 0 :
            return

        if len(betas) == 0 or (len(betas) == 1 and betas[0] == "ϵ"):
            newRulesA.append(newName)
        else:
            for beta in betas :
                if beta == "ϵ":
                    newRulesA.append(newName)
                else:
                    newRulesA.append(beta + newName)

        for alpha in alphas :
            newRulesA1.append(alpha + newName)

        A.setRules(newRulesA)
        newRulesA1.append("ϵ")

        nnt = NonTerminal(newName)
        nnt.setRules(newRulesA1)
        self.nonTerminals.append(nnt)

    def hasLeftRecursion(self):
        for nt in self.nonTerminals:
            name = nt.getName()
            for rule in nt.getRules():
                if rule[0 : len(name)] == name:
                    return True
        return False

    def applyAlgorithm(self) :
        is_recursive = self.hasLeftRecursion()
        
        if is_recursive:
            print("\nLeft-Recursion/Ambiguity risk found! Eliminating dependencies...")
            
            original_non_terminals = list(self.nonTerminals)
            size = len(original_non_terminals)
            
            for i in range(size) :
                for j in range(i) :
                    self.solveNonImmediateLR(original_non_terminals[i], original_non_terminals[j])
                self.solveImmediateLR(original_non_terminals[i])
        else:
            print("\nGrammar has no immediate left-recursion issues.")


grammar = Grammar()
grammar.inputData()

print("--- Original Production Rules ---")
grammar.printRules()

grammar.applyAlgorithm()

print("\n--- Processed Production Rules ---")
grammar.printRules()