args <- commandArgs(trailingOnly = TRUE)
data <- read.table(args[1], header = TRUE, sep=";")
plot(data, main="rpkm graph",xlab= "scaffold", ylab = "name")
rpkm_log2 <- log2(data$V2)
data_log <- data.frame(Transcript = data$Transcript,rpkm_log2)



par(mar = c(7, 4, 1, 1) + 0.4)
plot(data_log$Transcript, data_log$rpkm_log2 , main="Reads Per Kilobase per Million mapped reads", las = 2, ylab = "log2_rpkm")
abline(a = mean(data_log$rpkm_log2), b=0, col="red")
legend("topright", "Mean log2 rpkm", col = "red", merge = TRUE, cex = 0.75, lty = 1:2, xjust = 1, yjust = 1)

