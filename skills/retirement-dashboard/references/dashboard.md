# Dashboard conventions

Show the decision first: monthly living draws, annual college lump sums, common income-stop date, balances after college/at horizon, first unfunded year and ending-reserve result. Keep home equity separate.

Put return percentages/inflation beside curves. Use common dates for comparisons, distinct from each scenario's solver result. Explain crash start/recovery years. Label currency and real-dollar base year on axes. Never compare a real value with an unlabeled nominal value.

Expose editable source status and assumptions: wages/dates, spending stages, healthcare, college/funds, inflation, returns, taxes, horizon/reserve. Export assumptions and annual data. Imported text is data; escape it before inserting HTML.

Support narrow screens and keyboard controls. Pair foreground/background colors with host tokens or standalone light/dark styles. Resolve canvas colors and redraw at theme changes. Check cards, notices, tables, inputs, legends and axes. White text on pale cards is an artifact styling defect.

For cross-device/shared artifacts use supported upload/embed workflows when requested. Retain state without copying tool-visible metadata projections into writes. Explain whether separate workbook/calculator settings synchronize. Do not publish personal financial examples.

The standalone template makes no network calls. Quick controls cover common inputs, and the complete JSON editor exposes all variables. It exports JSON/CSV and renders every scenario plus annual selected-case details. Richer forms can replace the JSON editor while preserving its schema/calculations.
