library(ggplot2)
library(Cairo)
library(grid)

downsample <- function(ngrams, size=200000, treshold=1000){
	head<-head(ngrams, treshold)
	tail<-ngrams[sample(treshold:nrow(ngrams), size=size, replace=F),]
	ngrams<-rbind(head, tail)
	ngrams<-ngrams[order(count, decreasing=T),]
	return(ngrams)
}

#preprocess datasets
unigrams_head = head(filter(unigrams, !grepl('num|ust|<s>|</s>', token)), 30)
bigrams_head = head(filter(bigrams, !grepl('num|ust|<s>|</s>', token)), 30)
trigrams_head = head(filter(trigrams, !grepl('num|ust|<s>|</s>', token)), 30)
#unigrams_downsampled = downsample(unigrams)
#bigrams_downsampled = downsample(bigrams)
#trigrams_downsampled = downsample(trigrams)

#plot most common tokens
#common_unigrams = ggplot(unigrams_head, aes(x=token, y=count/sum(count))) +
#geom_bar(stat="identity") + 
#coord_flip() +
#scale_x_discrete(limits=unigrams_head$token[order(unigrams_head$count, decreasing=F)]) +
#labs(x="", y="relative count") +
#theme(text = element_text(size=25), axis.title.x = element_text(colour="dimgray", vjust=1)) +
#theme(axis.title.x=element_text(margin=margin(20,0,0,0)))
#
#
#common_bigrams = ggplot(bigrams_head, aes(x=token, y=count/sum(count))) +
#geom_bar(stat="identity") + 
#coord_flip() +
#scale_x_discrete(limits=bigrams_head$token[order(bigrams_head$count, decreasing=F)]) +
#labs(x="", y="relative count") +
#theme(text = element_text(size=25), axis.title.x = element_text(colour="dimgray", vjust=1)) +
#theme(axis.title.x=element_text(margin=margin(20,0,0,0)))
#
#common_trigrams = ggplot(trigrams_head, aes(x=token, y=count/sum(count))) +
#geom_bar(stat="identity") + 
#coord_flip() +
#scale_x_discrete(limits=trigrams_head$token[order(trigrams_head$count, decreasing=F)]) +
#labs(x="", y="relative count") +
#theme(text = element_text(size=25), axis.title.x = element_text(colour="dimgray", vjust=1)) +
#theme(axis.title.x=element_text(margin=margin(20,0,0,0)))

unigram_plot = ggplot(unigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.5) +
labs(x="log(n-gram index)", y="log(n-gram count)") +
theme(text = element_text(size=25))

bigram_plot = ggplot(bigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.5) +
labs(x="log(n-gram index)", y="log(n-gram count)")
theme(text = element_text(size=25))

trigram_plot = ggplot(trigrams_downsampled, aes(x=log(index), y=log(count))) +
geom_point(size=0.5) +
labs(x="log(n-gram index)", y="log(n-gram count)")
theme(text = element_text(size=25))

#save files
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_unigrams.png"), plot=unigram_plot, width=15, height=10, dpi=600, type='cairo-png')
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_bigrams.png"), plot=bigram_plot, width=15, height=10, dpi=600, type='cairo-png')
ggsave(file=paste0("data/results/plots/distributions/", corpus_name, "_trigrams.png"), plot=trigram_plot, width=15, height=10, dpi=600, type='cairo-png')
#ggsave(file=paste0("data/results/plots/common/", corpus_name, "_unigrams.png"), plot=common_unigrams, width=15, height=12, dpi=600, type='cairo-png')
#ggsave(file=paste0("data/results/plots/common/", corpus_name, "_bigrams.png"), plot=common_bigrams, width=15, height=12, dpi=600, type='cairo-png')
#ggsave(file=paste0("data/results/plots/common/", corpus_name, "_trigrams.png"), plot=common_trigrams, width=15, height=12, dpi=600, type='cairo-png')
