SRILM=/home/sebastian/Dokumenty/IS/Thesis/language-models/srilm/bin/i686-m64
SCRIPTS=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts 
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data
LM=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data/lm

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1_gt.lm" \
-gt3min 0 \
-unk

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1_kn.lm" \
-gt3min 0 \
-unk \
-ukndiscount1 -ukndiscount2 -ukndiscount3

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1_kni.lm" \
-gt3min 0 \
-unk \
-ukndiscount1 -ukndiscount2 -ukndiscount3 \
-interpolate1 -interpolate2 -interpolate3

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1_cg.lm" \
-gt3min 0 \
-unk \
-kndiscount1 -kndiscount2 -kndiscount3 \

$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-lm "$DATA/lm/$1.lm" \
-gt3min 0 \
-unk \
-kndiscount1 -kndiscount2 -kndiscount3 \
-interpolate1 -interpolate2 -interpolate3
#-write1 "$DATA/results/ngrams/$1_unigrams" \
#-write2 "$DATA/results/ngrams/$1_bigrams" \
#-write3 "$DATA/results/ngrams/$1_trigrams" \

echo "Good-Turing"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1_gt.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1_gt.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1_gt.lm" -unk -debug 0
echo "Kneser-Ney"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1_kn.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1_kn.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1_kn.lm" -unk -debug 0
echo "Kneser-Ney Interpolated"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1_kni.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1_kni.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1_kni.lm" -unk -debug 0
echo "Chen-Goodman"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1_cg.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1_cg.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1_cg.lm" -unk -debug 0
echo "Chen-Goodman Interpolated"
$SRILM/ngram -ppl $DATA/test/test -order 1 -lm "$DATA/lm/$1_cgi.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 2 -lm "$DATA/lm/$1_cgi.lm" -unk -debug 0
$SRILM/ngram -ppl $DATA/test/test -order 3 -lm "$DATA/lm/$1_cgi.lm" -unk -debug 0
