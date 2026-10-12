# Calculations and scenarios

First-year price index is 1. Subsequent years multiply by that year's inflation. Real ending capital = nominal ending capital ÷ price index. Label real amounts with the first year. End-age balances include the last year's expenses.

Income is active at `start_year <= year < stop_year`. Comparisons override only `optimize_stop` incomes. College costs occur as annual lump sums for years Y through Y+years−1, including overlapping children. Education funds are separate. The annual convention deducts all expenses/college before growth; it is conservative relative to exact monthly/semester dates. Monthly-equivalent displays do not change the timing.

## Cash flow

1. Release explicitly accessible accounts once; apply dated net cash events.
2. Calculate living costs, college, education-fund use, net wages and other after-tax income.
3. Net gap = living + college − education funding − net wages − other income + net event outflows.
4. Required gross draw = max(gap, 0) ÷ (1 − effective withdrawal tax).
5. Funded draw = min(available portfolio, required draw); remaining cash surplus becomes a contribution.
6. Unfunded net spending = (required − funded) × (1 − effective withdrawal tax).
7. Ending capital = (opening − funded draw + surplus) × (1 + nominal return).

Never let negative capital finance spending. Keep required/funded draws separate. Zero after depletion is failure to fund later expenses, not success with nothing left. Later recovery does not erase earlier shortfalls.

Monthly living draw excludes college. Allocate income to living first, then college, then events. Show an event draw separately so allocations reconcile to total gross draws.

## Illustrative cases

| Case | Nominal total return | Living inflation |
| --- | --- | --- |
| Slow | 3% | Base inflation |
| Base | 5.5% | Base inflation |
| Middle | 6.5% | Base inflation |
| Favorable | 7.5% | Base inflation |
| Early recession | −30%, −10%, +15%, +10%, then 4.5% | Explicit stress path, e.g. 4.5% first three years then base |
| Late recession | Full early-return series reversed | Same inflation as early |

These are editable examples, not forecasts for an actual portfolio. At 3% inflation, 3% nominal growth gives zero real growth before withdrawals; 0% nominal growth gives negative real growth. Reverse the entire expanded series, not just four shock years. Identify whether recession begins now or at retirement.

Hold salary dates, spending, college, tax and events fixed in comparison charts. Disclose explicit stress-inflation differences. For isolating return timing, keep inflation identical between early and late paths.

## Solvers and sensitivities

Earliest retirement tests every candidate stop year. Qualify only when all annual shortfalls are zero within tolerance and the terminal real reserve is met. No qualifying date must remain explicit; salary continuing beyond the horizon is not retirement.

Escape velocity solves constant nominal returns at a fixed stop date/base inflation for full funding, the selected reserve and original real capital. Test bisection bounds. Preservation at the endpoint permits earlier declines and college-era drawdowns; it is not an annual no-decline rule.

When asked how much monthly spending is affordable through a selected age, hold the income stop date and all other assumptions fixed, vary only the chosen spending phase, and solve the highest after-tax budget that funds every year and retains the reserve. Use explicit lower/upper spending bounds, preserving required housing and healthcare costs. Report infeasibility or a tested boundary honestly. Give separate sustainable budgets for base and stress cases; a favorable-only budget is not a conservative recommendation.

Test spending stages, working years, salary raises/no raises, public/private college, education funding/no funding, inflation, withdrawal-tax estimates, longevity to 90–95, mortgage payoff and return assumptions. Do not combine unlabeled favorable changes. Deterministic paths have no Monte Carlo success probability.

## Verification

- Reconcile accounts, duplicates, inaccessible balances, delayed access and distinct cash. Home equity stays separate.
- Check wage cessation, ages, first-year deflator, college start/overlap/end, shared funds and mortgage-only payoff.
- Reconcile cash gap, tax gross-up, living/college/event draws and funded shortfalls.
- Independently check constant-return capital with future values of starting capital and each cash flow. Use cumulative products for varying returns. Verify depletion.
- Change an input and check affected summaries/charts. Reject missing values and invalid rates. Preserve state without changing assumptions at load.
- Large remaining-wealth gaps are residuals after spending; verify arithmetic before explaining compounding.
