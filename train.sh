SRILM=/home/sebastian/Dokumenty/IS/Thesis/language-models/srilm/bin/i686-m64
SCRIPTS=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts 
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data
LM=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data/lm

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1.lm" \
-kndiscount1 -kndiscount2 -kndiscount3 \
-interpolate1 -interpolate2 -interpolate3 \
-write1 "$DATA/results/ngrams/$1_unigrams" \
-write2 "$DATA/results/ngrams/$1_bigrams" \
-write3 "$DATA/results/ngrams/$1_trigrams" \
-unk

echo "$1:"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1.lm" -unk -debug 0
