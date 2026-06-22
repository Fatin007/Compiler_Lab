# 08. Write  a  program  to  calculate  the  FIRST() and FOLLOW() of a given grammar. (any Lang)

from collections import defaultdict


def first_of(grammar, first, nt):
    """Compute FIRST of a single non-terminal (recursive with memo)."""
    if nt in first:
        return first[nt]

    first[nt] = set()
    for prod in grammar[nt]:
        if prod == ['#']:                   # epsilon
            first[nt].add('#')
            continue

        all_nullable = True
        for sym in prod:
            if sym not in grammar:           # terminal
                first[nt].add(sym)
                all_nullable = False
                break
            else:                             # non-terminal
                f = first_of(grammar, first, sym)
                first[nt] |= (f - {'#'})
                if '#' not in f:
                    all_nullable = False
                    break
        if all_nullable:
            first[nt].add('#')
    return first[nt]


def follow_of(grammar, first, follow, nt, start):
    """Compute FOLLOW of a single non-terminal (recursive with memo)."""
    if nt in follow:
        return follow[nt]

    follow[nt] = set()
    if nt == start:
        follow[nt].add('$')

    for lhs, prods in grammar.items():
        for prod in prods:
            for i, sym in enumerate(prod):
                if sym != nt:
                    continue
                # sym == nt, look at what follows
                rest = prod[i+1:]
                all_nullable = True
                for next_sym in rest:
                    if next_sym not in grammar:     # terminal
                        follow[nt].add(next_sym)
                        all_nullable = False
                        break
                    else:                             # non-terminal
                        follow[nt] |= (first[next_sym] - {'#'})
                        if '#' not in first[next_sym]:
                            all_nullable = False
                            break
                if all_nullable and lhs != nt:
                    follow[nt] |= follow_of(grammar, first, follow, lhs, start)
    return follow[nt]


def main():
    grammar = defaultdict(list)
    print("Enter grammar (space-separated symbols, | for alternatives, # for epsilon):")
    print("Example:  E -> T E'\n          E' -> + T E' | #\n")
    print("Enter empty line to finish:\n")

    start = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            break

        lhs, _, rhs = line.partition('->')
        lhs = lhs.strip()
        if not start:
            start = lhs
        for alt in rhs.split('|'):
            symbols = alt.strip().split()
            grammar[lhs].append(symbols if symbols else ['#'])

    if not grammar:
        print("No grammar.")
        return

    # Compute FIRST
    first = {}
    for nt in grammar:
        first_of(grammar, first, nt)

    # Compute FOLLOW
    follow = {}
    for nt in grammar:
        follow_of(grammar, first, follow, nt, start)

    # Print
    print("\n" + "=" * 45)
    print("FIRST:")
    print("=" * 45)
    for nt in sorted(grammar):
        print(f"  FIRST({nt}) = {{ {', '.join(sorted(first[nt]))} }}")

    print("\n" + "=" * 45)
    print("FOLLOW:")
    print("=" * 45)
    for nt in sorted(grammar):
        print(f"  FOLLOW({nt}) = {{ {', '.join(sorted(follow[nt]))} }}")
    print("=" * 45)


if __name__ == "__main__":
    main()
