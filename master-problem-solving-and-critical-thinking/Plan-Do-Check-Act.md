# The PDCA Cycle (Plan-Do-Check-Act)

## Overview

The **PDCA Cycle** (Plan-Do-Check-Act), also known as the **Deming Cycle** or **Shewhart Cycle**, is an iterative four-step management method used for continuous improvement of processes, products, or services.

Rather than committing to massive, irreversible changes all at once, PDCA emphasizes testing solutions on a small scale, learning from measurable results, and making data-backed refinements in a continuous loop.

---

## The PDCA Continuous Improvement Loop

```mermaid
graph TD
    Plan["<b>1. PLAN</b><br/>Identify problem, analyze root cause, set goals & build action plan."] --> Do["<b>2. DO</b><br/>Implement solution on a small scale (pilot / test run)."]
    Do --> Check["<b>3. CHECK</b><br/>Evaluate test results, compare actual vs. expected outcomes."]
    Check --> Act["<b>4. ACT</b><br/>Standardize success at scale, or adjust and restart cycle."]
    Act -->|Continuous Loop| Plan

    style Plan fill:#e6f0ff,stroke:#0066cc,stroke-width:2px
    style Do fill:#fff2e6,stroke:#ff6600,stroke-width:2px
    style Check fill:#e6ffe6,stroke:#009933,stroke-width:2px
    style Act fill:#f9e6ff,stroke:#9900cc,stroke-width:2px
```

---

## Detailed Breakdown of the 4 Stages

| Stage       | Core Focus                 | Key Activities                          | Output / Goal |
| ----------- | -------------------------- | --------------------------------------- | ------------- |
| **1. PLAN** | **Preparation & Analysis** | • Define the problem & gather data.<br> |

<br>• Identify root causes (using 5 Whys / Fishbone).<br>

<br>• Draft actionable solution, timeline, roles, & KPIs. | Clear target and risk-mitigated execution plan. |
| **2. DO** | **Small-Scale Test Run** | • Implement the plan in a controlled setting/pilot.<br>

<br>• Follow process strictly.<br>

<br>• Collect observational data and note friction points. | Empirical data from a controlled pilot environment. |
| **3. CHECK** | **Evaluation & Review** | • Compare actual performance against target KPIs.<br>

<br>• Analyze what worked, what failed, and unexpected bugs. | Verified results and list of necessary adjustments. |
| **4. ACT** | **Standardization or Refinement** | • **If successful:** Adopt, standardize, and scale globally.<br>

<br>• **If unsuccessful:** Tweak parameters and restart at **Plan**. | Process standard baseline or refined strategy for next turn. |

---

## Iterative Process Execution Workflow

```mermaid
flowchart LR
    subgraph Iteration 1 ["Iteration 1 (Pilot)"]
        P1[Plan] --> D1[Do] --> C1[Check] --> A1[Act/Adjust]
    end

    subgraph Iteration 2 ["Iteration 2 (Refinement)"]
        P2[Plan] --> D2[Do] --> C2[Check] --> A2[Act/Scale]
    end

    A1 ==> P2

    style Iteration 1 fill:#f9f9f9,stroke:#cccccc
    style Iteration 2 fill:#f0f9f0,stroke:#66cc66

```

---

## Key Takeaways

- **Low-Risk Innovation:** Testing on a small scale during the **DO** stage limits the blast radius of potential failures.
- **Driven by Data:** The **CHECK** stage ensures decisions rely on actual measured results rather than assumptions.
- **Kaizen Philosophy:** The cycle never truly stops—achieving a new baseline in **ACT** immediately becomes the starting point for the next **PLAN** phase.
