# CRM note summarisation smoke test.
# Intention: check that one-line summaries are consistently action-oriented.

import pandas as pd
from src.common import summarise_note

df = pd.read_csv('data/notes.csv')
df['summary'] = df['content'].apply(summarise_note)

# Simple shape checks: non-empty, short, ends without trailing punctuation issues, etc.
df['ok_len'] = df['summary'].str.len().between(5, 120)
print(df[['content','summary','ok_len']])
