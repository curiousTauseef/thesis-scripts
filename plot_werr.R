library(data.table)
library(ggplot2)

corpus_name="speech_plain"

data = fread(paste0("data/results/werr/", corpus_name, ".werr"))
colnames(data) = c("alpha", "WERR")
plot = qplot(data$alpha, data$WERR, geom="line")

ggsave(file=paste0("data/results/plots/werr/", corpus_name, "_werr.svg"), plot=plot, width=10, height=8)

