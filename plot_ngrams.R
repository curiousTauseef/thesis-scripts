downsample <- function(ngrams, size=200000){
	ngrams<-ngrams[sample(nrow(ngrams), size=size, replace=F),]
	ngrams<-ngrams[order(count, decreasing=T),]
	return(ngrams)
}

#preprocess datasets
unigrams_head = head(filter(unigrams, !grepl('num|ust|<s>|</s>', token)), 30)
bigrams_head = head(filter(bigrams, !grepl('num|ust|<s>|</s>', token)), 50)
trigrams_head = head(filter(trigrams, !grepl('num|ust|<s>|</s>', token)), 50)
unigrams = downsample(unigrams)
bigrams = downsample(bigrams)
trigrams = downsample(trigrams)

#plot most common tokens
common_unigrams = qplot(unigrams_head$token, unigrams_head$count/sum(unigrams$count), geom="bar", stat="identity") +
coord_flip() +
scale_x_discrete(limits=unigrams_head$token[order(unigrams_head$count, decreasing=F)]) +
labs(x="unigram token", y="relative count", title=paste("Unigram distribution in the", corpus_name, "corpus"))

common_bigrams = qplot(bigrams_head$token, bigrams_head$count/sum(bigrams$count), geom="bar", position = "dodge", stat="identity") +
coord_flip() +
scale_x_discrete(limits=bigrams_head$token[order(bigrams_head$count, decreasing=F)]) +
labs(x="bigram token", y="relative count", title=paste("Bigram distribution in the", corpus_name, "corpus"))

common_trigrams = qplot(trigrams_head$token, trigrams_head$count/sum(trigrams$count), geom="bar", position = "dodge", stat="identity") +
coord_flip() +
scale_x_discrete(limits=trigrams_head$token[order(trigrams_head$count, decreasing=F)]) +
labs(x="trigram token", y="relative count", title=paste("Trigram distribution in the", corpus_name, "corpus"))

#plot ngram distributions
unigram_plot = qplot(log(unigrams$index), log(unigrams$count)) +
labs(x="log(n-gram index)", y="log(n-gram count)", title=paste("Double logarithmic plot of the unigram distribution for the", corpus_name, "corpus"))

bigram_plot = qplot(log(bigrams$index), log(bigrams$count)) +
labs(x="log(n-gram index)", y="log(n-gram count)", title=paste("Double logarithmic plot of the bigram distribution for the", corpus_name, "corpus"))

trigram_plot = qplot(log(trigrams$index), log(trigrams$count)) +
labs(x="log(n-gram index)", y="log(n-gram count)", title=paste("Double logarithmic plot of the trigram distribution for the", corpus_name, "corpus"))

#save files
ggsave(file=paste0("data/results/plots/unigram_distribution_", corpus_name, ".svg"), plot=unigram_plot, width=10, height=8)
ggsave(file=paste0("data/results/plots/bigram_distribution_", corpus_name, ".svg"), plot=bigram_plot, width=10, height=8)
ggsave(file=paste0("data/results/plots/trigram_distribution_", corpus_name, ".svg"), plot=trigram_plot, width=10, height=8)
ggsave(file=paste0("data/results/plots/common_unigrams_", corpus_name, ".svg"), plot=common_unigrams, width=10, height=8)
ggsave(file=paste0("data/results/plots/common_bigrams_", corpus_name, ".svg"), plot=common_bigrams, width=10, height=8)
ggsave(file=paste0("data/results/plots/common_trigrams_", corpus_name, ".svg"), plot=common_trigrams, width=10, height=8)
