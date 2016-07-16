library(ggplot2)
library(Cairo)

options(scipen=999)
unigrams<-unigrams[order(count, decreasing=T),]
df <- data.frame(Terms=1:nrow(unigrams), Coverage=cumsum(unigrams$count)/sum(unigrams$count))

coverage = ggplot(df, aes(x=Terms)) + 
geom_line(aes(y=100*Coverage)) + 
scale_x_log10(breaks=10^(0:6)) + scale_y_continuous(breaks=seq(0, 100, 10)) +
xlab("vocabulary size") + ylab("coverage")
#ggsave(file=paste0("data/results/plots/coverage/coverage.png"), plot=coverage, width=15, height=12, dpi=600, type='cairo-png')
