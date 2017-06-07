#floating number motif scores 
#python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed Sox2_1_3_rep1-pr.IDR0.05.filt.12-col.bed  --reference /users/raunaq/chip-nexus-project/out_files/Sox2_2/moods_scan/sequence_to_motif/mm10/GRCm38.genome.fa --out_prefix DEBUG_moods_scan_sox2_all --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --num_hits_per_motif 1 --p_val 0.001  --freqs  --position_bin_size 1 --thresholds thresholds_sox2_mm10.score_cutoffs.tsv

#binarized motif scores 
#python scan_motifs.py --pwm_list pwm_list_cisbp.txt --positions_bed Sox2_1_3_rep1-pr.IDR0.05.filt.12-col.bed  --reference /mnt/data/annotations/by_release/mm10/GRCm38.genome.fa --out_prefix moods_scan_sox2_binarized_all --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --num_hits_per_motif 1 --p_val 0.001  --freqs --position_bin_size 1 --thresholds thresholds_sox2_mm10.score_cutoffs.tsv --binarize


#full set of chroms
#python scan_motifs.py --pwm_list pwm_list_cisbp.txt  --reference /mnt/data/annotations/by_release/mm10/GRCm38.genome.fa --out_prefix moods_scan_sox2_genome_wide --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --num_hits_per_motif 1 --p_val 0.001  --freqs --position_bin_size 1 --thresholds thresholds_sox2_mm10.score_cutoffs.tsv --binarize --background_freqs thresholds_sox2_mm10.foreground_freqs.txt --reference_bin_size 1000

#only main chromosomes, global scan 
python scan_motifs.py --pwm_list pwm_list.txt --positions_bed /srv/scratch/manyu/motif_scans/ZBTB33_K562_optimal_idr_padded_filteredforChronly.bed --reference /mnt/data/annotations/by_organism/human/hg20.GRCh38/GRCh38.genome.fa --out_prefix /srv/scratch/manyu/motif_scans/moods_scan_hocomoco --chrom_sizes /mnt/data/annotations/by_organism/human/hg20.GRCh38/hg38.chrom.sizes --num_hits_per_motif 1 --p_val 0.001  --freqs --position_bin_size 1  --background_freqs /srv/scratch/manyu/motif_scans/pwm_thresholds.foreground_freqs.txt --reference_bin_size 1000 
