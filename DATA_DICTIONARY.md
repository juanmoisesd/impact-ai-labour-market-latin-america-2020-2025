# Data Dictionary

## Impact of Artificial Intelligence on the Labour Market in Latin America (2020-2025)

### automation_by_sector.csv
| Field | Type | Description |
|-------|------|-------------|
| country | string | Latin American country |
| sector | string | Economic sector |
| year | integer | Reference year |
| automation_index | float | Automation risk index (0-1) |
| jobs_at_risk_pct | float | % of jobs at risk |

### labour_displacement.csv
| Field | Type | Description |
|-------|------|-------------|
| country | string | Country |
| year | integer | Projected year |
| displaced_jobs | integer | Estimated displaced jobs |
| scenario | string | Optimistic/Baseline/Pessimistic |

### emerging_occupations.csv
| Field | Type | Description |
|-------|------|-------------|
| occupation | string | Occupation name |
| growth_pct | float | Projected growth % |
| required_skills | string | Skills list |

### labour_policies.csv
| Field | Type | Description |
|-------|------|-------------|
| country | string | Country |
| policy | string | Policy description |
| type | string | Regulation/Incentive/Training |
| implementation_year | integer | Year of implementation |