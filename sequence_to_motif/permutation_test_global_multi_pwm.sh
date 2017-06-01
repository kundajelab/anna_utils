export pval=0.001
export thresh=0.35
#python permutation_test_global.py --foreground_bed /srv/scratch/shared/surya/raunaq/chip-nexus/data-stowers/semi_processed/Sox2_1_3/out/peak/idr/optimal_set/Sox2_1_3_rep1-pr.IDR0.05.filt.12-col.bed --reference /users/raunaq/chip-nexus-project/out_files/Sox2_2/moods_scan/sequence_to_motif/mm10/GRCm38.genome.fa --out_prefix thresholds_sox2_mm10 --permuted_reference all_GRCm38.permuted.fasta --pwm pwm_list_cisbp.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh --freqs

python permutation_test_global.py --foreground_bed Sox2_1_3_rep1-pr.IDR0.05.filt.12-col.bed --reference /users/raunaq/chip-nexus-project/out_files/Sox2_2/moods_scan/sequence_to_motif/mm10/GRCm38.genome.fa --out_prefix thresholds_sox2_mm10 --permuted_reference all_GRCm38.permuted.fasta --pwm pwm_list_cisbp.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh --freqs
