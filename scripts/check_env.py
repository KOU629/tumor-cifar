import sys

mods = [
    ("numpy", "numpy"),
    ("pandas", "pandas"),
    ("sklearn", "sklearn"),
    ("PIL", "PIL"),
    ("skimage", "skimage"),
    ("tqdm", "tqdm"),
    ("yaml", "yaml"),
    ("torch", "torch"),
    ("torchvision", "torchvision"),
]

missing = []
for name, imp in mods:
    try:
        __import__(imp)
        print(f"[OK] {name}")
    except Exception as e:
        missing.append((name, str(e)))
        print(f"[NG] {name}: {e}")

if missing:
    print("\nMissing modules:")
    for n, err in missing:
        print(f"- {n}: {err}")
    sys.exit(1)
else:
    import torch, torchvision
    print("\nEnvironment looks good.")
    print("Torch:", torch.__version__, "TorchVision:", torchvision.__version__)
