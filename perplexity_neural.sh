RNNLM=/home/sebastian/Dokumenty/IS/Thesis/language-models/rnnlm/simple-examples/rnnlm-0.2b
DATA=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data

for TYPE in plain lemma pos gnc
do
	${RNNLM}/rnnlm -rnnlm ${DATA}/lm/${TYPE}.rnnlm -test ${DATA}/test/test_${TYPE} -debug 1 > ${DATA}/results/ppl/neural/${TYPE}
done
