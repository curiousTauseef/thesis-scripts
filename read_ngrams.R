library(data.table)
library(dplyr)

read_ngram_file <- function(filename){
	ngrams<-fread(filename, header=F, sep="\t")
	colnames(ngrams)<-c("token", "count")
	ngrams<-ngrams[order(count, decreasing=T),]
	ngrams$index<-seq(1:nrow(ngrams))
	return(ngrams)
}

read_ngrams <- function(path){
	unigrams<<-read_ngram_file(paste0(path, "_unigrams"))
	bigrams<<-read_ngram_file(paste0(path, "_bigrams"))
	trigrams<<-read_ngram_file(paste0(path, "_trigrams"))
}

corpus_name = "full_lemma"
path = paste0("data/results/ngrams/", corpus_name)
read_ngrams(path)
