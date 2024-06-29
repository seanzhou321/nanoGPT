# Notes from Sean Zhoou

To play on a RTX 3060
## Load shakespeare_char
```commandline
cd data\shakespeare_char
ython prepare.py 
```
You should see input.txt, meta.pkl, train.bin, val.bin files are created in the directory.
## Train the model by shakespeare_char
```commandline
python train.py config\train_shakespeare_char.py
```
You should see out-shakespeare-char\ckpt.pt is created.
### Evaluate the model
```commandline
python train.py config\eval_nano.py
```
## Generate some sample text by the model
```commandline
python sample.py --out_dir=out-shakespeare-char
```

## NOTES
1. wandb_project='owt' # weight and biases project is open web text