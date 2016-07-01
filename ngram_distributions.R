library(data.table)
library(ggplot2)

read_ngram_file <- function(filename){
	ngrams<-fread(filename, header=F, sep="\t")
	colnames(ngrams)<-c("token", "count")
	ngrams<-ngrams[sample(nrow(ngrams), size=200000, replace=F),]
	ngrams<-ngrams[order(count, decreasing=T),]
	ngrams$index<-seq(1:nrow(ngrams))
	return(ngrams)
}

read_ngrams <- function(path){
	unigrams<<-read_ngram_file(paste0(path, "_unigrams"))
	bigrams<<-read_ngram_file(paste0(path, "_bigrams"))
	trigrams<<-read_ngram_file(paste0(path, "_trigrams"))
}

read_ngrams("data/results/ngrams/full_plain")

unigram_plot = qplot(log(unigrams$index), log(unigrams$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the unigram distribution for the full plain text corpus")
bigram_plot = qplot(log(bigrams$index), log(bigrams$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the bigram distribution for the full plain text corpus")
trigram_plot = qplot(log(trigrams$index), log(trigrams$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the trigram distribution for the full plain text corpus")

ggsave(file="data/results/plots/unigrams_full.svg", plot=unigram_plot, width=10, height=8)
ggsave(file="data/results/plots/bigrams_full.svg", plot=bigram_plot, width=10, height=8)
ggsave(file="data/results/plots/trigrams_full.svg", plot=trigram_plot, width=10, height=8)
