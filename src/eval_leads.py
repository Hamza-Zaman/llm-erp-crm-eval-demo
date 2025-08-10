# Lead qualification triage evaluation.
# Intention: quick baseline. Replace qualify_lead() with your scoring model.

import pandas as pd
from src.common import qualify_lead

df = pd.read_csv('data/leads.csv')
df['pred'] = df.apply(lambda r: qualify_lead(r['industry'], int(r['employees']), r['notes']), axis=1)
acc = (df['pred'] == df['qualified_gt']).mean()
print(f"Lead triage accuracy: {acc:.2f} on {len(df)} leads")
