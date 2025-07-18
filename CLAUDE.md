# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Project**: MEARA (Marketing Effectiveness Analysis Report Agent)  
**Version**: 1.0  
**Last Updated**: 2025-07-18

## Development Environment Setup

### Python Environment
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Common Development Commands

**HTML Template Processing:**
```bash
# Run HTML template sanitization (full version with BeautifulSoup)
python tools/sanitize_html_templates.py

# Run simplified version (regex-only, no dependencies)
python tools/sanitize_html_templates_simple.py
```

**Markdown Cleaning:**
```bash
# Clean escaped markdown characters from all .md files in a directory
python clean_markdown.py docs_framework/

# Clean a single markdown file
python clean_markdown.py path/to/file.md

# Preview changes without modifying files (dry run)
python clean_markdown.py docs_framework/ --dry-run

# Verbose output showing detailed cleaning process
python clean_markdown.py docs_framework/ --verbose
```

**File Structure Validation:**
```bash
# Check for required framework files
ls -la docs_framework/
ls -la docs/specifications/
```

## Project Architecture

### Core Pipeline Architecture
MEARA follows a **"Pipelined Generalist"** model with 5 sequential steps:

1. **Ingest & Plan**: `Deep_Research_Brief.txt` → analysis plan
2. **Dimension Analysis Loop**: Analyzes 9 marketing dimensions using individual rubrics
3. **Synthesize & Recommend**: Root cause analysis and strategic recommendations  
4. **Extract Data for HTML**: Parses markdown → structured JavaScript data
5. **Generate Dashboard**: Injects data into HTML templates → interactive dashboard

### Key Framework Principles (SLC)
- **Simple**: One job per component, minimalist interface, clear data contracts
- **Lovable**: Clear feedback, confidence-building, transparent processing  
- **Complete**: Functionally correct, tested, seamlessly integrated

### Directory Structure
```
madio-meara/
├── docs/specifications/          # Core project specs (PRD, roadmap, SLC principles)
├── docs_framework/              # MADIO framework structure (00-07 numbered dirs)
│   ├── 00_project_system_instructions/
│   ├── 05_rubrics/             # 9 individual marketing dimension rubrics
│   └── 07_html_templates/      # HTML template files for dashboard
├── tools/                      # Utility scripts (HTML sanitization)
├── clean_markdown.py           # Standalone markdown cleaner for escaped characters
├── README-clean_markdown.md    # Documentation for markdown cleaning utility
├── archive/                    # Historical documentation and analysis
└── requirements.txt            # Python dependencies (BeautifulSoup4, etc.)
```

## Development Guidelines

### Task Assignment Process
- **Source of Truth**: Always work from assigned tasks in `docs/specifications/roadmap.md`
- **Task Format**: Milestone-based (M0.1, M1.2, etc.) with clear SLC criteria
- **Feature Specs**: Each task includes detailed specification following `FEATURE_SPECIFICATION_TEMPLATE.md`

### File-Based I/O Pattern
- **Input**: Text files (`Deep_Research_Brief.txt`, individual rubric files)
- **Processing**: Sequential pipeline steps with clear data contracts
- **Output**: Markdown reports + interactive HTML dashboard

### Orchestration Tools
- **Manual Testing**: Gemini CLI commands for individual pipeline steps
- **Automation**: n8n workflow for full pipeline orchestration
- **Interface**: Command-line interface, file-based I/O (no databases)

## Key Project Documents

### Foundation Documents (Read First)
- `docs/specifications/roadmap.md` - Master plan with specific tasks
- `docs/specifications/PRD.md` - Product requirements and vision  
- `docs/specifications/SLC_Principles.md` - Development methodology
- `docs/specifications/Experience_Goals.md` - Target user experience

### Implementation Guidance
- `docs/specifications/FEATURE_SPECIFICATION_TEMPLATE.md` - Template for all components
- `docs/specifications/dev-cycle.md` - Development process details

## Component Development Cycle

### 1. Task Assignment
- Receive specific task from roadmap (e.g., M1.1, M1.2)
- Read accompanying feature specification

### 2. Implementation Types
**For AI Pipeline Steps:**
- Write prompt files (.txt)
- Provide Gemini CLI commands
- Test with sample data

**For Scripting Steps:**  
- Write Python/Bash automation scripts
- Ensure pipeline integration

### 3. Validation Criteria
- **Simple**: Clean code, focused implementation, one clear job
- **Lovable**: Clear CLI output, informative status feedback
- **Complete**: Error handling, testing, seamless integration

## Critical Success Factors

### Pipeline Integration Requirements
- **Clear Input/Output**: Predictable data contracts between steps
- **Error Handling**: Graceful failure with informative diagnostics  
- **Status Feedback**: Transparent processing with progress indicators

### Experience Goal: "Expert Insight Through Reliable Automation"
- **Anticipation**: Clear overview of what will happen
- **Confidence**: Transparent processing, methodical progress
- **Delight**: High-quality automated output (markdown + HTML dashboard)

### Technical Standards
- **File-based I/O**: Simple, debuggable, version-controllable
- **Command-line Interface**: Minimalist, scriptable, reliable
- **Modular Design**: Each component independently testable

## Key Reminders
1. **Always reference roadmap** - Never work on unassigned tasks
2. **SLC is non-negotiable** - Every component must meet all three criteria
3. **"Perfect Handoff Confidence"** - Each step must seamlessly enable the next
4. **Experience goals drive decisions** - Maintain reliability and automation vibe