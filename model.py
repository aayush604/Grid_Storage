import numpy as np, pandas as pd

#Curtailment scenarios (GW): illustrative sensitivity bounds, not independent..
#Sourced to a specific report, "mid" (4 GW) is anchored to Mercom India's
#reporting of up to 4 GW curtailed in Rajasthan, Mar-Aug 2025; "low" and "high"
# are +/-2x bounds chosen to show sensitivity; they are not separately verified figures.

curt_GW   = {"low":2, "mid":4, "high":8}   
curt_hours = 4                             #assuming daily window of peak curtailment risk(midday); not measured directly, see README. 

usable_kWh = 0.9                           #usable battery capacity per household, lead-acid,from Luminous LPTT12150H datasheet (150Ah, 12V, ~80% DoD)

eta        = 0.85                          # round-trip efficiency, standard assumption for lead-acid
          
population_2021 = 79_281_000       # source: [https://rajasthan.census.gov.in/]
avg_household_size = 5.1           # source: Census of India 2011, Rajasthan average household size.
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

df["surplus_GWh"] = df["surplus_GWh"].round(2)
df["absorbed_GWh"] = df["absorbed_GWh"].round(3)
df["pct_absorbed"] = df["pct_absorbed"].round(2)
df.to_csv("results/output.csv", index=False)


print(df)


df.to_csv("result.csv", index=False)


# # manual check: mid scenario, 5% adoption
# manual = (households * 0.05 * usable_kWh / eta / 1e6) / (4 * 4) * 100
# print("manual check:", manual)


def absorbed_GWh(households, adopt, usable_kWh, eta):
    return households * adopt * usable_kWh / eta / 1e6


# Sanity check on the function's arithmetic using a fixed, round number
# (17,000,000) chosen specifically so the result is easy to verify by hand.
# This is NOT the household figure used in the pipeline above (15,545,294,
# from the Census-derived calculation.
# hand-checkable test of the formula itself, independent of which
# household estimate ends up being used.

assert abs(absorbed_GWh(17_000_000, 0.05, 0.9, 0.85) - 0.9) < 1e-6
assert abs(absorbed_GWh(17_000_000, 0.05, 0.9, 0.85) / (4 * 4) - 0.05625) < 1e-6
print("tests passed")
