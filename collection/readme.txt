Set
---
Set Types — set, frozenset
1. A set object is an unordered collection of distinct hashable objects.
2. Set is an unordered collection (do not record element position or order of insertion). 
3. Sets do not support indexing, slicing, or other sequence-like behavior.
4. There are currently two built-in set types, set and frozenset.
5. The set type is mutable — the contents can be changed using methods like add() and remove().
6. Being mutable means there no hash value for the set instance.
7. Set cannot be used as either a dictionary key or as an element of another set.
    Because dict key or element of another set must be hashable (must have a has value)
8. The frozenset type is immutable and hashable — its contents cannot be altered after it is created;
    it can therefore be used as a dictionary key or as an element of another set.
9. Set and frozenset support set to set comparisons.
    Two sets are equal if and only if every element of each set is contained in the other (each is a subset of the other).
    A set is less than another set if and only if the first set is a proper subset of the second set (is a subset, but is not equal).
    A set is greater than another set if and only if the first set is a proper superset of the second set (is a superset, but is not equal).