library(data.table)
library(ggplot2)

myfunction <- function(filename){
	ngrams<-fread(filename, header=F, sep="\t")
	colnames(ngrams)<-c("token", "count")
	ngrams<-ngrams[order(count, decreasing=T),]
	ngrams$index<-seq(1:nrow(ngrams))
	return(ngrams)
}
unigrams_plot = qplot(log(unigrams$index), log(unigrams$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the unigram distribution for the full plain text corpus")
ggsave(file="data/results/plots/unigrams_full.svg", plot=unigrams_plot, width=10, height=8)
