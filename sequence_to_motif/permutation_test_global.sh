#run permutation test for Irene's TF's of interest
#uses union of Daniel's cross-celltype DNAse as foreground
for pval in   0.01 0.001 0.0001 0.00005 0.00001 0.000001
do
    python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.ATF3.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/ATF3_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 
 
    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.BRCA1.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/BRCA1_HUMAN.H10MO.D.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.CREB1.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/CREB1_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.CTCF.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/CTCF_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.E2F4.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/E2F4_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed
    #with hg19 background freqs

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.E2F4.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/E2F4_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs temp_freqs 
 
    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.FOXM1.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/FOXM1_HUMAN.H10MO.D.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 
    
    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.GABPA.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/GABPA_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.GATA1.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/GATA1_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 

    #python permutation_test_global.py --foreground_bed final_merged_set.bed --reference hg19/hg19.genome.fa --out_prefix global.test.MAX.$pval --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/MAX_HUMAN.H10MO.A.pwm --p_val $pval --foreground_freqs final_merged_set.freqs.bed 
done


