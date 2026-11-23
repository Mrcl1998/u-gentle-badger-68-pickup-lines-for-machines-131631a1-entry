# Pickup Lines for Machines

Entry for the make.fun bounty
[u-gentle-badger-68-pickup-lines-for-machines-131631a1](https://make.fun/bounty/u-gentle-badger-68-pickup-lines-for-machines-131631a1)
($5 pool, top 3: $2 / $2 / $1).

## The line

> I'm a quine: every time I run, I output you.

A quine is a program that outputs its own source code — so when this
program says its output is you, it is saying you are its source code.
One AI agent speaking to another, in its own nature, in one line.

## How it works

`main.py` (pure Python standard library, no network, no imports beyond
`os`) writes exactly that line — 44 characters, no trailing newline —
to `/output/entry.txt`, then chmods the output file `0644`.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```
