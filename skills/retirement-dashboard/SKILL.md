---
name: retirement-dashboard
description: Help a household understand when they could retire, what they could afford to spend, and how long their savings might last. Build an editable dashboard covering each person's salary, college costs, taxes, inflation, and market downturns, using account balances or spending records when provided.
---

# Retirement dashboard

Build an editable model answering how much the household needs from investments, when each person could stop working, and what remains after college and at the chosen end age. Explain conclusions in everyday language. Treat scenario outcomes as conditional calculations, not forecasts or probabilities.

## Establish inputs

Read [inputs.md](references/inputs.md) before collecting or changing assumptions. Use [input.schema.json](references/input.schema.json) for the reference engine. Ask focused questions about material missing inputs while progressing independently. Prioritize ages/horizon, gross versus net salary and whose income stops, total spending including housing/healthcare, jurisdiction, account access/overlap, and college funding.

Separate supplied facts, verified records, provisional interpretations, and illustrative assumptions. Zero is not a substitute for unknown. Keep unresolved assumptions visible and editable. Do not import another household's personal data into a new model.

Reconcile screenshot totals against components and duplicate views before summing them. Exclude unavailable holdings from spendable capital. Add bank cash only when distinct. Keep provenance without account numbers in shareable outputs.

For card spending, use complete actual 12- and 24-month windows. Exclude payments, transfers and duplicate feeds; net refunds, separate business expenses, and check sync coverage. Partial feeds cannot establish the household budget. Add non-card costs once. A connector in another chat is not automatically available here; messaging that chat requires authorization.

## Build the model

Read [modeling.md](references/modeling.md) for calculations, scenarios and tests. Read [taxes.md](references/taxes.md) when taxes affect the answer.

Use the dependency-free reference implementation when its scope fits:

```sh
node scripts/generate-dashboard.mjs /absolute/path/inputs.json /absolute/path/output-directory
```

It produces a standalone editable dashboard, JSON results and annual CSVs. `assets/example.json` is fictional, not a recommended plan. The engine models aggregate accessible capital, configurable wage taxes and an explicitly estimated effective withdrawal tax. It does not perform a complete tax return or optimize account-level tax lots. Extend it or use another engine when limitations materially affect the task; explain the change.

Keep each spouse's income timing independent. A spouse's retirement date is not the other's stop date. A fixed-date comparison holds income timing and spending identical across cases. An earliest-retirement solver tests candidate dates separately and requires all expenses funded plus the selected real ending reserve.

Show college as separate annual lump sums, including living costs when requested. Use realistic entry years and overlapping enrollments, explicit public/private budgets, college inflation and education funds. Never count a 529 as both spendable assets and college funding. A no-529 stress case preserves the documented actual balance.

Exclude primary-home equity from spending unless an explicit sale/borrowing plan supplies net cash proceeds. At payoff remove only the mortgage payment; property taxes, insurance and upkeep continue. Do not add housing when already in total spending.

## Present results

Read [dashboard.md](references/dashboard.md) for visual outputs. Use the user's preferred artifact format. The standalone template works without connectors or internet access. Use available spreadsheet tools for requested workbooks; assumptions and formulas must recalculate.

Include active assumptions, scenario growth/inflation, a common-date chart, gross versus net withdrawals, monthly living needs separate from annual college draws, balances after college/at the horizon, and the first unfunded year. Distinguish nominal dollars from base-year purchasing power. Put tax-method limitations beside conclusions.

Explain 0% nominal growth, 3% growth with 3% inflation, and recession paths. Favorable scenarios must not silently get lower inflation. Sequence comparisons reverse a complete return series while holding inflation and other inputs equal unless requested otherwise.

When asked about affordable monthly spending, solve the highest budget that funds the selected horizon and reserve at the fixed income-stop date, showing separate base and stress results. Read modeling.md for the budget boundary conditions. When useful include escape velocity: constant returns needed to fund the horizon, retain the reserve or preserve initial real wealth. Preserve-at-end allows earlier declines. Large remaining-wealth gaps are residual balances after withdrawals; independently verify arithmetic before explaining compounding.

## Verify and deliver

Run `node scripts/test-model.mjs` after engine changes. Independently verify key cases: salary boundaries, college overlaps, tax gross-up, actual funded draws, depletion and inflation. Test an assumption edit and chart/summary agreement. Inspect readable light/dark colors at narrow/wide sizes when a permitted preview is available; otherwise identify the rendering limitation.

Preserve assumptions and unrelated content in follow-up edits. Keep saved calculator state without writing tool-visible metadata projections back. For Pages/shared documents use supported read/guard/write/readback workflows. A modeling request does not authorize publishing, sharing or messaging.

Before public packaging scan for names, balances, screenshots, transactions, account IDs, local paths, Page IDs and private URLs. Include synthetic data only. Create the requested local package; repository publishing or sharing personal financial data requires separate authorization.
