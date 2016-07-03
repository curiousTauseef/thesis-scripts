SRILM=/home/sebastian/Dokumenty/IS/Thesis/language-models/srilm/bin/i686-m64
SCRIPTS=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts 
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data

#train model with good-turing discounting (katz smoothing)
$SRILM/ngram-count \
-order 3 \
-text "$DATA/full/$1" \
-write1 "$DATA/results/ngrams/$1_unigrams" \
-write2 "$DATA/results/ngrams/$1_bigrams" \
-write3 "$DATA/results/ngrams/$1_trigrams" \
-unk \
-lm "$DATA/lm/$1.lm" \
#-no-sos -no-eos

#train model with modified kneser-ney smoothing
#$SRILM/ngram-count\
#-order 3\
#-text "$DATA/full/$1"\
#-lm "$DATA/lm/$1_kn.lm"\
#-kndiscount1 -kndiscount2 -kndiscount3 \
#-unk\
#
##train model with modified kneser-ney smoothing and interpolation
#$SRILM/ngram-count
#-order 3\
#-text "$DATA/full/$1"\
#-lm "$DATA/lm/$1_kni.lm"\
#-kndiscount1 -kndiscount2 -kndiscount3\
#-interpolate1 -interpolate2 -interpolate3\
#-unk\
#
##train model with unmodified kneser-ney smoothing
#$SRILM/ngram-count\
#-order 3\
#-text "$DATA/full/$1"\
#-lm "$DATA/lm/$1_ukn.lm"\
#-ukndiscount1 -ukndiscount2 -ukndiscount3\
#-unk\
#
##train model with unmodified kneser-ney smoothing and interpolation
#$SRILM/ngram-count\
#-order 3\
#-text "$DATA/full/$1"\
#-lm "$DATA/lm/$1_ukni.lm"\
#-ukndiscount1 -ukndiscount2 -ukndiscount3\
#-interpolate1 -interpolate2 -interpolate3\
#-unk\

##evaluate models
#echo "$1_gt.lm"
#$SRILM/ngram -ppl $DATA/test/full_plain -order 3 -lm "$DATA/lm/$1_gt.lm" -unk -debug 0
#echo "$1_kn.lm"
#$SRILM/ngram -ppl $DATA/test/full_plain -order 3 -lm "$DATA/lm/$1_kn.lm" -unk -debug 0
#echo "$1_kni.lm"
#$SRILM/ngram -ppl $DATA/test/full_plain -order 3 -lm "$DATA/lm/$1_kni.lm" -unk -debug 0
#echo "$1_ukn.lm"
#$SRILM/ngram -ppl $DATA/test/full_plain -order 3 -lm "$DATA/lm/$1_ukn.lm" -unk -debug 0
#echo "$1_ukni.lm"
#$SRILM/ngram -ppl $DATA/test/full_plain -order 3 -lm "$DATA/lm/$1_ukni.lm" -unk -debug 0
