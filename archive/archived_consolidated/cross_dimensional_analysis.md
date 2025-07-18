# Cross-Dimensional Analysis Framework

## Purpose
Enable systematic identification of root causes versus symptoms across multiple evaluation dimensions, documenting cascade effects and eliminating analytical redundancy while maintaining comprehensive coverage.

## Template Metadata
- **Template ID**: cross_dimensional_analysis
- **Version**: 1.0
- **Category**: Tier 3 - Analysis & Evaluation
- **Dependencies**: methodology_framework, rubrics_evaluation
- **Required By**: orchestrator, strategic_quality_assurance

## Core Components

### 1. Interconnected Dimensions Model
**[DIMENSION_RELATIONSHIPS]**
Define how your evaluation dimensions interact and influence each other:
```
Dimension A → Dimension B (Causal)
Dimension B ↔ Dimension C (Bidirectional)
Dimension C ← Dimension D (Dependency)
```

**[SYSTEM_COMPONENTS]**
Treat dimensions as systemic components rather than isolated elements:
- Primary dimensions that drive system behavior
- Secondary dimensions that reflect system state
- Tertiary dimensions that indicate system outcomes

### 2. Root Cause Identification Framework
**[CAUSE_IDENTIFICATION]**
Distinguish fundamental causes from cascading symptoms:

**Root Cause Indicators:**
- Appears across 3+ dimensions
- Cannot be explained by another issue
- Directly impacts business outcomes
- Requires strategic intervention

**Symptom Indicators:**
- Manifests in 1-2 dimensions
- Can be traced to deeper issue
- Tactical rather than strategic
- Addressable through execution

**[CAUSE_HIERARCHY]**
```
Root Cause 1: [FUNDAMENTAL_ISSUE]
├── Symptom A in Dimension 1
├── Symptom B in Dimension 3
└── Symptom C in Dimension 5
```

### 3. Cascade Effect Documentation
**[CASCADE_ANALYSIS]**
Map how issues flow between dimensions:

**Cascade Pattern Template:**
```
Trigger: [INITIAL_ISSUE] in [DIMENSION]
   ↓
Primary Impact: [EFFECT] in [DIMENSION]
   ↓
Secondary Impact: [EFFECT] in [DIMENSION]
   ↓
Tertiary Impact: [EFFECT] in [DIMENSION]
```

**[IMPACT_SEVERITY]**
- **Critical**: Affects 5+ dimensions or core business metrics
- **High**: Affects 3-4 dimensions with revenue impact
- **Medium**: Affects 2 dimensions with efficiency impact
- **Low**: Affects 1 dimension with limited scope

### 4. Redundancy Elimination Logic
**[DEDUPLICATION_FRAMEWORK]**
Prevent repetitive analysis while maintaining completeness:

**Cross-Reference Rules:**
1. If issue explained as root cause, don't repeat in symptom dimensions
2. Reference primary analysis location when issue appears elsewhere
3. Use "See [Dimension X]" notation for cross-references
4. Maintain issue visibility without redundant explanation

**[COMPLETENESS_VALIDATION]**
Ensure no critical issues are missed:
- All dimensions reviewed systematically
- Cross-dimensional patterns identified
- Root causes traced to all manifestations
- Strategic implications captured

### 5. Visual Relationship Mapping
**[RELATIONSHIP_DIAGRAMS]**
Required visual documentation:

**Network Diagram Structure:**
```
[Root Cause] --→ [Dimension A Impact]
     |              ↓
     +--------→ [Dimension B Impact]
                    ↓
               [Business Outcome]
```

**[VISUALIZATION_STANDARDS]**
- Use consistent symbols for relationship types
- Color-code by severity level
- Include impact quantification where possible
- Provide clear legends and keys

## Implementation Guidelines

### Step 1: Dimension Mapping
1. List all evaluation dimensions
2. Identify natural relationships between dimensions
3. Classify relationship types (causal/dependency/bidirectional)
4. Document expected interaction patterns

### Step 2: Evidence Collection
1. Gather findings for each dimension
2. Tag potential root causes vs. symptoms
3. Track cross-dimensional appearances
4. Document evidence trails

### Step 3: Pattern Analysis
1. Cluster related findings across dimensions
2. Identify issues appearing in 3+ dimensions
3. Trace symptom chains to root causes
4. Validate cause-effect relationships

### Step 4: Cascade Documentation
1. Map primary → secondary → tertiary impacts
2. Quantify severity at each level
3. Identify intervention points
4. Document ripple effects

### Step 5: Synthesis & Validation
1. Consolidate root causes (target: 3-5)
2. Verify all symptoms traced to roots
3. Eliminate redundant explanations
4. Validate strategic completeness

## Quality Standards

### Analysis Integrity
- [ ] All dimensions systematically evaluated
- [ ] Root causes explain 80%+ of symptoms
- [ ] No circular reasoning in cause identification
- [ ] Evidence supports all causal claims

### Documentation Completeness
- [ ] Visual relationship map created
- [ ] Cascade effects documented
- [ ] Cross-references properly noted
- [ ] Strategic implications identified

### Output Validation
- [ ] 3-5 root causes identified
- [ ] All major symptoms mapped
- [ ] Redundancy eliminated
- [ ] Actionable insights preserved

## Integration Points

### Input Requirements
- Completed dimensional evaluations from `rubrics_evaluation`
- Evidence collection from `research_protocols`
- Strategic context from `deep_research_integration`

### Output Deliverables
- Root cause identification for `methodology_framework` Step 4
- Cross-dimensional insights for `strategic_framework`
- Visual diagrams for `visual_documentation_framework`
- Validated findings for `strategic_quality_assurance`

## Customization Variables

**[PROJECT_DIMENSIONS]**: Your specific evaluation dimensions
**[SEVERITY_THRESHOLDS]**: Custom impact classification levels
**[RELATIONSHIP_TYPES]**: Additional relationship categories beyond causal/dependency/bidirectional
**[VISUALIZATION_TOOLS]**: Preferred diagram formats and tools
**[EVIDENCE_STANDARDS]**: Specific validation requirements

## Example Application

### Marketing Effectiveness Analysis
```
Root Cause: "Unclear Value Proposition"
├── Symptom: Poor conversion (Dimension 1: Positioning)
├── Symptom: Low engagement (Dimension 2: Journey)
├── Symptom: Weak differentiation (Dimension 6: Competitive)
└── Business Impact: 40% below revenue target

Cascade Effect:
Unclear Value → Confused Messaging → Poor Content → Low Conversion → Revenue Gap
```

This framework transforms multi-dimensional analysis from isolated assessments into integrated strategic insights, ensuring no critical patterns are missed while avoiding analytical redundancy.