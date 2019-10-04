

Sequence Types
--------------
1. There are 3 basic sequence type list, tuple and range
2. Most sequence types, both mutable and immutable type support basic operation such as:
    if s and n are 2 sequences hen 
        -> it is allowed to operate on sequence with in/ not in operator
          eg: x in s or x not in s
        -> s + n to concatenation 2 sequence
        -> s * n to add s to itself n times
        -> s[i] to get value at i in s
        -> s[i:j] to slice s from i to j
        -> s[i:j:k] to slice s from i to j with setp k
        -> len/min/max of s
        -> s.count(x) number of x in s
        -> s.index(x[,i[,j]])  index of the first occurrence of x in s (at or after index i 
           and before index j)
Sequences of the same type also support comparisons. In perticular tuples and lists
are compare lexical order means every element must compare to itslef, must be of same type,
same order and sequence must have same length.

Immutable Sequence Type
-----------------------
The difference between immutable (tuple) and mutable sequence is that immutable has an extra operation called hash() which
immutable sequence to a best candidate for dict key.

List
-----

Lists are mutable (being able to change).

Lists may be constructed in several ways:
Using a pair of square brackets to denote the empty list: []
Using square brackets, separating items with commas: [a], [a, b, c]
Using a list comprehension: [x for x in iterable]
Using the type constructor: list() or list(iterable)

-The constructor builds a list whose items are the same and
 in the same order as iterable’s items. iterable may be either a sequence,
 a container that supports iteration, or an iterator object. 


Sorting: https://docs.python.org/3.8/howto/sorting.html#sortinghowto


Tuples:
------

Tuples are immutable sequence.

Tuples may be constructed in a number of ways:
    Using a pair of parentheses to denote the empty tuple: ()
    Using a trailing comma for a singleton tuple: a, or (a,)
    Separating items with commas: a, b, c or (a, b, c)

Using the tuple() built-in: tuple() or tuple(iterable)

Range
-----
The range type represents an immutable sequence of numbers and is commonly
used for looping a specific number of times in for loops.

Testing range objects for equality with == and != compares them as sequences. That is, two range objects
are considered equal if they represent the same sequence of values.
(Note that two range objects that compare equal might have different start,
stop and step attributes, for example range(0) == range(2, 1, 3) or range(0, 3, 2) == range(0, 4, 2).)


Other sequence types
-------------------
Additional sequence types tailored for processing of binary data and text strings are
described in dedicated sections.

1.https://docs.python.org/3.8/library/stdtypes.html#binaryseq
2.https://docs.python.org/3.8/library/stdtypes.html#textseq

Text Sequence Type 
------------------
Textual data in Python is handled with str objects, or strings.
Strings are immutable sequences of Unicode code points.

String literals are written in a variety of ways:
Single quotes: 'allows embedded "double" quotes'

Double quotes: "allows embedded 'single' quotes".

Triple quoted: '''Three single quotes''', """Three double quotes"""

red more at : https://docs.python.org/3.8/library/stdtypes.html#string-methods

Binary Sequence Types — bytes, bytearray, memoryview
---------------------------------------------------
- The core built-in types for manipulating binary data are bytes and 
 bytearray

Bytes Objects
Bytes objects are immutable sequences of single bytes. 
Since many major binary protocols are based on the ASCII text encoding, 
bytes objects offer several methods that are only valid when working with
ASCII compatible data and are closely related to string objects in a variety of other ways.

Only ASCII characters are permitted in bytes literals (regardless of the 
declared source code encoding). Any binary values over 127 must be entered 
into bytes literals using the appropriate escape sequence.

Bytearray Objects

bytearray objects are a mutable counterpart to bytes objects.


Memory views
https://docs.python.org/3.8/library/stdtypes.html#memory-views



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



Mapping Types — dict
--------

A mapping object maps hashable values to arbitrary objects.
Mappings are mutable objects. There is currently only one standard mapping type, the dictionary

Dictionaries can be created by placing a comma-separated list of
key: value pairs within braces, 
for example: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}, or
by the dict constructor.

If keyword arguments are given, the keyword arguments and their values 
are added to the dictionary created from the positional argument. 
If a key being added is already present, the value from the keyword
argument replaces the value from the positional argument.