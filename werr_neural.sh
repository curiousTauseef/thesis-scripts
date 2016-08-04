RNNLM=/home/sebastian/Dokumenty/IS/Thesis/language-models/rnnlm/simple-examples/rnnlm-0.2b
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data

for TYPE in plain lemma pos gnc
do
	#$RNNLM/rnnlm -rnnlm "$DATA/lm/${TYPE}.rnnlm" -test "$DATA/test/nbest_${TYPE}" -nbest -debug 1 > "$DATA/results/simulated_werr/neural/${TYPE}_output"
	python3 calculate_werr.py "data/results/simulated_werr/neural/${TYPE}_output" "data/test/nbest_${TYPE}" -d 2 > "data/results/simulated_werr/neural/${TYPE}"
done
