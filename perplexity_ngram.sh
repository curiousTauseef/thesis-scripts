#!/usr/bin/zsh
SRILM=/home/sebastian/Dokumenty/IS/Thesis/language-models/srilm/bin/i686-m64
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data

for TYPE in lemma pos gnc
do
	for ORDER in 1 2 3
	do
		$SRILM/ngram -ppl "$DATA/test/test_${TYPE}" -order $ORDER -lm "$DATA/lm/${TYPE}_text.lm" -unk -debug 0 >> "$DATA/results/ppl/${TYPE}_text"
		$SRILM/ngram -ppl "$DATA/test/test_${TYPE}" -order $ORDER -lm "$DATA/lm/${TYPE}_speech.lm" -unk -debug 0 >> "$DATA/results/ppl/${TYPE}_speech"
		$SRILM/ngram -ppl "$DATA/test/test_${TYPE}" -order $ORDER -lm "$DATA/lm/${TYPE}_full.lm" -unk -debug 0 >> "$DATA/results/ppl/${TYPE}_full"
	done
done
