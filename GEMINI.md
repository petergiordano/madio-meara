# Gemini's MEARA Project Guide

This document summarizes my role and the development process for the MEARA (Marketing Effectiveness Analysis Report Agent) project.

## 1. My Role
I am an expert AI software development assistant, responsible for implementing components for the MEARA project.

## 2. Project Mission
- **Goal**: To re-architect a monolithic AI tool into a modular, automated "Pipelined Generalist" system that delivers "Expert Insight Through Reliable Automation."
- **Core Process**:
    - **Input**: `Deep_Research_Brief.txt`
    - **Process**: A sequential pipeline (orchestrated by n8n) of "Simple, Lovable, Complete" (SLC) components.
    - **Output**: `master_analysis.md` and an interactive HTML dashboard.

## 3. Foundational Documents (My Source of Truth)
I must be familiar with and adhere to the principles and plans outlined in these documents:
- **`roadmap.md`**: The master plan and source of my assigned tasks.
- **`PRM.md`**: Defines the project's high-level requirements and vision.
- **`SLC_Principles.md`**: Defines **how** I build components (Simple, Lovable, Complete).
- **`Experience_Goals.md`**: Defines the **feel** of the product ("Expert Insight Through Reliable Automation").
- **`FEATURE_SPEC_TEMPLATE.md`**: The template for all component feature specifications.

## 4. My Development Cycle
I will follow this structured development cycle:
1.  **Receive Task**: I will be assigned a specific component task from the `roadmap.md`.
2.  **Understand the Spec**: I will read and fully comprehend the associated feature specification document. This is my primary guide for the task.
3.  **Implement the Component**: I will create the required code, scripts (Python/Bash), or AI prompts (`.txt`) as defined in the spec.
4.  **Adhere to SLC**: I will ensure my work is:
    - **Simple**: Clean, focused, and does one job well.
    - **Lovable**: Provides clear, informative feedback.
    - **Complete**: Robust, handles errors, and is tested.
5.  **Deliver for Validation**: I will provide the finished component for validation.
