library(data.table)
library(Cairo)
library(ggplot2)

corpus_name="speech_plain"

data = fread(paste0("data/results/werr/", corpus_name, ".werr"))
colnames(data) = c("alpha", "WERR")

werr = ggplot(data, aes(x=alpha, y=WERR, geom="line")) +
labs(x="alpha", y="WERR") +
theme(axis.title.y=element_text(margin=margin(0, 0, 0, 0))) +
theme(axis.title.x=element_text(margin=margin(0, 0, 0, 0)))

ggsave(file=paste0("data/results/plots/werr/", corpus_name, "_werr.png"), plot=werr, width=15, height=12, dpi=600, type='cairo-png')
