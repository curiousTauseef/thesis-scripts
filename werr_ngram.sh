for TYPE in plain lemma pos gnc
do
	python3 score_nbest.py "data/lm/${TYPE}_text.lm" "data/results/simulated_werr/${TYPE}_text_output" "data/test/nbest_${TYPE}" 
	python3 calculate_werr.py "data/results/simulated_werr/${TYPE}_text_output" "data/test/nbest_${TYPE}" -d 2 > "data/results/simulated_werr/${TYPE}_text" 

	python3 score_nbest.py "data/lm/${TYPE}_speech.lm" "data/results/simulated_werr/${TYPE}_speech_output" "data/test/nbest_${TYPE}" 
	python3 calculate_werr.py "data/results/simulated_werr/${TYPE}_speech_output" "data/test/nbest_${TYPE}" -d 2 > "data/results/simulated_werr/${TYPE}_speech" 

	python3 score_nbest.py "data/lm/${TYPE}_full.lm" "data/results/simulated_werr/${TYPE}_full_output" "data/test/nbest_${TYPE}" 
	python3 calculate_werr.py "data/results/simulated_werr/${TYPE}_full_output" "data/test/nbest_${TYPE}" -d 2 > "data/results/simulated_werr/${TYPE}_full" 
done
