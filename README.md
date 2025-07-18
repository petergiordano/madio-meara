# MEARA → MADIO Framework Conversion Project

## Project Overview

This project converts the MEARA (Marketing Effectiveness Analysis Reporting Agent) from its current Google Docs-based Claude Project/Gemini Gem implementation into a comprehensive MADIO-start framework.

### What is MEARA?
MEARA is a sophisticated Marketing Effectiveness Analysis Reporting Agent that provides:
- Complex marketing analysis capabilities
- Strategic evaluation and reporting
- Multi-dimensional assessment frameworks
- Evidence-based recommendations

### What is MADIO?
MADIO (Modular AI Declarative Instruction and Orchestration) is a production-ready framework with 14 standardized templates organized in a hierarchical structure:
- **Tier 1**: `project_system_instructions` (mandatory)
- **Tier 2**: `orchestrator` (mandatory) 
- **Tier 3**: 12 supporting templates for content, analysis, visual, and implementation needs

## Project Structure

```
MADIO-MEARA/
├── .claude/
├── archive/
├── docs/
└── docs_framework/
    ├── 00_project_system_instructions/
    │   └── project_system_instructions.md
    ├── 01_persona/
    │   └── character_voice_authority.md
    ├── 02_process_and_planning/
    │   ├── methodology_framework.md
    │   └── orchestrator.md
    ├── 03_knowledge_base/
    │   ├── competitive_intelligence_framework.md
    │   ├── implementation_planning.md
    │   └── root_cause_analysis_system.md
    ├── 04_strategic_frameworks/
    │   └── strategic_analysis_framework.md
    ├── 05_rubrics/
    │   └── unified_evaluation_framework.md
    ├── 06_output_templates/
    │   └── reporting_and_visualization.md
    └── 07_html_templates/
```

## Project Status

**Phase**: Environment Setup Complete
**Next Step**: MADIO Research and MEARA Documentation Analysis

## Key Files

- `MEARA_MADIO_CONVERSION_MAPPING.md` - Master conversion strategy document
- `analysis/meara_system_analysis.md` - Comprehensive MEARA capability inventory
- `mapping/madio_template_requirements.md` - MADIO template selection and justification
- `implementation/conversion_roadmap.md` - Phase-by-phase execution plan

## Development Setup

### Prerequisites
- Python 3.7 or higher
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/petergiordano/madio-meara.git
   cd madio-meara
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Tools Usage
The `tools/` directory contains utilities for working with HTML templates:

- **sanitize_html_templates.py**: Full-featured script using BeautifulSoup for robust HTML parsing
- **sanitize_html_templates_simple.py**: Lightweight regex-only version with no dependencies

Run the sanitization tool:
```bash
python tools/sanitize_html_templates.py
```

## Conversion Methodology

This conversion follows the proven methodology used for the "Chronicles of Khronexia: Who Would Win" project, adapted for MEARA's marketing analysis complexity.

## Success Criteria

1. **Complete Capability Preservation**: All MEARA functions maintained in MADIO format
2. **Framework Enhancement**: Identify opportunities to improve MADIO templates
3. **Production Readiness**: Deployable across OpenAI CustomGPT, Gemini Gem, and Claude Project
4. **Quality Assurance**: Comprehensive testing and validation strategy

---

*Last Updated: July 2025*
*Project Lead: MADIO Framework Development Assistant*