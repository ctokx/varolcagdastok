# A Guide to Black-Box Testing: Equivalence, Boundary, and Decision Table Techniques
<p class="post-date">Published: November 17, 2025</p>

Black-box testing is a method of software testing that does not consider the internal structure of the system. Instead, test cases are derived from the external specification, which describes what the system is supposed to do. This approach is often used in system and integration testing.

Because it is impossible to test every conceivable input, black-box testing relies on techniques that intelligently select a small number of tests to represent a much larger set of possibilities.

## Technique 1: Equivalence Class Partitioning

This is a foundational technique in black-box testing. The core idea is to divide the entire domain of input values into distinct groups called **equivalence classes**. Within each class, the system is expected to behave in the same way.

When creating classes, you must:
* Consider both **valid and invalid** input values.
* Ensure that equivalence classes for valid and invalid inputs are kept separate.
* Select **one representative value** from each class for testing. The assumption is that if this one value works, all other values in its class will also work.

### Example: `getAbsoluteValue(int num)`
A specification for a function that gets the absolute value of an integer might have these rules:
* If the argument is not negative, it is returned.
* If the argument is negative, its negation is returned.
* A special case notes that if the argument is `Integer.MIN_VALUE`, the result is `Integer.MIN_VALUE` (which is negative).

This specification leads to three distinct equivalence classes for the input `num`:

| Class Name | Values | Representative |
| :--- | :--- | :--- |
| non-negative | $0 \le num \le$ Integer.MAX_VALUE | 10 |
| negative-not-min | Integer.MIN_VALUE < $num$ < 0 | -5 |
| min-value | $num$ = Integer.MIN_VALUE | Integer.MIN_VALUE |

This reduces the full range of possible integers to just three representative cases.

## Technique 2: Boundary Value Analysis

This technique is a complement to equivalence partitioning. It is based on the assumption that program errors are most likely to occur at the **boundaries** of these partitions.

Boundary value analysis requires identifying the partitions and then testing the values directly on the boundary, as well as their immediate neighbors on either side.

### Example: `getAbsoluteValue(int num)` Boundaries
Using the same classes from before, we can identify the following boundaries and create test cases for them:
* **For `non-negative` ($0 \le num \le$ MAX):** Boundaries are 0 and `Integer.MAX_VALUE`.
* **For `negative-not-min` (MIN < $num$ < 0):** Boundaries are `Integer.MIN_VALUE + 1` and `-1`.
* **For `min-value` ($num$ = MIN):** The boundary is `Integer.MIN_VALUE`.

This creates a more robust set of test cases for catching common off-by-one errors.
            
## Technique 3: Decision Tables

When input combinations become complex and lead to different outcomes, a **decision table** is a formal way to describe the interactions.

The table is split into **Conditions** (inputs) and **Reactions** (outputs/actions). Each column represents a single rule or test case, and the goal is to generate one test per column.