library(ggplot2)
library(grid)

downsample <- function(ngrams, size=200000){
	ngrams<-ngrams[sample(nrow(ngrams), size=size, replace=F),]
	ngrams<-ngrams[order(count, decreasing=T),]
	return(ngrams)
}

#preprocess datasets
unigrams_head = head(filter(unigrams, !grepl('num|ust|<s>|</s>', token)), 35)
bigrams_head = head(filter(bigrams, !grepl('num|ust|<s>|</s>', token)), 35)
trigrams_head = head(filter(trigrams, !grepl('num|ust|<s>|</s>', token)), 35)
unigrams = downsample(unigrams)
bigrams = downsample(bigrams)
trigrams = downsample(trigrams)

##plot most common tokens
#common_unigrams = qplot(unigrams_head$token, unigrams_head$count/sum(unigrams$count), geom="bar") +
#coord_flip() +
#scale_x_discrete(limits=unigrams_head$token[order(unigrams_head$count, decreasing=F)]) +
#labs(y="relative count")
##theme(axis.title.y=element_text(margin=margin(20,20,20,20))) +
##theme(axis.title.x=element_text(margin=margin(20,20,20,20)))
#
#common_bigrams = qplot(bigrams_head$token, bigrams_head$count/sum(bigrams$count), geom="bar") +
#coord_flip() +
#scale_x_discrete(limits=bigrams_head$token[order(bigrams_head$count, decreasing=F)]) +
#labs(y="relative count")
##theme(axis.title.y=element_text(margin=margin(0,20,0,0))) +
##theme(axis.title.x=element_text(margin=margin(0,20,0,0)))
#
#common_trigrams = qplot(trigrams_head$token, trigrams_head$count/sum(trigrams$count), geom="bar") +
#coord_flip() +
#scale_x_discrete(limits=trigrams_head$token[order(trigrams_head$count, decreasing=F)]) +
#labs(y="relative count")
##theme(axis.title.y=element_text(margin=margin(0,20,0,0))) +
##theme(axis.title.x=element_text(margin=margin(0,20,0,0)))

unigram_plot = ggplot(unigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.3) +
labs(x="log(n-gram index)", y="log(n-gram count)")

bigram_plot = ggplot(bigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.3) +
labs(x="log(n-gram index)", y="log(n-gram count)")

trigram_plot = ggplot(trigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.3) +
labs(x="log(n-gram index)", y="log(n-gram count)")

#save files
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_unigrams.svg"), plot=unigram_plot, width=10, height=8)
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_bigrams.svg"), plot=bigram_plot, width=10, height=8)
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_trigrams.svg"), plot=trigram_plot, width=10, height=8)
#ggsave(file=paste0("data/results/plots/common/", corpus_name, ".svg"), plot=common_unigrams, width=10, height=8)
#ggsave(file=paste0("data/results/plots/common/", corpus_name, ".svg"), plot=common_bigrams, width=10, height=8)
#ggsave(file=paste0("data/results/plots/common/", corpus_name, ".svg"), plot=common_trigrams, width=10, height=8)
