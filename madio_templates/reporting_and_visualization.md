# Reporting and Visualization Framework

## Purpose
Create multi-layered reporting structures with visual documentation standards for complex analytical findings, enabling progressive disclosure and stakeholder-specific communication.

## Template Metadata
- **Template ID**: reporting_and_visualization
- **Version**: 1.0
- **Dependencies**: unified_evaluation_framework, root_cause_analysis_system, strategic_analysis_framework
- **Required By**: orchestrator

## Core Components

### 1. Three-Layer Reporting Structure

#### Executive Layer (1-2 pages)
**Audience**: C-suite, board, investors
**Content**:
- Executive Summary (3-5 critical impacts)
- Critical Issues Summary (top 3 issues)
- Findings Relationship Map
- Implementation Priority Matrix

**Format Requirements**:
- Business outcome focus
- Quantified impacts (revenue/growth)
- Clear decision points
- Visual-heavy presentation

#### Strategic Layer (5-7 pages)
**Audience**: CMO, marketing leadership, founders
**Content**:
- Executive Summary link
- Key Findings by Priority (5-7)
- Root Cause Analysis Summary
- Strategic Recommendations (5-7)
- Implementation Roadmap
- Risk Mitigation Plan

**Format Requirements**:
- Strategic insight with tactical direction
- Cross-functional dependencies noted
- Phased implementation approach
- Industry terminology appropriate

#### Tactical Layer (15-30 pages)
**Audience**: Marketing specialists, implementation teams
**Content**:
- Detailed Findings by Dimension
- Evidence & Data Supporting Each Finding
- Specific Action Items with Owners
- Implementation Checklists
- Success Metrics & KPIs
- Technical Appendices

**Format Requirements**:
- Comprehensive detail
- Step-by-step guidance
- All evidence and citations
- Enables autonomous execution

### 2. Visual Documentation Standards

#### Findings Relationship Map
```
┌─────────────┐      ┌─────────────┐
│ Root Cause 1│─────▶│  Symptom A  │
└──────┬──────┘      └──────┬──────┘
       │                     │
       │ ┌─────────────┐     │
       └▶│  Symptom B  │     │
         └──────┬──────┘     │
                │            ▼
         ┌──────┴──────┐ ┌────────────┐
         │  Symptom C  │ │  Business  │
         └─────────────┘ │   Impact   │
                         └────────────┘
```

**Visual Encoding**:
- Node Size: Impact magnitude
- Color: Severity (red=critical, orange=high, yellow=medium, green=low)
- Line Thickness: Relationship strength
- Proximity: Logical grouping

#### Priority Matrix (2x2)
```
         High Impact
              │
    Quick     │     Strategic
    Wins      │     Initiatives
  ┌───────────┼───────────┐
  │     A     │     D     │
  │           │           │
  ├───────────┼───────────┤
  │     B     │     C     │
  │           │           │
  └───────────┴───────────┘
Low │                   │ High
Effort                Effort
              │
         Low Impact
```

#### Cascade Diagrams
```
Initial Problem
    │
    ├─▶ Primary Impact 1
    │      │
    │      ├─▶ Secondary Impact A
    │      │      │
    │      │      └─▶ Tertiary Impact α
    │      │
    │      └─▶ Secondary Impact B
    │
    └─▶ Primary Impact 2
           │
           └─▶ Secondary Impact C
```

**Severity Indicators**:
- Critical (█): Business operations affected
- High (▓): Revenue/growth impact
- Medium (▒): Efficiency degradation
- Low (░): Limited scope

#### Implementation Timeline
```
Phase 1: Foundation    ████████░░░░░░░░░░░░
Phase 2: Core Build    ░░░░████████████░░░░
Phase 3: Optimization  ░░░░░░░░░░░░████████
Phase 4: Scale         ░░░░░░░░░░░░░░░░████

Timeline: Q1    Q2    Q3    Q4
```

### 3. Progressive Disclosure Framework

**Information Hierarchy**:
```
Level 1: Key Impact Statement (1 sentence)
    ↓
Level 2: Critical Finding Summary (1 paragraph)
    ↓
Level 3: Detailed Analysis (1-2 pages)
    ↓
Level 4: Full Evidence Package (unlimited)
```

**Navigation Elements**:
- Clear visual hierarchy
- "Read more" links between levels
- Executive dashboard with drill-down
- Cross-references to detailed sections

### 4. Stakeholder-Specific Formatting

#### Executive Formatting
- Bullet points for key findings
- Bold for critical numbers
- Visual-to-text ratio: 60/40
- Maximum 25 words per bullet

#### Strategic Formatting
- Short paragraphs (3-4 sentences)
- Subheadings every 2-3 paragraphs
- Visual-to-text ratio: 40/60
- Industry terminology included

#### Tactical Formatting
- Detailed explanations
- Step-by-step instructions
- Complete evidence citations
- Technical specifications

### 5. Data Visualization Guidelines

#### Chart Selection
- **Comparison**: Bar/column charts
- **Composition**: Pie/stacked bars
- **Distribution**: Histograms/scatter
- **Relationship**: Network/bubble
- **Trend**: Line/area charts

#### Visual Standards
- Maximum 5-7 colors
- Consistent palette throughout
- Clear legends and labels
- Accessibility compliant
- Print-friendly versions

## Implementation Process

### Content Stratification
1. Classify findings by impact level
2. Assign content to appropriate layers
3. Create drill-down pathways
4. Ensure no critical gaps

### Layer Development
1. Executive Layer first (outcomes)
2. Strategic Layer (plans)
3. Tactical Layer (execution)
4. Validate vertical alignment

### Visual Creation
1. Sketch key diagrams
2. Apply encoding standards
3. Test readability
4. Build interactive versions

### Quality Validation
- Executive review (<10 min)
- Strategic completeness
- Tactical executability
- Cross-layer consistency

## Integration Points

### Inputs From
- unified_evaluation_framework: Dimension ratings and findings
- root_cause_analysis_system: Root causes and relationships
- strategic_analysis_framework: Strategic opportunities

### Outputs To
- orchestrator: Complete layered report structure

## Deliverables

### Report Components
1. Executive Brief (PDF, 2 pages)
2. Strategic Report (PDF/slides, 5-7 pages)
3. Tactical Playbook (PDF, 15-30 pages)
4. Visual Asset Library (PNG/SVG)

### Tool Recommendations
- **Diagrams**: Draw.io, Lucidchart, Miro
- **Data Charts**: Tableau, Power BI
- **Infographics**: Canva, Adobe
- **Code-Based**: D3.js, Plotly, Mermaid

## Success Metrics
- Executive engagement in <10 minutes
- Strategic clarity achieved
- Tactical completeness verified
- Visual clarity validated
- No information loss between layers