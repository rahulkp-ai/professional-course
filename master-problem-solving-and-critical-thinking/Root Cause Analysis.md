# Root Cause Analysis: The 5 Whys Method

## Context & Scenario

**Participants:**

- **Mia** (Project Manager / Lead)
- **Lily** (Assistant)
- **Alex** (Developer)

**Initial Problem:**
The team noticed that work was not getting completed on time, leading to testing delays, confusion over responsibilities, and significant rework. Initial guesses pointed to surface symptoms like task assignment overlaps or communication gaps.

To avoid quick, superficial fixes, Mia applied the **5 Whys Technique** to peel back the layers and uncover the root cause.

---

## What is the 5 Whys Technique?

The **5 Whys** is an iterative interrogative technique used to explore the cause-and-effect relationships underlying a particular problem.

- **Primary Goal:** To determine the root cause of a defect or problem by repeating the question _"Why?"_.
- **Core Benefit:** Prevents team members from jumping to conclusions or addressing surface-level symptoms, guiding them toward long-term systemic solutions.

---

## The 5 Whys Breakdown

```mermaid
flowchart TD
    Problem["<b>Problem:</b> Incomplete requirements cause rework & delays"] --> Q1["<b>1. Why are requirements incomplete?</b><br/>Dev team didn't receive detailed specs from Business Analysts."]
    Q1 --> Q2["<b>2. Why no detailed specs?</b><br/>BAs didn't fully understand client needs during gathering."]
    Q2 --> Q3["<b>3. Why didn't BAs understand client needs?</b><br/>Lack of proper communication between BAs and client during discovery."]
    Q3 --> Q4["<b>4. Why was communication lacking?</b><br/>Initial project meetings were rushed."]
    Q4 --> Q5["<b>5. Why were meetings rushed?</b><br/>Project schedule was set too aggressively."]
    Q5 --> Root["<b>Root Cause:</b> Aggressive project schedule with insufficient planning time."]
```

### Detailed Breakdown

1. **Why are the requirements incomplete?**

- _Answer:_ The development team didn't receive detailed specifications from the business analysts (BAs).

2. **Why didn't the business analysts provide detailed specifications?**

- _Answer:_ They didn't fully understand the client's needs during the initial requirements gathering.

3. **Why didn't they understand the client's needs?**

- _Answer:_ There was a lack of proper communication between the business analysts and the client during the discovery phase.

4. **Why was communication lacking during such a critical phase?**

- _Answer:_ The initial project meetings were rushed, with insufficient time allocated for detailed discussions and clarification.

5. **Why were those meetings rushed?**

- _Answer:_ The **project schedule was set too aggressively**, causing the team to jump straight into execution without buffering enough time for thorough analysis.

---

## Causal Chain & Key Insight

```mermaid
graph LR
    A[Aggressive Schedule] -->|Causes| B[Rushed Meetings]
    B -->|Causes| C[Poor Communication]
    C -->|Causes| D[Misunderstood Client Needs]
    D -->|Causes| E[Incomplete Specs]
    E -->|Causes| F[Rework & Delays]

    style A fill:#ffcccc,stroke:#ff0000,stroke-width:2px
    style F fill:#ffe6cc,stroke:#ff9900,stroke-width:2px

```

- **Surface Symptom:** Delays in development and testing.
- **Initial Assumption:** Task misassignment or individual performance issues.
- **True Root Cause:** Systemic planning failure (setting an overly aggressive schedule that sacrificed discovery and requirements gathering).
