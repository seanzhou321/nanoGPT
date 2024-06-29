# evaluate the base gpt2
# n_layer=12, n_head=12, n_embd=768
# 124M parameters
batch_size = 64
block_size = 256
eval_iters = 500 # use more iterations to get good estimate
out_dir='out-shakespeare-char'
dataset = 'shakespeare_char'
compile=False