# DPLL
DPLL Algorithm with Backtracking

## Pseudo Code
```
DPLL (Clause Set S, Literal Set)
{
 while (S contains a unit clause {l}) {
   delete clauses containing l from S and update Literal Set
   delete l from all clauses in S and update Literal Set
}
If (CNF ∈ S) return false
If (S = ∅) return true
Choose a literal l occurring in S
If (DPLL (S ∪ {l}) or (DPLL (S ∪ {-l})) return true
Else return false
}
```
# Input Information
```
-1 2
-2 3
4 -3 -1
-1
```
###### Here, each line is used to describe a single clause. "-" is used to describe the negation of the literal. Spaces are used to seperate the literals from each clause. Here, the above input information can be visualized as [(~A or B) and (~B or C) and (D or ~C or ~A) and (~A)].

## Running Procedure
```
python DPLL.py sampleCNF/input.txt
```
