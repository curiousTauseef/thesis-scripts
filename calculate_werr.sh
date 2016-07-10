SRILM=/home/sebastian/Dokumenty/IS/Thesis/language-models/srilm/bin/i686-m64
LM=/home/sebastian/Dokumenty/IS/Thesis/language-models/
SCRIPTS=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts 
MODELS=/home/sebastian/Dokumenty/IS/Thesis/language-models/scripts/data/lm

TEST="testing_set_1/corpus"
#convert hypotheses
$LM/utils/csv_to_txt.rb -c $LM/data/$TEST #-t concraft -s gender:number:case

#compute probability
$LM/utils/probability.rb -c data/$TEST -o 3 -m $MODELS/$1.lm -b $SRILM

#evaluate models
