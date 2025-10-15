import os
import argparse
import random
import pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True, help='dataset root containing train/ and/or test/ with T0..T4/')
    ap.add_argument('--phase', required=True, choices=['train','test'], help='which phase to scan')
    ap.add_argument('--out', default=None, help='output csv path; default: <root>/<phase>.csv')
    args = ap.parse_args()

    tdir = os.path.join(args.root, args.phase, 'T4')
    if not os.path.isdir(tdir):
        raise FileNotFoundError(f'not found: {tdir}')

    imgs = sorted([f for f in os.listdir(tdir) if os.path.isfile(os.path.join(tdir,f))])

    rows = []
    for img in imgs:
        # Simple deterministic times 0..4 to satisfy loader expectation
        times = [0,1,2,3,4]
        gt = random.randint(0,1)
        rows.append({
            'img': img,
            'time': str(times),
            'gt': gt,
        })
    df = pd.DataFrame(rows)
    out = args.out or os.path.join(args.root, f'{args.phase}.csv')
    df.to_csv(out, index=False)
    print(f'wrote {out} with {len(df)} rows')

if __name__ == '__main__':
    main()
