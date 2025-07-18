# MEARA Development Cycle

**Version**: 1.0
**Last Updated**: 2025-07-17

This document describes the development workflow for building each component of the MEARA pipeline. Our process is designed to be iterative, focused, and aligned with our core principles.

## 🧠 Step 1: Use the Roadmap as the Source of Truth

* The `roadmap.md` file is our master plan. It breaks down the project into milestones and specific, actionable tasks.
* The `PRM.md` defines the high-level vision and requirements for the product.
* We will always refer to the roadmap to select the next task in our development queue.

## 🔍 Step 2: Identify the Next SLC Slice to Build

* Open `roadmap.md` and identify the next task marked with "⏳ To Do".
* Each task (e.g., M1.1, M1.2) represents a "Simple, Lovable, Complete" (SLC) slice of the product that we will build and validate in isolation.

## 🧾 Step 3: Generate a Detailed Feature Spec

* For the selected task, we will create a detailed feature specification.
* We will use the `FEATURE_SPEC_TEMPLATE.md` to ensure all requirements, flows, and test cases are considered.
* As the MEARA-Builder, I will collaborate with you to flesh out this document, ensuring it aligns with our SLC principles and Experience Goals.
* The spec will be saved as `docs/specifications/feat_spec_[task_id].md` (e.g., `feat_spec_M1-1_ingest-and-plan.md`).

## 💻 Step 4: Implement and Test the Component

* With a complete feature spec, you will implement the component.
* For pipeline steps involving AI, this involves:
    1.  Writing the prompt file (`.txt`).
    2.  Testing the prompt using the Gemini CLI against our test environment assets.
    3.  Refining the prompt until the output is correct and reliable.
* For scripting steps (like the dashboard generator), this involves writing and testing the script locally.

## ✔️ Step 5: Validate Against SLC Criteria

* Before marking a task as complete, we will validate it against our definition of done:
    * **Simple**: Does it do one job well? Is the implementation clean and focused?
    * **Lovable**: Does it provide clear feedback? Does it instill "Perfect Handoff Confidence"?
    * **Complete**: Do all tests pass? Is it seamlessly integrated with the previous step's output?

## 🔄 Step 6: Update Roadmap and Loop

* Once a component is validated, update its status in `roadmap.md` to "✅ Done".
* Archive the feature spec and any relevant test logs.
* Return to Step 2 and select the next SLC slice to build.

This cycle ensures we build the MEARA pipeline in a methodical, quality-driven way, delivering one robust component at a time.