# When Can I Retire?

An AI skill that helps you work through a practical question: **When could I stop working, and how much could we afford to spend?** It turns your household assumptions into an editable dashboard with clear charts.

You can compare a few more working years, different spending budgets, college costs, taxes, inflation, and market downturns. It shows how much you would need to take from investments and whether the money lasts through the age you choose.

## What it can help you answer

- How much would we need to take from savings each month while one person still works?
- Could I retire now, in five years, or after the children finish college?
- What monthly budget would our investments support?
- How much would remain after college and at ages 80, 90, or 95?
- What changes if we pay for public or private college?
- What happens if investments grow slowly or a recession hits early in retirement?
- How much investment growth would cover spending without using up our savings?

Each person's salary has its own stop date. College appears as a separate yearly bill, so it does not inflate the monthly living budget. The home is shown separately from money available to spend.

## Use it with your AI assistant

Install it using the [repository instructions](../../README.md#install), or point your assistant at [SKILL.md](SKILL.md). Compatible assistants include Codex, Claude Code, and others that support Agent Skills.

Then ask:

```text
Use when-can-i-retire to help me understand when we could retire.
Ask me for the missing details, build an editable dashboard, and compare
retiring now with working five more years. Include college, taxes,
inflation, slow investment growth, and early and late recessions.
Explain the results in everyday language.
```

For a follow-up:

```text
Keep the retirement date the same, but compare a lower monthly budget
and public versus private college. Show what remains at age 90.
```

## Information to have ready

| Information | Why it matters |
| --- | --- |
| Ages and how long you want the plan to last | Sets the number of years your savings must cover |
| Account balances and account types | Identifies money you can use and avoids counting the same account twice |
| Salaries before taxes and each person's work plans | Estimates take-home pay and keeps the two retirement dates separate |
| Monthly spending, including housing and healthcare | Establishes the living costs the plan must fund |
| State or country where you pay taxes | Helps estimate salary and investment taxes |
| Children's ages, college plans, and education savings | Sets the timing and size of college bills |
| Mortgage-only payment and payoff date | Removes the loan payment at payoff while keeping property tax and upkeep |

Account screenshots and complete spending exports can help. If a number is missing, the assistant should ask or label an editable assumption. It should not pretend incomplete card records establish your full spending.

## How to read the charts

The example includes six paths: 3% annual growth, base, middle, favorable, early recession, and late recession. The percentages are assumptions you can change. Recession charts show the calendar years of losses and recovery.

All paths in a comparison use the same retirement date. “Future dollars” means the amount you might see in the account. “Starting-year dollars” means what that amount could buy after inflation. For example, 3% investment growth with 3% inflation gives no growth in buying power before withdrawals.

If a path reaches zero and reports an unfunded year, the plan runs out of money before paying all the expenses. A large balance in a favorable case does not make that outcome a prediction.

## Try the fictional example yourself

If you have Node.js 18 or newer, run these commands from this skill's folder:

```sh
node scripts/generate-dashboard.mjs assets/example.json ./demo
```

Open `demo/dashboard.html` in your browser. Change the common settings or ask your assistant to help edit the full assumptions. You can save the settings and download the yearly figures. The generator runs locally without accounts, downloads, or an internet connection.

Developers can run the calculation tests with:

```sh
node scripts/test-model.mjs
```

The [input guide](references/inputs.md) explains every variable; the [JSON schema](references/input.schema.json) defines the data format.

## Privacy and limits

**Every bundled household example is fictional.** The skill contains no real account screenshots, transactions, account numbers, names, or private financial records. Keep your own inputs and generated reports in `local/`, which this folder's ignore rules exclude from Git. Review files before publishing; ignore rules cannot protect files that are already tracked or copied elsewhere.

The dashboard compares possibilities; it does not predict market returns or guarantee a safe retirement date. Salary taxes can use estimates or supplied tax brackets. Investment-withdrawal taxes are labeled estimates until account basis and other tax details are known. The included calculator does not file a tax return, choose which shares to sell, calculate required retirement-account distributions, or produce a probability of success. The assistant should explain when a more complete model is needed.

## License

MIT. You can share and adapt the skill, scripts, and template. External sources are linked rather than copied into the package.
