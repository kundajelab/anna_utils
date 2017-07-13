export base=/srv/scratch/annashch/dmso/map_of_gene_to_enhancer/results/predicted_impact_scores

#python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.earlyG1.down.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix earlyG1.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
echo "done with earlyG1 down" 

python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.earlyG1.up.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix earlyG1.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
#echo "done with earlyG1 up" 

python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.lateG1.down.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix lateG1.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
#echo "done with lateG1 down" 

python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.lateG1.up.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix lateG1.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
#echo "done with lateG1 up" 

python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.SG2M.down.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix SG2M.down  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
#echo "done with SG2M down"

python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed $base.SG2M.up.tsv.sorted.peaks --reference hg19/hg19.genome.fa --out_prefix SG2M.up  --chrom_sizes hg19/hg19.chrom.sizes --num_hits_per_motif 1 --p_val 0.000001  --freqs --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --totext
#echo "done with SG2M up"
