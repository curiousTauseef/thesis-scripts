library(data.table)
library(ggplot2)

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

downsample <- function(ngrams, size=200000){
	ngrams<-ngrams[sample(nrow(ngrams), size=size, replace=F),]
	ngrams<-ngrams[order(count, decreasing=T),]
	return(ngrams)
}

read_ngrams("data/results/ngrams/full_plain")

unigrams_head = head(unigrams, 20)
bigrams_head = head(bigrams, 20)
trigrams_head = head(trigrams, 20)

#plot most common tokens
qplot(unigrams_head$token, unigrams_head$occurrence/sum(unigrams$count)) + geom_bar(position = "dodge", stat="identity")+coord_flip() + scale_x_discrete(limits=unigrams_head$token[order(unigrams_head$count, decreasing=F)])+labs(x="Unigram token", y="Relative occurrence", title="Unigram distribution")

unigrams_small = downsample(unigrams)
bigrams_small = downsample(bigrams)
trigrams_small = downsample(trigrams)

unigram_plot = qplot(log(unigrams_small$index), log(unigrams_small$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the unigram distribution for the full plain text corpus")
bigram_plot = qplot(log(bigrams_small$index), log(bigrams_small$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the bigram distribution for the full plain text corpus")
trigram_plot = qplot(log(trigrams_small$index), log(trigrams_small$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the trigram distribution for the full plain text corpus")

save files
#ggsave(file="data/results/plots/unigrams_full.svg", plot=unigram_plot, width=10, height=8)
#ggsave(file="data/results/plots/bigrams_full.svg", plot=bigram_plot, width=10, height=8)
#ggsave(file="data/results/plots/trigrams_full.svg", plot=trigram_plot, width=10, height=8)
