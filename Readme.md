# Compiler Design Lab

A collection of **10 compiler design lab programs** implementing lexical analysis, syntax analysis, and grammar processing using **Flex (Lex)** and **Python**.

---

## 📋 Table of Contents

| # | Program | Tool | Description |
|---|---------|------|-------------|
| 01 | [Recognize Telephone Operators](#01-recognize-telephone-operators) | Flex | Identify Bangladeshi mobile operators from phone numbers |
| 02 | [Count Characters, Words & Lines](#02-count-characters-words--lines) | Flex | Count characters, words, and lines in a C program |
| 03 | [Identify Number Types](#03-identify-number-types) | Flex | Classify integer, float, exponential, and complex numbers |
| 04 | [Count Spaces & Comments](#04-count-spaces--comments) | Flex | Count whitespace characters and comments in C code |
| 05 | [Recognize & Count Identifiers](#05-recognize--count-identifiers) | Flex | Identify and count all user-defined identifiers in C |
| 06 | [Recognize "To Be" Verbs](#06-recognize-to-be-verbs) | Flex | Detect forms of "to be" in English text |
| 07 | [Sentence Type Classifier](#07-sentence-type-classifier) | Flex | Classify sentences as simple, complex, or compound |
| 08 | [FIRST & FOLLOW Calculator](#08-first--follow-calculator) | Python | Compute FIRST() and FOLLOW() sets for a CFG |
| 09 | [CFG Ambiguity Check](#09-cfg-ambiguity-check) | Python | Detect and eliminate left-recursion/ambiguity in CFGs |
| 10 | [C Lexical Analyzer](#10-c-lexical-analyzer) | Flex | Complete lexer for C programs with token counting |

---

## 🛠️ Prerequisites

### For Flex Programs (01–07, 10)

- **Flex** (Lexical Analyzer Generator) — `flex-2.5.4a-1-setup.exe` included in `Software/`
- **GCC** (C Compiler) — MinGW or any C compiler

### For Python Programs (08–09)

- **Python 3.6+**

---

## 🚀 How to Run

### Flex Programs

```bash
# Step 1: Generate C source from .l file
flex program.l

# Step 2: Compile
gcc lex.yy.c -o program

# Step 3: Run (some accept stdin, some accept file arguments)
./program < input.txt        # stdin mode
./program input.c            # file mode (Program 10)
```

### Python Programs

```bash
python program.py
```

---

## 📖 Program Details

### 01. Recognize Telephone Operators

**File:** `01_Recognize_teephone.l`

Recognizes Bangladeshi mobile phone numbers and identifies the operator.

| Prefix | Operator |
|--------|----------|
| 013, 017 | Grameenphone |
| 014, 019 | Banglalink |
| 015 | Teletalk |
| 016 | Airtel |
| 018 | Robi |

**Run:**
```bash
flex 01_Recognize_teephone.l && gcc lex.yy.c -o phone && ./phone
```

**Test Input:**
```
01312345678 01498765432 01511112222 01633334444 01755556666 01877778888 01999990000
```

**Expected Output:**
```
Grameenphone: 01312345678
Banglalink: 01498765432
Teletalk: 01511112222
Airtel: 01633334444
Grameenphone: 01755556666
Robi: 01877778888
Banglalink: 01999990000
```

---

### 02. Count Characters, Words & Lines

**File:** `02_count_characters_words_lines.l`

Counts the number of characters, words, and lines in a given C program.

**Run:**
```bash
flex 02_count_characters_words_lines.l && gcc lex.yy.c -o count && ./count < test.c
```

**Test Input (`test.c`):**
```c
int main() {
    int x = 5;
    return x;
}
```

**Expected Output:**
```
Characters: 37
Words: 12
Lines: 4
```

---

### 03. Identify Number Types

**File:** `03_identify_int_float_exp_colplex.l`

Classifies numeric literals into four categories: Integer, Floating-Point, Exponential, and Complex.

**Run:**
```bash
flex 03_identify_int_float_exp_colplex.l && gcc lex.yy.c -o numbers && ./numbers
```

**Test Input:**
```
42 3.14 2.5e10 -7 +3.14e-5 1+2i 3.0-4.5i 100
```

**Expected Output:**
```
Integer: 42
Floating-Point: 3.14
Exponential: 2.5e10
Integer: -7
Exponential: +3.14e-5
Complex: 1+2i
Complex: 3.0-4.5i
Integer: 100
```

---

### 04. Count Spaces & Comments

**File:** `04_count_space_and_comment.l`

Counts the total number of whitespace characters and comments (both `//` and `/* */`) in a C program.

**Run:**
```bash
flex 04_count_space_and_comment.l && gcc lex.yy.c -o spcomment && ./spcomment < test.c
```

**Test Input (`test.c`):**
```c
// This is a comment
int main() {
    /* block comment */
    int x = 5;   // inline comment
    return x;
}
```

**Expected Output:**
```
No of Comment: 3
No of Space: 28
```

---

### 05. Recognize & Count Identifiers

**File:** `05_recognize_and_count_identifiers.l`

Identifies and counts all user-defined identifiers in a C program, skipping keywords.

**Run:**
```bash
flex 05_recognize_and_count_identifiers.l && gcc lex.yy.c -o identifiers && ./identifiers < test.c
```

**Test Input (`test.c`):**
```c
int main() {
    float salary, tax;
    int age = 25;
    return 0;
}
```

**Expected Output:**
```
Identifier: main
Identifier: salary
Identifier: tax
Identifier: age

Total Identifiers: 4
```

---

### 06. Recognize "To Be" Verbs

**File:** `06_recognize_be_verb.l`

Detects all forms of the verb "to be" in a given English paragraph.

Recognized forms: `am`, `is`, `are`, `was`, `were`, `been`, `have`, `has`, `be`

**Run:**
```bash
flex 06_recognize_be_verb.l && gcc lex.yy.c -o beverb && ./beverb
```

**Test Input:**
```
I am a student. They are happy. She was late. We have been waiting. It is cold today.
```

**Expected Output:**
```
To-Be Verb Found: am
To-Be Verb Found: are
To-Be Verb Found: was
To-Be Verb Found: have
To-Be Verb Found: been
To-Be Verb Found: is
Total No of To-Be Verbs: 6
```

---

### 07. Sentence Type Classifier

**File:** `07_check_simple_complex_compound.l`

Classifies each line as **Simple**, **Complex**, **Compound**, or **Compound-Complex** based on the presence of subordinating and coordinating conjunctions.

| Type | Indicators |
|------|------------|
| Complex | `that`, `since`, `because`, `although`, `if`, `when`, `while`, `unless`, `until`, `after`, `before` |
| Compound | `and`, `or`, `but` |
| Compound-Complex | Both complex and compound keywords |
| Simple | None of the above |

**Run:**
```bash
flex 07_check_simple_complex_compound.l && gcc lex.yy.c -o sentence && ./sentence
```

**Test Input:**
```
The sun is shining.
I went home because I was tired.
She likes tea and he likes coffee.
Although it rained, we went out and had fun.
```

**Expected Output:**
```
Simple Sentence
Complex Sentence
Compound Sentence
Compound-Complex Sentence
```

---

### 08. FIRST & FOLLOW Calculator

**File:** `08_first_follow.py`

Computes the **FIRST()** and **FOLLOW()** sets for a given Context-Free Grammar. Accepts grammar rules interactively via stdin.

**Run:**
```bash
python 08_first_follow.py
```

**Test Input:**
```
E -> T E'
E' -> + T E' | #
T -> F T'
T' -> * F T' | #
F -> ( E ) | id
```
*(Press Enter on empty line to finish)*

**Expected Output:**
```
=============================================
FIRST:
=============================================
  FIRST(E)  = { (, id }
  FIRST(E') = { #, + }
  FIRST(F)  = { (, id }
  FIRST(T)  = { (, id }
  FIRST(T') = { #, * }

=============================================
FOLLOW:
=============================================
  FOLLOW(E)  = { $, ) }
  FOLLOW(E') = { $, ) }
  FOLLOW(F)  = { $, ), +, * }
  FOLLOW(T)  = { $, ), + }
  FOLLOW(T') = { $, ), + }
=============================================
```

---

### 09. CFG Ambiguity Check

**File:** `09_CFG_ambiguity_check.py`

Detects **left-recursion** (a source of ambiguity in top-down parsing) in a CFG and eliminates it by transforming the grammar. Uses a hardcoded example grammar.

**Run:**
```bash
python 09_CFG_ambiguity_check.py
```

**Test Case (built-in grammar):**
```
S -> A a | b
A -> A c | S d | ε
```

**Expected Output:**
```
--- Original Production Rules ---
S -> Aa | b
A -> Ac | Sd | ε

Left-Recursion/Ambiguity risk found! Eliminating dependencies...

--- Processed Production Rules ---
S -> Aa | b
A -> bdA' | A' | Ada'
A' -> cA' | ε
```

---

### 10. C Lexical Analyzer

**File:** `10_C_lexer.l`

A complete lexical analyzer for the C programming language. Processes preprocessor directives, comments, keywords, identifiers, constants, operators, and punctuation. Produces a summary of token counts.

**Run:**
```bash
flex 10_C_lexer.l && gcc lex.yy.c -o c_lexer && ./c_lexer test.c
```

**Test Input (`test.c`):**
```c
#include <stdio.h>
int main() {
    int x = 5, y = 10;
    float pi = 3.14;
    if (x < y) {
        return x + y;
    }
    return 0;
}
```

**Expected Output:**
```

=== Lexer Summary ===
Lines:            8
Keywords:         6
Identifiers:      8
Operators (1-char): 5
Operators (2-char): 0
Punctuations:     9
Statements:       4
```

---

## 📁 Project Structure

```
Compiler_Lab/
├── 01_Recognize_teephone.l          # Flex: Phone operator recognizer
├── 02_count_characters_words_lines.l # Flex: Char/word/line counter
├── 03_identify_int_float_exp_colplex.l # Flex: Number type classifier
├── 04_count_space_and_comment.l      # Flex: Space & comment counter
├── 05_recognize_and_count_identifiers.l # Flex: Identifier recognizer
├── 06_recognize_be_verb.l            # Flex: "To be" verb detector
├── 07_check_simple_complex_compound.l # Flex: Sentence type classifier
├── 08_first_follow.py                # Python: FIRST & FOLLOW calculator
├── 09_CFG_ambiguity_check.py         # Python: CFG ambiguity checker
├── 10_C_lexer.l                      # Flex: Complete C lexer
├── README.md                         # This file
├── Notes/                            # Lab problem statements (PDF/DOCX)
└── Software/                         # flex & bison installers
```

---

## 🔧 Build All Flex Programs at Once

```bash
# Build all Flex programs
for f in 01_Recognize_teephone.l 02_count_characters_words_lines.l 03_identify_int_float_exp_colplex.l 04_count_space_and_comment.l 05_recognize_and_count_identifiers.l 06_recognize_be_verb.l 07_check_simple_complex_compound.l 10_C_lexer.l; do
    base=$(basename "$f" .l)
    flex "$f" && gcc lex.yy.c -o "$base" && echo "Built: $base"
done
```

---

## 📝 Notes

- All Flex programs use `yywrap()` returning 1 to signal end-of-input.
- Programs 01–07 read from **stdin**; Program 10 reads from a **file argument**.
- The `Software/` folder contains Windows installers for Flex 2.5.4a and Bison 2.4.1.
- Python programs (08, 09) require no external libraries — standard library only.
