# validation_plan.md

## Necessary Context

The **DeepStack - MEARA (Marketing Effectiveness Analysis Report Agent)** is a sophisticated AI designed to emulate a senior B2B SaaS marketing strategist, embodying the expertise of industry-leading CMOs.  Its primary function is to conduct a comprehensive marketing effectiveness analysis for a given company, delivering actionable insights and a clear implementation roadmap. 

The **DeepStack - MEARA (Marketing Effectiveness Analysis Report Agent)** is a sophisticated framework designed to guide a project-type AI agent in producing expert-level B2B SaaS marketing analyses. 

The architecture of the framework is built on two core components: 
1. a detailed set of system instructions that establish the agent's expert persona and operational rules, 
   and 
2. a dedicated knowledge base of interconnected documents (Marketing Analysis Methodology, Marketing Analysis Rubrics, Strategic_Elements_Framework) that provide a structured process and evaluation criteria. 

This MEARA blueprint is designed to be platform-agnostic and can be implemented in various advanced AI agent environments, such as Gemini Gems, Claude Projects, or ChatGPT CustomGPTs (and Projects). 

To date, the implementation within the Gemini Gem environment has yielded the best-performing and most consistent results.

The analysis process begins with a crucial piece of pre-compiled intelligence: the **"Deep Research Brief for [Company Name]."**  This brief is not merely raw data; it is a foundational document containing curated strategic insights, hypotheses about market dynamics, voice-of-the-customer data, and potential "Breakthrough Sparks" or "Hidden Gems."  The agent is mandated to use this brief as a starting point to guide its investigation.

However, the agent's core task is to then conduct its own **extensive, independent, and current web research** to validate, verify, update, or even challenge the findings presented in the brief.  This active evidence collection is non-negotiable and ensures the final report is based on the most current, verifiable information, with all examples and quotes cited from the agent's direct research during the analysis session. 

### Architectural & Document Relationship Diagram

The agent's high-quality output is ensured by a hierarchical and interdependent document architecture. The relationship and dependency flow can be visualized as follows:

```
[System Instructions & Persona]
     |
     └──> 1. Instruct_Marketing_Analysis (The Master Orchestrator) 
               |
               ├──> Manages the entire process, output structure, and tone. 
               |
               └──> 2. Marketing Analysis Methodology (The 8-Step Process) 
                         |
                         ├──> Input: [Deep Research Brief] 
                         |
                         ├──> Step 3: Dimension Evaluation -> Utilizes:
                         |      |
                         |      └──> 3. Marketing Analysis Rubrics 
                         |           (Provides detailed scoring criteria for 9 dimensions)
                         |
                         ├──> Between Steps 3 & 4: Strategic Verification -> Utilizes:
                         |      |
                         |      └──> 4. Strategic_Elements_Framework 
                         |           (Ensures 'Breakthrough Sparks' from the Deep Research Brief are preserved) 
                         |
                         └──> Steps 4-8: Root Cause Analysis, Recommendations, Implementation Plan, and Report Assembly.
```

As the diagram illustrates, the `Instruct_Marketing_Analysis` document is the central controller, directing the agent to follow the 8-step `Marketing Analysis Methodology`.  At specific points in this methodology, other documents are invoked. During Step 3 (Dimension Evaluation), the `Marketing Analysis Rubrics` provide the granular criteria for scoring.  Crucially, between the evaluation and root cause identification steps, the `Strategic_Elements_Framework` is applied as a checkpoint to ensure high-level strategic opportunities, often seeded by the Deep Research Brief, are not lost in the detailed analysis and are carried forward into the final recommendations.  This structured dependency ensures that tactical observations are always connected back to overarching strategic imperatives.


---
## Core Problem

There are three key problems to resolve:
1. Difficult to diagnose issues. Each doc is very long and serves multiple purposes, often making it difficult to diagnose an issue and make a change to improve the AI output. 
2. Hard to update. When I do figure out what needs to be fixed, it is often the case that I have to make precision, almost "surgical", text changes in many different places across many documents. 
3. AI often stalls out. Even when using gemini 2.5 pro with a 1M+ token context window, will stop in the middle of generating the output. I think this is a symptom of how much the AI is trying to do in a one-shot prompt. My sense is that it might be better to provide a series of analysis that can be put together programmatically. 

---
## End Goal
Find the right set and number of documents to strike the balance of performance, reliability, and maintainability. 

## Get Options from AI


## Potential Path

- Using the MEARA docs mentioned, we decomposed them into an initial potential set of documents that might strike the balance of performance, reliability, and maintainability. 
- The draft write up of these potential files is in the file: madio_core_templates.md
- The draft set of dependencies is in the file: meara-doc-dependencies.yml

### Questions

- Is this the optimal set of documents to re-architect MEARA to strike the balance of performance, reliability, and maintainability. (madio_core_templates.md)
- Are the document dependencies correct (meara-doc-dependencies.yml)
- How can the documents be improved to make them easier to manage, maintain, diagnose and resolve issues, enhance and upgrade, etc?