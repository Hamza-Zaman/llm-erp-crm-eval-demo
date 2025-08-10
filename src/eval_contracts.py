# Contract clause extraction evaluation.
# Intention: show an offline scoring harness. Swap in a model inside extract_contract_fields().

import pandas as pd
from src.common import extract_contract_fields
from src.metrics import prf1

df = pd.read_csv('data/contracts.csv')

# Score payment terms only for brevity. Extend to warranty/termination similarly.
tp=fp=fn=0
for _, row in df.iterrows():
    pred = extract_contract_fields(row['text'])
    gt = str(row['payment_terms']).lower()
    pv = (pred['payment_terms'] or '').lower()
    if pv == gt:
        tp += 1
    else:
        fn += 1

p,r,f1 = prf1(tp,0,fn)
print(f"Payment terms extraction — P={p:.2f} R={r:.2f} F1={f1:.2f} on {len(df)} docs")
