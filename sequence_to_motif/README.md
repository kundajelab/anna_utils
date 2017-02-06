The files and pathways referenced by the shell scripts in this repository are found on nandi in:
`/srv/scratch/annashch/hocomoco_scan`

For now I have used the 640 human motifs for HOCOMOCO v10 & 1kb tiles (genome-wide) across hg19.
  There are 4 directories of matrices (on nandi):
 * `/srv/scratch/annashch/hocomoco_scan/hocomocov10_hg19_1kb_S_by_M_1_0.001`   -- This takes the top 1 hit per motif in a given sequence, and draws a binary threshold with a motif score corresponding to a p-value of 0.001
 * `/srv/scratch/annashch/hocomoco_scan/hocomocov10_hg19_1kb_S_by_M_1_0.0001`   -- This takes the top 1 hit per motif in a given sequence, and draws a binary threshold with a motif score corresponding to a p-value of 0.0001
 * `/srv/scratch/annashch/hocomoco_scan/hocomocov10_hg19_1kb_S_by_M_3_0.001`   -- This takes the top 3 hits per motif in a given sequence, and draws a binary threshold with a motif score corresponding to a p-value of 0.001
 * `/srv/scratch/annashch/hocomoco_scan/hocomocov10_hg19_1kb_S_by_M_3_0.0001`   -- This takes the top 3 hit per motif in a given sequence, and draws a binary threshold with a motif score corresponding to a p-value of 0.0001


Inside each of these folders, you will see three types of files for each chromosome. For example, for chromosome 1, we have:
* `chr1.mat.npy ` this is a numpy array of SxM (or Sx3M if you are looking at the folders where we consider the top 3 hits per motif). A "1" means that the motif hit is signficant for the given 1kb region of the genome. for the Sx3M case "1,1,1" means that there are 3 significant motif hits for the sequence, "1,1,0" means that there are 2 significant hits, and so on.
* `chr1.pos.npy` This is an Sx2 matrix that specifies the start (inclusive) and end (non-inclusive) of each 1kb region
* `chr1.tf.npy` This is the SxTF (or Sx3TF) matrix obtained by taking the max across all motifs that correspond to a particular TF. This isn't much of a reduction for the HOCOMOCO case -- there are 640 motifs corresponding to 600 TF's. 