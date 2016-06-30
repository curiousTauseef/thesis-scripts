library(data.table)
library(ggplot2)
unigrams<-fread("data/results/ngrams/full_plain_unigrams", header=F, sep="\t")
unigrams<-unigrams[order(count, decreasing=T),]
colnames(unigrams)<-c("token", "count")
unigrams$index<-seq(1:nrow(unigrams))

qplot(log(unigrams$index), log(unigrams$count))+labs(x="log(n-gram index)", y="log(n-gram count)", title="Double logarithmic plot of the unigram occurrence distribution")
