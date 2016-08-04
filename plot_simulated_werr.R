library(data.table)
library(ggplot2)

werr = fread('data/results/simulated_werr/simulated_werr')
colnames(werr) = c("corpus", "WERR")

plot = ggplot(werr, aes(x=corpus, y=WERR)) +
geom_bar(stat="identity") + 
coord_flip() +
scale_x_discrete(limits=werr$corpus[order(werr$WERR)]) +
labs(x="", y="WERR [%]") +
theme(text = element_text(size=25), axis.title.x = element_text(colour="dimgray", vjust=1)) +
theme(axis.title.x=element_text(margin=margin(20,0,0,0)))
ggsave(file=paste0("data/results/plots/simulated_werr/total.png"), plot=plot, width=15, height=10, dpi=100, type='cairo-png')
