#perform permutation-test to calculate cell-type specific foreground. 

#for pval in 0.00005 #0.0001 0.00005 0.00001
#do
#    for thresh in 0.2 #0.3 0.35 0.4 #0.01 0.05 0.1 0.15 0.25
#    do

	#k562 cells 
	#python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt  --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list.txt  --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh

	#Nadine's peaks
	#python permutation_test_global.py --foreground_bed nadine_bed_file.padded.txt --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval.nadine_data --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh --foreground_freqs fdr0.2.pval.0.00005.nadine_data.foreground_freqs.txt
	
	#heterokaryon peaks (H1)
	#python permutation_test_global.py --foreground_bed heterokaryon.labels.bed --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval.heterokaryon_data --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh 
	
	#gecco union peak set
	#python permutation_test_global.py --foreground_bed gecco.sampled.labels.bed --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval.gecco_data --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh
	
	#dmso peak set
	#python permutation_test_global.py --foreground_bed dmso.labels.bed --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval.dmso_data --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh


 #   done
#done

#THIS IS USING THE CISBP MOTIF SET
#Peyton peak set

#nadine_diff_wrt_HSC_april4_240k.bed
export pval=0.00005
export thresh=0.2
#python permutation_test_global.py --foreground_bed peaks_nadine_diff_wrt_HSC_april4_240K.bed --reference hg19/hg19.genome.fa --out_prefix thresholds_nadine_diff_wrt_HSC_april4_240K --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list_cisbp.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh --freqs 

#nadine_binary_test_april12
python permutation_test_global.py --foreground_bed peaks_nadine_binary_test_april12.bed --reference hg19/hg19.genome.fa --out_prefix thresholds_nadine_binary_test_april12 --permuted_reference hg19/hg19.shuffled.fa --pwm pwm_list_cisbp.txt --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh --freqs 
