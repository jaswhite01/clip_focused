import os
import pandas as pd

DATA_DIR = '/data/physionet.org/files/mimic-iii-clinical-action/1.0.0'
OUT_DIR = '/data/splits'
os.makedirs(OUT_DIR, exist_ok=True)

sents = pd.read_csv(os.path.join(DATA_DIR, 'sentence_level.csv'))
for split in ['train', 'val', 'test']:
    ids = pd.read_csv(os.path.join(DATA_DIR, f'{split}_ids.csv'), header=None)[0].astype(str).str.strip()
    ids = set(ids) - {'doc_id', 'id', 'document_id'}
    df = sents[sents['doc_id'].astype(str).isin(ids)].sort_values(['doc_id', 'sent_index'])
    df.to_csv(os.path.join(OUT_DIR, f'{split}.csv'), index=False)
    print(split, df['doc_id'].nunique(), 'notes', len(df), 'sentences')
