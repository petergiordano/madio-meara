# Stakeholder Reporting Architecture

## Purpose
Create multi-layered reporting structures that optimize information delivery for different organizational levels, enabling progressive disclosure and audience-specific communication while maintaining analytical integrity.

## Template Metadata
- **Template ID**: stakeholder_reporting_architecture
- **Version**: 1.0
- **Category**: Tier 3 - Integration & Output
- **Dependencies**: orchestrator, cross_dimensional_analysis
- **Required By**: visual_documentation_framework, implementation_roadmap

## Core Components

### 1. Three-Layer Reporting Framework
**[REPORTING_LAYERS]**

#### Executive Layer
**Purpose**: C-suite and board-level decision making
**[EXECUTIVE_STRUCTURE]**
```
1. Critical Business Impact (3-5 bullets)
2. Strategic Decisions Required (2-3 items)
3. Resource Requirements Summary
4. Success Metrics & Timeline
```

**Content Guidelines:**
- Maximum 1-2 pages
- Focus on business outcomes, not process
- Quantify impact in revenue/growth terms
- Clear yes/no decision points

#### Strategic Layer  
**Purpose**: VP/Director-level planning and coordination
**[STRATEGIC_STRUCTURE]**
```
1. Executive Summary (links to Executive Layer)
2. Key Findings by Priority (5-7 items)
3. Root Cause Analysis Summary
4. Strategic Recommendations (5-7)
5. Implementation Roadmap
6. Risk Mitigation Plan
```

**Content Guidelines:**
- Maximum 5-7 pages
- Balance strategic insight with tactical direction
- Include cross-functional dependencies
- Provide phased implementation approach

#### Tactical Layer
**Purpose**: Manager/Team-level execution
**[TACTICAL_STRUCTURE]**
```
1. Detailed Findings by Dimension
2. Evidence & Data Supporting Each Finding
3. Specific Action Items with Owners
4. Implementation Checklists
5. Success Metrics & KPIs
6. Technical Appendices
```

**Content Guidelines:**
- Comprehensive detail (15-30 pages)
- Include all evidence and citations
- Provide step-by-step guidance
- Enable autonomous execution

### 2. Progressive Disclosure Framework
**[DISCLOSURE_LEVELS]**

#### Information Hierarchy
```
Level 1: Key Impact Statement (1 sentence)
    ↓
Level 2: Critical Finding Summary (1 paragraph)
    ↓
Level 3: Detailed Analysis (1-2 pages)
    ↓
Level 4: Full Evidence Package (unlimited)
```

#### Navigation Structure
**[NAVIGATION_DESIGN]**
- Clear visual hierarchy with headers
- "Read more" links between levels
- Executive dashboard with drill-down capability
- Cross-references to detailed sections

### 3. Audience Adaptation Framework
**[AUDIENCE_ANALYSIS]**

#### Stakeholder Profiles
**Executive Stakeholders**
- **Information Needs**: ROI, competitive impact, strategic alignment
- **Decision Context**: Resource allocation, strategic direction
- **Communication Style**: Visual, quantitative, outcome-focused
- **Time Constraints**: 5-10 minute review

**Strategic Stakeholders**
- **Information Needs**: Implementation feasibility, cross-functional impact
- **Decision Context**: Planning, coordination, prioritization  
- **Communication Style**: Balanced detail, process-oriented
- **Time Constraints**: 30-45 minute review

**Tactical Stakeholders**
- **Information Needs**: Specific tasks, technical requirements, timelines
- **Decision Context**: Execution, troubleshooting, optimization
- **Communication Style**: Detailed, instructional, example-rich
- **Time Constraints**: Deep dive as needed

### 4. Two-Part Analysis Structure
**[REPORT_STRUCTURE]**

#### Part 1: Core Analysis
**[CORE_CONTENT]**
- Primary findings and recommendations
- Essential visuals and frameworks
- Critical path to success
- Must-read for all stakeholders

#### Part 2: Supporting Documentation
**[APPENDIX_CONTENT]**
- Detailed evidence tables
- Methodology documentation
- Technical specifications
- Additional data and research
- Reference for tactical execution

### 5. Cross-Layer Integration
**[INTEGRATION_FRAMEWORK]**

#### Vertical Alignment
```
Executive Bullet → Strategic Finding → Tactical Actions
"20% revenue gap" → "3 root causes" → "15 specific fixes"
```

#### Horizontal Consistency
- Consistent terminology across layers
- Aligned metrics and KPIs
- Unified visual language
- Coordinated timelines

## Implementation Guidelines

### Step 1: Stakeholder Mapping
1. Identify all report consumers
2. Document decision-making authority
3. Assess information needs
4. Define success criteria per audience

### Step 2: Content Stratification
1. Classify all findings by impact level
2. Assign content to appropriate layers
3. Create drill-down pathways
4. Ensure no critical information gaps

### Step 3: Layer Development
1. Write Executive Layer first (outcomes)
2. Expand to Strategic Layer (plans)
3. Detail in Tactical Layer (execution)
4. Validate vertical alignment

### Step 4: Progressive Disclosure Design
1. Create information hierarchy
2. Design navigation structure
3. Build visual connectors
4. Test user pathways

### Step 5: Quality Validation
1. Executive review (<10 minutes)
2. Strategic completeness check
3. Tactical executability test
4. Cross-layer consistency audit

## Quality Standards

### Content Integrity
- [ ] No information loss between layers
- [ ] Consistent data across all levels
- [ ] Clear traceability top to bottom
- [ ] Appropriate detail at each level

### Audience Optimization
- [ ] Executive layer drives decisions
- [ ] Strategic layer enables planning
- [ ] Tactical layer supports execution
- [ ] Each layer self-contained

### Navigation Excellence
- [ ] Intuitive drill-down paths
- [ ] Clear visual hierarchy
- [ ] Effective cross-references
- [ ] Smooth user experience

## Integration Points

### Input Requirements
- Analysis findings from `cross_dimensional_analysis`
- Strategic priorities from `strategic_framework`
- Visual assets from `visual_documentation_framework`

### Output Deliverables
- Three-layer report structure
- Progressive disclosure navigation
- Audience-optimized content
- Integrated appendices

## Customization Variables

**[LAYER_NAMES]**: Custom naming for your organizational levels
**[PAGE_LIMITS]**: Specific length constraints per layer
**[VISUAL_STANDARDS]**: Organization's design guidelines
**[DELIVERY_FORMATS]**: PDF, slides, interactive dashboard
**[APPROVAL_WORKFLOW]**: Review and sign-off process

## Example Application

### Marketing Effectiveness Report
```
EXECUTIVE LAYER:
• 30% revenue gap traced to positioning issues
• $2M investment needed over 6 months
• Expected ROI: 150% within 12 months

    ↓ [See Strategic Details]

STRATEGIC LAYER:
Key Finding: Unclear value proposition causing:
- 50% lower conversion rates
- 40% competitive win rate
- 60% longer sales cycles

    ↓ [See Tactical Implementation]

TACTICAL LAYER:
Action 1.1: Rewrite homepage headline
- Current: "Enterprise Software Solutions"
- Proposed: "Cut Integration Time by 75%"
- Owner: Marketing Manager
- Timeline: Week 1
```

This architecture ensures every stakeholder receives precisely the information they need to make decisions and take action, while maintaining complete analytical integrity across all organizational levels.