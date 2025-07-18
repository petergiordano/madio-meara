# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the MEARA → MADIO Framework Conversion Project. MEARA (Marketing Effectiveness Analysis Reporting Agent) is being converted from Google Docs-based implementation into a comprehensive MADIO-start framework.

## Project Type

This is a documentation and framework development project, not a traditional code repository. The project consists entirely of Markdown files that define templates and analysis frameworks for B2B SaaS marketing effectiveness analysis.

## Key Architecture

### MADIO Framework Structure
The project follows a hierarchical template system:
- **Tier 1**: `project_system_instructions.md` - Core system identity and authorization
- **Tier 2**: `orchestrator.md` - Primary execution guide coordinating all activities  
- **Tier 3**: 8 supporting templates covering analysis, evaluation, output, and specialized needs

### Template Consolidation
Original MEARA documents (5 files) have been consolidated into 10 MADIO templates:
1. Core templates (2): System instructions and orchestrator
2. Analysis & Evaluation (4): Methodology, evaluation framework, strategic analysis, root cause analysis
3. Output & Implementation (2): Reporting/visualization, implementation planning
4. Specialized (2): Competitive intelligence, character voice authority

### Document Dependencies
Templates reference each other through explicit dependency declarations. The orchestrator (`orchestrator.md`) serves as the central coordination point referencing all other templates.

## Working with This Project

### No Build Commands
This is a documentation project with no build, test, or deployment commands. All work involves editing Markdown files.

### Key Files to Understand
- `MADIO_MEARA_MASTER_TRACKING.md` - Project status and template mapping
- `madio_templates/project_system_instructions.md` - System identity and core purpose
- `madio_templates/orchestrator.md` - Execution framework and dimension definitions
- `README.md` - Project overview and structure

### Project Goals
1. Convert MEARA capabilities into MADIO template format
2. Maintain all original functionality while improving organization
3. Ensure compatibility with OpenAI CustomGPT, Gemini Gem, and Claude Project
4. Identify opportunities to enhance the MADIO framework itself

## Development Approach

When modifying templates:
1. Preserve all MEARA capabilities - no functionality should be lost
2. Maintain clear document dependencies and references
3. Follow MADIO template conventions for structure and formatting
4. Ensure content remains actionable and specific to B2B SaaS marketing analysis

The project prioritizes comprehensive marketing analysis capabilities over generic templates, with specific focus on B2B SaaS companies and AI-native organizations.