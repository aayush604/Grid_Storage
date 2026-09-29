import numpy as np, pandas as pd

curt_GW   = {"low":2, "mid":4, "high":8}   # scenarios, cite your sources
curt_hours = 4                              # assumption, state it
usable_kWh = 0.9                            # lead-acid, from datasheet
eta        = 0.85
# households = 17_000_000                     # replace with sourced figure

population_2021 = 79_281_000        # source: [cite]
avg_household_size = 5.1            # source: Census 2011, [cite]
households = population_2021 / avg_household_size

rows = []
for s, gw in curt_GW.items():
    surplus_GWh = gw * curt_hours
    for adopt in (0.01, 0.05, 0.10):
        N = households * adopt
        absorbed_GWh = N * usable_kWh / eta / 1e6
        rows.append((s, adopt, surplus_GWh, absorbed_GWh,
                     100*absorbed_GWh/surplus_GWh))

df = pd.DataFrame(rows, columns=["scenario","adoption","surplus_GWh",
                                  "absorbed_GWh","pct_absorbed"])

print(df)

df.to_csv("result.csv", index=False)

# # manual check: mid scenario, 5% adoption
# manual = (households * 0.05 * usable_kWh / eta / 1e6) / (4 * 4) * 100
# print("manual check:", manual)

def absorbed_GWh(households, adopt, usable_kWh, eta):
    return households * adopt * usable_kWh / eta / 1e6

# sanity test with the hand-calculated case
assert abs(absorbed_GWh(17_000_000, 0.05, 0.9, 0.85) - 0.9) < 1e-6
assert abs(absorbed_GWh(17_000_000, 0.05, 0.9, 0.85) / (4 * 4) - 0.05625) < 1e-6
print("tests passed")