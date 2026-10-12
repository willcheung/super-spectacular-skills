# Tax scope

Separate gross salary, take-home cash, net investment cash need, gross portfolio sales and realized taxable income. Brokerage transfers are not themselves identical to taxable income; gains depend on proceeds and basis. [IRS capital gains](https://www.irs.gov/taxtopics/tc409).

Before supplying progressive schedules, verify year, jurisdiction, filing status, deductions, credits and payroll rules from official sources. Apply household income-tax brackets to joint wages; payroll wage caps may apply separately to each earner. The generic progressive method accepts national/state schedules and payroll caps/thresholds, but does not implement every local rule or its investment-income interactions.

Brackets are ascending `{up_to, rate}`, ending with `up_to: null`. Payroll components specify a rate, optional cap, threshold, and whether calculated per income or household. `tax.salary.index_rate` indexes deductions, brackets and payroll caps/thresholds; set the applicable component's `indexed: false` for a fixed threshold.

Pretax saving reduces take-home wages and taxable wages. It is reported separately and not automatically added to accessible capital. Extend account-level projections when these savings materially affect retirement resources.

The reference engine uses a combined effective withdrawal-tax allowance. An assumed gain share × combined tax rate can supply a provisional estimate. State its federal/state scope. Do not add another blanket state tax if included already.

A complete model solves gross sales and taxes together using wages, ordinary investment income, gain realization, federal capital-gains stacking, state treatment, NIIT, deductions/credits and tax-lot basis. Traditional distributions and qualified Roth draws need distinct treatment; a brokerage assumption cannot silently cover mixed accounts.

California generally taxes capital gains at ordinary state income-tax rates. [California capital gains](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html). NIIT depends on investment income and modified adjusted gross income. [IRS NIIT](https://www.irs.gov/individuals/net-investment-income-tax).

No statutory schedules are bundled. The example uses synthetic effective allowances. Progressive wages plus effective investment tax still do not produce a complete combined annual tax return. Unknown basis/dividends/deductions require explicit provisional assumptions and sensitivities. Charge recurring dividend/interest tax in returns or cash flows once.
