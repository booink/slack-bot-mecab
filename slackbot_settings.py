import os

API_TOKEN = os.environ["API_TOKEN"]

DEFAULT_REPLY = '''```!mecab -h
MeCab: Yet Another Part-of-Speech and Morphological Analyzer

Copyright(C) 2001-2012 Taku Kudo
Copyright(C) 2004-2008 Nippon Telegraph and Telephone Corporation

Usage: mecab [options] files
 -r, --rcfile=FILE              use FILE as resource file
 -d, --dicdir=DIR               set DIR  as a system dicdir
 -u, --userdic=FILE             use FILE as a user dictionary
 -l, --lattice-level=INT        lattice information level (DEPRECATED)
 -D, --dictionary-info          show dictionary information and exit
 -O, --output-format-type=TYPE  set output format type (wakati,none,...)
 -a, --all-morphs               output all morphs(default false)
 -N, --nbest=INT                output N best results (default 1)
 -p, --partial                  partial parsing mode (default false)
 -m, --marginal                 output marginal probability (default false)
 -M, --max-grouping-size=INT    maximum grouping size for unknown words (default 24)
 -F, --node-format=STR          use STR as the user-defined node format
 -U, --unk-format=STR           use STR as the user-defined unknown node format
 -B, --bos-format=STR           use STR as the user-defined beginning-of-sentence format
 -E, --eos-format=STR           use STR as the user-defined end-of-sentence format
 -S, --eon-format=STR           use STR as the user-defined end-of-NBest format
 -x, --unk-feature=STR          use STR as the feature for unknown word
 -b, --input-buffer-size=INT    set input buffer size (default 8192)
 -P, --dump-config              dump MeCab parameters
 -C, --allocate-sentence        allocate new memory for input sentence
 -t, --theta=FLOAT              set temparature parameter theta (default 0.75)
 -c, --cost-factor=INT          set cost factor (default 700)
 -o, --output=FILE              set the output file name
 -v, --version                  show the version and exit.
 -h, --help                     show this help and exit.

```'''

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
