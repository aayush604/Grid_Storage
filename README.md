# Grid_Storage

# Rajasthan Solar Curtailment: Can Home Batteries Absorb the Midday Surplus?

A small model estimating how much of Rajasthan's midday solar curtailment
could be absorbed if home inverter batteries charged during peak sun hours.
Built for my IRENA Youth Forum 2027 application.

## The question

Developers reported to India's Central Electricity Authority that nearly
4 GW of commissioned solar capacity was being curtailed at peak hours in
early 2026 — not for lack of sun, but because the grid can't carry the
power out. Millions of homes in Rajasthan already have inverter batteries
for power cuts, sitting mostly idle at midday. This model asks: how much
of that surplus could they absorb, under a range of realistic assumptions?

**Short answer: not much, but not nothing.** Under a moderate scenario,
about 5% of a typical curtailed day's surplus. Home batteries don't solve
the transmission bottleneck — utility-scale storage has to do that — but
they're an underused, already-installed resource worth counting.

## Data and assumptions

| Input | Value | Source |
|---|---|---|
| Curtailed capacity (mid) | 4 GW | Developers to CEA, reported [Mercom India, Jan 2026] |
| Curtailed capacity (low/high) | 2 GW / 8 GW | Sensitivity bounds, not independently sourced |
| Curtailed hours/day | 4 hours | Assumption, based on typical peak-solar window |
| Usable battery capacity | 0.9 kWh | Luminous Solar LPTT12150H, 150Ah/12V, ~50% depth of discharge |
| Round-trip efficiency | 85% | Luminous Solar LPTT12150H spec sheet states >80% Wh efficiency; 85% used as a mid-range estimate |
| Households (Rajasthan) | ~15.5 million | Derived: population 79.28M (2021) ÷ avg. household size 5.1 (Census 2011) |
| Adoption rates tested | 1%, 5%, 10% | Scenario range, not a forecast |

All sourced figures link to their original page below. Everything else is
a stated assumption, not a finding — see "Limitations."

## How to run it

```bash
pip install -r requirements.txt
python model.py
```

Outputs `results/output.csv` and prints a summary table.

## Results

Full sensitivity table: [`results/output.csv`](results/output.csv)

| Scenario | Adoption | Surplus (GWh/day) | Absorbed (GWh/day) | % Absorbed |
|---|---|---|---|---|
| Mid | 5% | 16 | 0.82 | 5.1% |

*(Full 9-row table in the CSV — low/mid/high × 1%/5%/10%.)*

## What this means

Under the mid scenario at 5% adoption, home batteries absorb roughly 5%
of a curtailed day's surplus. That's meaningful at the margins — it's
storage that already exists, in homes, unused at exactly the hours it's
needed. It is not a fix for the underlying problem: curtailment is driven
by transmission constraints out of western Rajasthan's solar parks, which
home batteries in cities like Jaipur don't touch. Closing that gap needs
utility-scale storage and grid buildout, not distributed batteries alone.

## Limitations

- Curtailment scenarios beyond the sourced 4 GW figure are illustrative
  bounds, not independently reported numbers.
- Curtailed-hours and battery-spec values are assumptions, stated above,
  not measured.
- The model doesn't account for battery degradation, seasonal variation
  in solar output, or the cost/logistics of aggregating home batteries.
- Household count is derived, not from a single official source — shown
  as a calculation so it can be checked.

## Sources

- Mercom India / developers-to-CEA reporting, Jan 2026 — [link](https://cea.nic.in/wp-content/uploads/rpm_division/2026/04/Quarterly_Report_on_Under_Construction_Renewable_Energy_Projects_as_on_March_2026.pdf)
- Census 2011, household size — [link](https://censusindia.gov.in/nada/index.php/catalog/7117)
- Population 2021 estimate — [link](https://www.researchgate.net/figure/Population-Projections-India-and-Rajasthan-2016-2021-2026_fig1_324839782)
- Battery specifications — [Luminous Solar LPTT12150H product page](https://flipkart.com/luminous-solar-lptt12150h-150ah-tall-tubular-battery-60-months-warranty-inverter/p/itmc3ceda246bd9c)
## License

MIT — see LICENSE.

## Author

Ayush Soni, B.Tech in Data Science, PIET, Jaipur.
