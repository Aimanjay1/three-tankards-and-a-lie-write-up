Here is a complete CTF-style write-up for the challenge. You can use this for your personal notes, a blog post, or a portfolio.

---

# CTF Write-Up: Three Tankards and a Lie

## Challenge Overview

**Category:** Coding / Algorithms
**Objective:** Track the movement of specific items hidden under "tankards" across a series of positional swaps, and report their final locations.

**Context:**
The challenge presents a classic shell game scenario (reminiscent of tracking a hidden ball under cups). We are given $N$ tankards, initially holding an item matching their position number (1 to $N$). A series of $M$ swap operations exchanges the contents of two positions. Finally, we are given $Q$ queries asking for the final position of the item that originally started at a given position $p$.

## Analysis & Approach

Looking at the constraints:

* $N \le 2000$ (Tankards)
* $M \le 5000$ (Swaps)
* $Q \le 2000$ (Queries)

The constraints are small enough that an optimized mathematical approach isn't strictly necessary; a direct simulation of the swaps will run well within the time limits.

To solve this efficiently, we need to maintain two pieces of state:

1. **The Tankards Array (`tankard`):** Tracks which item is currently sitting at position `i`.
2. **The Position Array (`pos`):** Tracks the current location of item `i`.

By keeping track of both, every time a swap occurs between position `a` and `b`, we can instantly look up which items are involved and update their respective locations in $O(1)$ time. This allows the entire simulation to run in linear time relative to the number of swaps and queries.

## The Solution

Here is the clean Python script used to simulate the swaps and output the final positions.

```python
import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    Q = int(input_data[2])

    # tankard[i] tracks the item currently at position i
    tankard = [i for i in range(N + 1)]
    # pos[i] tracks the current location of item i
    pos = [i for i in range(N + 1)]

    idx = 3

    # Process all M swap operations
    for _ in range(M):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2

        # Identify which items are at positions a and b
        item_a = tankard[a]
        item_b = tankard[b]

        # Swap the items in the tankard array
        tankard[a] = item_b
        tankard[b] = item_a

        # Update the tracked positions for the swapped items
        pos[item_a] = b
        pos[item_b] = a

    # Process all Q queries
    for _ in range(Q):
        p = int(input_data[idx])
        idx += 1
        print(pos[p])

if __name__ == '__main__':
    solve()

```

## Debugging Note

During the execution phase, an initial script threw a `NameError: name 'solve' is not defined`. In Python, the interpreter executes code from top to bottom. Calling a function before it is declared in the script causes a runtime error. Removing the premature function call and letting the `if __name__ == '__main__':` block handle execution resolved the issue.

## The Flag

Successfully passing the test cases yields the flag, a clever nod to the challenge lore where the character Rin refuses to play the betting game and instead simply observes.

**Flag:** `HTB{n3v3r_pl4ys_4lw4ys_w4tch3s}`
