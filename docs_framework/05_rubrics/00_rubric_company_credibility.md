# Rubric 00: Company Credibility
# 00_rubric_company_credibility.md


## Purpose
To gather and assess foundational data about a company's credibility, stability, and market reputation. This rubric does not produce a score for the final report but provides essential context and evidence for the 9 primary analytical dimensions.

## Template Metadata
- **Template ID**: rubric_company_credibility
- **Version**: 1.0
- **Status**: Draft
- **Designation**: Foundational Input
- **Dependencies**: None
- **Required By**: orchestrator, root_cause_analysis_system, all_scoring_rubrics

## Core Components
This rubric is a data collection framework. The collected points serve as evidence for other analyses.

### A. Financial & Corporate Stability
| Metric                  | Source      | Value / Finding |
| :---------------------- | :---------- | :-------------- |
| **Year Founded** | LinkedIn/Web |                 |
| **HQ Location** | LinkedIn/Web |                 |
| **Employee Count** | LinkedIn    |                 |
| **Funding Amount** | Crunchbase, etc. |                 |
| **Last Funding Date** | Crunchbase, etc. |                 |
| **Key Investors** | Crunchbase, etc. |                 |

### B. Employer Brand & Culture
| Metric                      | Source     | Value / Finding |
| :-------------------------- | :--------- | :-------------- |
| **Glassdoor Rating (/5)** | Glassdoor  |                 |
| **Comparably Culture Grade** | Comparably |                 |
| **eNPS (/100)** | Comparably |                 |
| **Average Employee Tenure** | LinkedIn   |                 |

### C. Leadership & Influence
| Metric                          | Source     | Value / Finding (Qualitative) |
| :------------------------------ | :--------- | :---------------------------- |
| **Founder Brand Strength** | Various    |                               |
| **Executive Team Rating** | Comparably |                               |
| **Key Influencers Coverage** | Various    |                               |

## Evaluation & Output Format
This rubric is **not** assigned a summative rating (e.g., 'Exceptional'). Its output is a structured data object containing the collected facts. This data serves as evidence for analysis within the 9 core dimensions.

For example, a low "Average Employee Tenure" might be used as evidence to explain a finding of "Inconsistent Brand Messaging" in rubric #07.

## Integration Points

### Inputs From
- Publicly available data from sources like LinkedIn, Glassdoor, Comparably, Crunchbase, and news articles.

### Outputs To
- A structured data object (e.g., JSON) to the `orchestrator`, which then makes this contextual data available to all subsequent rubric analysis steps.