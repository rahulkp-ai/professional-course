# The Pareto Principle (80/20 Rule)

## Overview

The **Pareto Principle** (also known as the **80/20 Rule**) states that roughly **80% of effects come from 20% of causes**. In problem-solving and management, it serves as a prioritization framework to identify and tackle the "vital few" root causes that yield the highest impact.

---

## Key Concepts

- **The 80/20 Ratio:** A small minority of factors (~20%) drives the vast majority of outcomes or problems (~80%).
- **Targeted Focus:** Helps teams avoid spreading resources too thin across minor, low-impact issues.
- **Resource Optimization:** Maximizes ROI on effort and time by fixing high-leverage issues first.

---

## Step-by-Step Implementation

```mermaid
flowchart TD
    Step1["<b>1. Identify & List</b><br/>Analyze all contributing factors or issues"] --> Step2["<b>2. Measure Influence</b><br/>Quantify how much each factor impacts the outcome"]
    Step2 --> Step3["<b>3. Apply 80/20 Filter</b><br/>Isolate the ~20% of causes driving ~80% of the problem"]
    Step3 --> Step4["<b>4. Target Key Causes</b><br/>Focus resources directly on the vital few"]
```

### Detailed Steps

1. **Identify & List Factors**

- Gather data on all problems, bugs, or bottlenecks affecting project performance.

2. **Analyze Influence**

- Measure the frequency, severity, or cost associated with each contributing cause.

3. **Isolate the Vital 20%**

- Rank causes by impact to pinpoint the small subset responsible for most of the trouble.

4. **Target High-Impact Solutions**

- Allocate effort toward resolving those vital causes rather than spreading bandwidth across trivial ones.

---

## Impact Distribution

```mermaid
graph LR
    subgraph Causes ["Causes (100%)"]
        C1["Vital 20% Causes"]
        C2["Minor 80% Causes"]
    end

    subgraph Outcomes ["Outcomes / Problems (100%)"]
        O1["80% of Impact"]
        O2["20% of Impact"]
    end

    C1 ==>|Drives| O1
    C2 -->|Drives| O2

    style C1 fill:#ffcccc,stroke:#cc0000,stroke-width:2px
    style O1 fill:#ffe6cc,stroke:#ff6600,stroke-width:2px
    style C2 fill:#e6e6e6,stroke:#999999
    style O2 fill:#f9f9f9,stroke:#cccccc

```

---

## Summary Table

| Category                | Vital Few (~20%)                 | Trivial Many (~80%)            |
| ----------------------- | -------------------------------- | ------------------------------ |
| **Share of Causes**     | ~20% of issues                   | ~80% of issues                 |
| **Share of Impact**     | ~80% of friction/results         | ~20% of friction/results       |
| **Action Required**     | High priority — fix immediately  | Low priority — defer or ignore |
| **Resource Allocation** | Majority of team effort & budget | Minimal effort                 |
