export base=/srv/scratch/annashch/dmso/ctcf_check
#ALL CTCF variations 
#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atac_earlyG1_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix earlyG1.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt  --totext  --thresholds dmso_ctcf.score_cutoffs.tsv
#echo "done with earlyG1 down" 

#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed  $base/atac_earlyG1_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix earlyG1.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv 
#echo "done with earlyG1 up" 

#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atac_lateG1_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix lateG1.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv 
#echo "done with lateG1 down" 

#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atac_lateG1_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix lateG1.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv 
#echo "done with lateG1 up" 

#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atac_sg2m_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix SG2M.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv 
#echo "done with SG2M down"

#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atac_sg2m_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix SG2M.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv 
#echo "done with SG2M up"


#original set of full peaks!
#python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF.txt --positions_bed $base/atacseq_merged.peaks.padded.bed --reference hg19/hg19.genome.fa --out_prefix atacseq_merged  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf.score_cutoffs.tsv
#echo "done with merged peak set" 

#MAP TO CONSENSUS CTCF MOTIF 
python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atac_earlyG1_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix earlyG1.down.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt  --totext  --thresholds dmso_ctcf_consensus.score_cutoffs.tsv
echo "done with earlyG1 down" 

python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed  $base/atac_earlyG1_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix earlyG1.up.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv 
echo "done with earlyG1 up" 

python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atac_lateG1_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix lateG1.down.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv 
echo "done with lateG1 down" 

python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atac_lateG1_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix lateG1.up.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv 
echo "done with lateG1 up" 

python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atac_sg2m_dmso_control_DOWN.padded.bed --reference hg19/hg19.genome.fa --out_prefix SG2M.down.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv 
echo "done with SG2M down"

python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atac_sg2m_dmso_control_UP.padded.bed --reference hg19/hg19.genome.fa --out_prefix SG2M.up.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv 
echo "done with SG2M up"


#original set of full peaks!
python scan_motifs.py --pwm_list pwm_list_cisbp_CTCF_consensus.txt --positions_bed $base/atacseq_merged.peaks.padded.bed --reference hg19/hg19.genome.fa --out_prefix atacseq_merged.consensus  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.00001  --freqs --background_freqs dmso_ctcf.foreground_freqs.txt --totext --thresholds dmso_ctcf_consensus.score_cutoffs.tsv
echo "done with merged peak set" 
