# 09. Write a Program to identify if a CFG has left-recursion (ambiguity).
#     If present, eliminate it and show the non-ambiguous grammar.

from collections import OrderedDict


def get_grammar():
    """Read grammar interactively from stdin (like program 08)."""
    grammar = OrderedDict()
    print("Enter grammar (space-separated symbols, | for alternatives, # for epsilon):")
    print("Example:  S -> A a | b")
    print("          A -> A c | S d | #\n")
    print("Enter empty line to finish:\n")

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            break

        lhs, _, rhs = line.partition('->')
        lhs = lhs.strip()
        rhs = rhs.strip()

        prods = []
        for alt in rhs.split('|'):
            symbols = alt.strip().split()
            prods.append(symbols if symbols else ['#'])
        grammar[lhs] = prods

    return grammar


def print_grammar(grammar, title="Production Rules"):
    """Pretty-print the grammar."""
    print(f"\n--- {title} ---")
    for lhs, prods in grammar.items():
        alts = [' '.join(p) if p != ['#'] else 'ε' for p in prods]
        print(f"  {lhs} -> {' | '.join(alts)}")


def has_left_recursion(grammar):
    """Check if any rule has immediate left-recursion."""
    for lhs, prods in grammar.items():
        for p in prods:
            if p and p[0] == lhs:
                return True
    return False


def eliminate_left_recursion(grammar):
    """Eliminate immediate left-recursion from the grammar."""
    new_grammar = OrderedDict()
    extra_rules = OrderedDict()

    for lhs, prods in grammar.items():
        alphas = []   # rules starting with lhs (left-recursive)
        betas = []    # rules not starting with lhs

        for p in prods:
            if p and p[0] == lhs:
                alphas.append(p[1:] if len(p) > 1 else [])
            else:
                betas.append(p)

        if not alphas:
            # No left-recursion for this non-terminal
            new_grammar[lhs] = prods
            continue

        # Create new non-terminal: A'
        new_nt = lhs + "'"

        # A  -> beta1 A' | beta2 A' | ...
        new_prods = []
        for b in betas:
            if b == ['#']:
                new_prods.append([new_nt])
            else:
                new_prods.append(b + [new_nt])
        new_grammar[lhs] = new_prods if new_prods else [[new_nt]]

        # A' -> alpha1 A' | alpha2 A' | ... | #
        new_prods2 = []
        for a in alphas:
            new_prods2.append((a if a else []) + [new_nt])
        new_prods2.append(['#'])
        extra_rules[new_nt] = new_prods2

    # Add the new rules at the end
    for nt, prods in extra_rules.items():
        new_grammar[nt] = prods

    return new_grammar


def main():
    grammar = get_grammar()

    if not grammar:
        print("No grammar provided.")
        return

    print_grammar(grammar, "Original Production Rules")

    if has_left_recursion(grammar):
        print("\n⚠ Left-Recursion/Ambiguity risk found! Eliminating dependencies...")
        grammar = eliminate_left_recursion(grammar)
    else:
        print("\n✅ Grammar has no immediate left-recursion issues.")

    print_grammar(grammar, "Processed Production Rules")


if __name__ == "__main__":
    main()