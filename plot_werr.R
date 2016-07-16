library(data.table)
library(Cairo)
library(ggplot2)

corpus_name="pos"

text = fread(paste0("data/results/werr/", corpus_name, "_text.werr"))
name = rep("text", nrow(text))
text = data.frame(text, name)
colnames(text) = c("alpha", "WERR", "name")

speech = fread(paste0("data/results/werr/", corpus_name, "_speech.werr"))
name = rep("speech", nrow(speech))
speech = data.frame(speech, name)
colnames(speech) = c("alpha", "WERR", "name")

full = fread(paste0("data/results/werr/", corpus_name, "_full.werr"))
name = rep("full", nrow(full))
full = data.frame(full, name)
colnames(full) = c("alpha", "WERR", "name")

data = rbind(text, speech, full)
werr = ggplot(data, aes(x=alpha, y=WERR, colour=name)) +
geom_line() +
#geom_line(data=text, color="#CC6666") +
#geom_line(data=speech, color="#9999CC") +
#geom_line(data=full) +
labs(x="alpha", y="werr") +
theme(axis.title.y=element_text(margin=margin(0, 0, 0, 0))) +
theme(axis.title.x=element_text(margin=margin(0, 0, 0, 0)))

ggsave(file=paste0("data/results/plots/werr/", corpus_name, "_werr.png"), plot=werr, width=15, height=12, dpi=600, type='cairo-png')
