# Graph Neural Network Lab of HUST.CS

2024-2025, Fall

## Source

Forked from [devign_lab](https://github.com/gystar/devign_lab)

## References

Devign: Effective Vulnerability Identification by Learning Comprehensive Program Semantics via Graph Neural Networks

## Choose Gather Layer & Classify Layer

Modify configs.json, setting `gather_layer_type` and `classify_layer_type`.

`gather_layer_type` should be one of the following:

- `ggrn`
- `gcn`
- `gat`

`classify_layer_type` should be one of the following:

- `readout`
- `conv`

The default setting is `gcn` and `readout`, which achieved the highest acc. in test.

## Run

```python
# After setting the config
python lab.py
```

## Evaluation

| Gather Layer | Classify Layer | Acc. | F1 |
| :--: | :--: | :--: | :--: |
| `ggrn` | `readout` | $55.69\%$ | $0.41$ |
| `ggrn` | `conv` | $52.33\%$ | $0.37$ |
| `gcn` | `readout` | $56.21\%$ | $0.54$ |
| `gcn` | `conv` | $49.48\%$ | $0.45$ |
| `gat` | `readout` | $51.55\%$ | $0.19$ |
| `gat` | `conv` | $50.52\%$ | $0.03$ |