_This project has been created as part of the 42 curriculum by pabdalla_

# DataDeck - Abstract Card Architecture

## Evaluator Instructions

### Running the scripts
```bash
python3 battle.py       # Exercise 0
python3 capacitor.py    # Exercise 1
python3 tournament.py   # Exercise 2
```

### Checking code standards
```bash
flake8      # style linter
mypy ./     # type checker
```

---

## Overview

This project teaches Python's advanced design patterns through a creature-based card game
inspired by monster-collecting games. Starting from abstract factories, progressing through
mixin-style capabilities and multiple inheritance, and culminating in the strategy pattern,
each exercise builds a more complete and flexible system — ending in a fully functional
multi-family tournament engine.

---

## Concepts Covered

- Implementing the **Abstract Factory** pattern to group related object creation logic
- Defining abstract base classes with `abc.ABC` and `@abstractmethod`
- Using concrete factories (`FlameFactory`, `AquaFactory`) to encapsulate family-specific creation
- Controlling package public interfaces via `__init__.py` — hiding concrete classes, exposing only factories
- Adding orthogonal capabilities (`HealCapability`, `TransformCapability`) via multiple inheritance without coupling to the base class
- Tracking stateful transformations and letting them influence method behavior at runtime
- Implementing the **Strategy** pattern to decouple battle behavior from Creature logic
- Validating strategy-creature compatibility and raising descriptive exceptions on misuse
- Organizing a multi-opponent round-robin tournament with per-combatant strategies

---

## Key Python Concepts

### Abstract Factory Pattern
- A `CreatureFactory` abstract class exposes `create_base` and `create_evolved` — both abstract
- Concrete factories (`FlameFactory`, `AquaFactory`, etc.) implement these methods and return family-specific creatures
- The package's `__init__.py` only exposes factories — concrete `Creature` subclasses are never directly importable from the package

### Capability Mixins via Multiple Inheritance
- `HealCapability` and `TransformCapability` are independent abstract classes — they do **not** inherit from `Creature`
- Concrete creatures like `Sproutling` or `Shiftling` inherit from **both** `Creature` and the appropriate capability class
- `TransformCapability` uses a persistent boolean attribute to track transformation state, which alters the `attack` output accordingly

### Strategy Pattern
- A `BattleStrategy` abstract class exposes two abstract methods: `is_valid(creature)` and `act(creature)`
- `NormalStrategy` works with any creature; `AggressiveStrategy` requires `TransformCapability`; `DefensiveStrategy` requires `HealCapability`
- `is_valid` returns `False` on mismatches; `act` raises a descriptive exception if called with an incompatible creature

### Package Architecture
- Each exercise lives in its own package folder (`ex0/`, `ex1/`, `ex2/`) with a mandatory `__init__.py`
- `ex1` builds on `ex0`; `ex2` combines both — imports flow upward across packages
- Test scripts (`battle.py`, `capacitor.py`, `tournament.py`) live at the repository root

---

## Project File Tree

```
.
|-- ex0
|   |-- __init__.py
|   |-- creatures.py
|   └── factories.py
|-- ex1
|   |-- __init__.py
|   |-- capabilities.py
|   |-- creatures.py
|   └── factories.py
|-- ex2
|   |-- __init__.py
|   └── strategies.py
|-- battle.py
|-- capacitor.py
└── tournament.py
```

---

## Exercise Summary

| Part | Scripts | Concepts |
|------|---------|----------|
| 0 — Creature Factory | `battle.py` | Abstract factory, `Creature` base class, `FlameFactory` / `AquaFactory`, package interface control |
| 1 — Capabilities | `capacitor.py` | Multiple inheritance, `HealCapability`, `TransformCapability`, stateful attack behavior |
| 2 — Abstract Strategy | `tournament.py` | Strategy pattern, `BattleStrategy`, validity checks|