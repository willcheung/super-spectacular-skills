# Input contract

Money uses one currency. Rates are decimals (`0.03` means 3%). Years are calendar years. Dollar inputs identify their price year. `input.schema.json` defines the executable fields; a complete financial model may need additional inputs below.

## Household and income

| Variable | Meaning |
| --- | --- |
| `start_year`, `horizon_years`, `adults[].age_at_start` | Last modeled age = first age + horizon − 1. Explain whether the horizon reaches each spouse's goal age. |
| `currency` | Currency code; explicitly convert mixed currencies. |
| `incomes[].gross_annual` | Gross salary in first-year dollars. Confirm bonuses/equity compensation. |
| `growth_rate`, `start_year`, `stop_year` | Each income's independent timing. Stop year is the first full year without it. |
| `optimize_stop` | Income(s) whose dates the solver varies; other incomes retain their dates. |
| `pretax_annual`, `benefits_annual` | Paycheck deductions; pretax saving is reported separately and not automatically added to spendable capital. |
| `other_income[]` | Explicit after-tax pensions, benefits or other income with start/end years and growth. No assumed credit for unknown benefits. |
| `comparison_stop_year` | Common manual stop date, separate from the earliest-date solver. |

## Accounts and home

| Variable | Meaning |
| --- | --- |
| `accounts[].id`, `balance`, `source`, `as_of`, `status` | Canonical anonymous account IDs and evidence; exclude account numbers from public files. |
| `duplicate_of` | Known duplicate account. Similar totals alone do not prove overlap. |
| `unavailable`, `available_year` | Excluded amount and access year. Delayed accounts enter once at their entered value; no pre-access growth is invented. |
| `type`, `cost_basis`, `gain_fraction` | Cash, brokerage, traditional, Roth, education or other. Basis/access affect tax treatment; a combined rate does not settle them. |
| `home.value`, `home.debt` | Descriptive equity, excluded from spendable funds. |
| `home.mortgage_monthly`, `mortgage_end_year` | Mortgage-only nominal payment and last payment year; never include property taxes here. |
| `home.nonmortgage_monthly` | Taxes, insurance, upkeep and other housing in starting-year dollars, used only when a spending phase excludes housing. |
| `events[]` | Dated nominal after-tax inflow/outflow, such as net sale proceeds or a repair. Do not duplicate an account release. |

Education accounts are excluded from spendable assets. `college_funds[].account_id` uses one linked education account's balance once. Otherwise a fund balance must be confirmed distinct. Shared siblings can reference one fund without duplicating it.

## Spending and college

| Variable | Meaning |
| --- | --- |
| `spending.phases[]` | Monthly after-tax budget in first-year dollars; stages may cover children at home, two adults and later life. Explicit `includes_housing` prevents double counting. |
| `healthcare_extra_annual` | Costs missing from the monthly budget; verify coverage before setting zero. |
| `spending.inflation` | Common living inflation unless explicitly overridden by a scenario. |
| `children[].age_at_start`, `college_start_year`, `years`, `plan` | Explicit academic timing and public/private plan. Age-derived entry dates remain assumptions. |
| `college.plans` | All-in budgets split into tuition, room/board and other costs; planning inputs are not published tuition averages. |
| `college.price_year`, `inflation` | Base cost year and college-specific inflation. |
| `college_funds[].balance`, `growth_rate`, `account_id` | Separate education resources; optional link to a canonical education account. |
| `college.credit_funds` | False keeps actual balances documented but gives no funding credit in the stress case. |
| `reserve_real` | Required terminal capital in first-year purchasing power, not an annual expense. |

## Taxes and scenarios

`tax.salary.mode` is `effective` (one total including income/payroll taxes) or `progressive` (configured national/state brackets, deductions, indexing and payroll components). No current statutory schedule is bundled. `tax.withdrawal_effective_rate` is a combined planning allowance on gross portfolio sales, not a statutory withdrawal tax.

Scenario fields are `id`, `label`, `long_run_return`, `returns`, `reverse_returns`, optional `inflations`, and optional `inflation`. Expand returns through the entire horizon before reversing. Returns are nominal totals after fees/recurring investment-tax drag but before separate withdrawal tax. Avoid charging dividends/interest tax twice.

## Additional inputs for a complete model

Allocation/concentrated holdings; account-level access and withdrawal order; tax lots and long/short-term basis; dividends/interest; filing status/jurisdiction; deductions/credits; NIIT; retirement-account access exceptions/penalties; RMDs; benefit estimates; mortgage amortization/reassessment; healthcare and long-term care; estate goals; education ownership/restrictions; survivor spending and longevity.

Metadata retains unresolved facts but does not calculate them. State which inputs actually drive results.
