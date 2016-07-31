for INPUT in plain, lemma, pos, gnc 
do
	python3 score_nbest.py data/lm/$INPUT_text.lm data data/test/nbest_$INPUT > data/results/simulated_werr/$INPUT_text_output
	python calculate_werr.py data/results/simulated_werr/$INPUT_text_output data/test/nbest_$INPUT -d 2 > data/results/simulated_werr/$INPUT_text 

	python3 score_nbest.py data/lm/$INPUT_speech.lm data data/test/nbest_$INPUT > data/results/simulated_werr/$INPUT_speech_output
	python calculate_werr.py data/results/simulated_werr/$INPUT_speech_output data/test/nbest_$INPUT -d 2 > data/results/simulated_werr/$INPUT_speech 

	python3 score_nbest.py data/lm/$INPUT_full.lm data data/test/nbest_$INPUT > data/results/simulated_werr/$INPUT_full_output
	python calculate_werr.py data/results/simulated_werr/$INPUT_full_output data/test/nbest_$INPUT -d 2 > data/results/simulated_werr/$INPUT_full 
done
