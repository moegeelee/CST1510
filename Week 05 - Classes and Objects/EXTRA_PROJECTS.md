# Week 5 — Extra Practice Projects

Optional. Beyond the lab. The *100 Days of Code* material this course
draws on doesn't reach classes until well past Day 16, so there's no
direct project to adapt here — instead, this is a refactor exercise:
take a project built with loose functions and variables, and rebuild it
around a class, the same move `04 - Lists, Dictionaries and Files`'s
`Server`/`Record` examples made from a dict.

---

## Blackjack, Object-Oriented

**Uses:** classes, `__init__`, methods, `self`

If you built a version of Blackjack (Day 11 of *100 Days of Code* — deal
two cards each, hit or stand, dealer plays to 17, compare scores) using
loose functions like `deal_card()`, `calculate_score(cards)`, and
`compare(user_score, computer_score)`, redo it with:

1. A `Hand` class — `__init__(self)` starts with an empty `cards` list.
   Give it a method `add_card(self)` that deals one card into
   `self.cards`, and a method `score(self)` that returns the hand's
   total (including the ace-is-1-or-11 and blackjack rules).
2. A `Player` class wrapping a `Hand` — or just use two `Hand` objects
   directly, one for the user and one for the computer.
3. Rewrite the game loop so it calls `user_hand.add_card()` and
   `user_hand.score()` instead of passing lists into functions by hand.

Nothing here is a new rule of Blackjack — only where the data and the
logic that acts on it now live: together, on one object, instead of
scattered across a card list and separate functions that both need it
passed in every time.

*Loosely adapted from: 100 Days of Code, Day 11.*

---

Want to see this exact refactor done for you, step by step, on a
simpler example first? That's `03 - Many Objects Together` in this
folder, and Week 8's `04 - From Functions to a Class` does the same move
again on real pulled data.
