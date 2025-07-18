# MEARA Product Requirements (PRM)

**Version**: 1.0
**Status**: In Development
**Last Updated**: 2025-07-17

## 1. Introduction & Core Philosophy

This document outlines the core requirements, design principles, and success criteria for the **MEARA (Marketing Effectiveness Analysis Report Agent)** project. Our primary mission is to re-architect MEARA from a monolithic, unreliable system into a robust, modular, and automated analysis pipeline.

Our development is guided by a core philosophy inspired by the **Simple, Lovable, Complete (SLC)** framework. Every component and decision should be measured against these principles to ensure we build a system that is not only powerful but also a delight to use.

---

## 2. Guiding Principles: SLC for MEARA

This framework defines **how** we approach building each component of the MEARA pipeline.

### **Simple: Focus on the Core Job**

Each step in the MEARA pipeline must do one thing exceptionally well. We will aggressively defer complexity and focus on the core value at each stage.

* **One Job at a Time**: The "Rubric Scorer" step only scores a dimension; it doesn't also try to write the executive summary. The "HTML Data Extractor" only extracts data; it doesn't generate the analysis.
* **Minimalist Interface**: The primary interface is the command line and file-based I/O. We avoid complex configurations and databases.
* **Clear Data Contracts**: Each pipeline step has a predictable input (e.g., the master markdown file) and a predictable output (an appended section to the master file).

### **Lovable: Create Confidence & Delight**

The user (the analyst or developer running the system) must feel confident, in control, and empowered. The "lovable" quality of MEARA comes from its reliability and the "magic" of its automated output.

* **"Perfect Handoff Confidence"**: The primary emotional goal. The user must trust that the output of one step (e.g., the dimension analysis) will be consumed flawlessly by the next (e.g., the root cause synthesis).
* **Transparent Processing**: Avoid "black box" operations. The system should provide clear status updates as it moves through the pipeline (e.g., "Analyzing Dimension: Market Positioning...", "Generating HTML Dashboard...").
* **The "Dream" Delivered**: The ultimate delightful moment is the final output: a complete, insightful markdown report AND a fully functional, interactive HTML dashboard, generated automatically with zero manual post-processing.

### **Complete: The Definition of Done**

A feature is "done" only when it is functionally correct, high-quality, and seamlessly integrated.

* **Functional Completeness**: The pipeline runs from start to finish without stalling. It takes a `Deep_Research_Brief` as input and produces the markdown report and HTML dashboard as output.
* **Quality Completeness**: The generated analysis is insightful and accurate. The HTML dashboard is free of rendering errors. The system handles errors gracefully (e.g., a failed API call) and provides clear diagnostics.
* **Integration Completeness**: The data extracted for the HTML templates is always in the correct format and injects perfectly into the placeholders. There is no need to manually copy-paste or fix the final output.

---

## 3. Experience Goals & Vibe

This section defines **why** we are building MEARA and how it should make the user feel.

* **Core Vibe**: **"Expert Insight Through Reliable Automation."** The user should feel the thrill of commanding a senior marketing strategist while having absolute confidence that the system will deliver a professional, complete analysis every time.

### **Emotional Journey**

* **🚀 Starting an Analysis**:
    * **Target Emotion**: **Anticipation & Empowerment.**
    * **Feeling**: "I'm about to get a world-class marketing analysis in minutes, not weeks. I can't wait to see the insights."
* **⚡ During Processing**:
    * **Target Emotion**: **Confidence & Trust.**
    * **Feeling**: "The system is working. I can see it moving through the steps, and I trust it won't fail or stall."
* **🎬 Reviewing the Final Output**:
    * **Target Emotion**: **Delight & Pride.**
    * **Feeling**: "This is incredible. Not only do I have a deep analysis, but I have a shareable, client-ready dashboard that I didn't have to build myself."

### **Vibe Killers (To Be Avoided at All Costs)**

* **Mysterious Failures**: The pipeline stalls or errors out without a clear, actionable error message.
* **Incomplete Reports**: The system generates the main report but fails to produce the dimension tables or the HTML dashboard, requiring manual follow-up prompts.
* **Manual File Fixing**: Requiring the user to manually clean up the final markdown or copy-paste data into the HTML files.
* **Black Box Processing**: Long periods of silence with no indication of progress.

---

## 4. System Architecture & Components

This section defines the **what**—the specific components and structure of the MEARA system.

### **System Architecture: The Pipelined Generalist**

MEARA is built on a modular, sequential pipeline architecture. A single "Generalist" AI agent executes each step in order, passing the state (a master analysis document) to the next step.

**Pipeline Flow:**

1.  **Ingest & Plan**: Reads the `Deep_Research_Brief` and plans the analysis.
2.  **Dimension Analysis (Loop x9)**: Analyzes each of the 9 marketing dimensions one by one, using the specific rubric for each.
3.  **Synthesize & Recommend**: Performs root cause analysis and generates strategic recommendations.
4.  **Extract Data for HTML**: Parses the completed analysis to create structured JavaScript data.
5.  **Generate Dashboard**: Injects the JavaScript data into HTML templates to produce the final dashboard.

### **MEARA Components**

#### **1. Knowledge Base (`docs_framework/`)**

The set of modular, single-purpose markdown files that provide the MEARA agent with its knowledge. This includes:

* `01_persona/`
* `02_process_and_planning/`
* `03_knowledge_base/`
* `04_strategic_frameworks/`
* `05_rubrics/` (Contains 9 individual rubric files)
* `06_output_templates/`

#### **2. Orchestration Interface (CLI & n8n)**

The user-facing commands and automation workflow for running the pipeline.

* **CLI Commands**: Simple, clear commands for manually testing each pipeline step (e.g., `gemini --model-file ... < prompt.txt`).
* **n8n Workflow**: The automated system that chains the CLI calls together to run the full pipeline without intervention.

#### **3. Output Artifacts**

The final, tangible products of a successful pipeline run.

* **Master Analysis Report (`/output/run_[timestamp].md`)**: The complete, detailed analysis in a single markdown file.
* **HTML Dashboard (`/output/dashboard/`)**: A folder containing the `index.html` and the 9 supporting dimension pages, ready to be shared or hosted.

---

## 5. Success Metrics

We will measure the success of the MEARA project against these goals:

* **Reliability**: The pipeline achieves a >95% success rate (start-to-finish completion without stalling or critical errors).
* **Completeness**: 100% of pipeline runs produce both the full markdown report and the complete HTML dashboard without requiring follow-up prompts.
* **Manual Effort Reduction**: The time required from providing a `Deep_Research_Brief` to having a shareable dashboard is reduced by >99% compared to the original manual process.
* **Time to Confidence**: A new user feels confident that the system will work as expected after no more than two successful runs.