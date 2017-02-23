#run permutation test for Irene's TF's of interest
#uses union of Daniel's cross-celltype DNAse as foreground
#use this range of p-values for histogram & fdr plots 
#for pval in 0.01 0.001 0.0001 0.00005 0.00001 0.000001 0.0000001
#use this range of p-values to find score-cutoff & calculate number of genome hits. 
for pval in 0.00001 #0.0001 0.00005 
do
    #ATF3
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.ATF3.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt  --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/ATF3_HUMAN.H10MO.A.pwm --p_val $pval --test_to_perform score_cutoff --fdr_thresh 0.2  &

    #TAL1_A
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.TAL1.A.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/TAL1_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #TAL1_S
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.TAL1.S.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/TAL1_HUMAN.H10MO.S.pwm --p_val $pval   --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #CREB1
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.CREB1.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/CREB1_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #CTCF
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.CTCF.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/CTCF_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #E2F4
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.E2F4.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/E2F4_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #ELF1
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.ELF1.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/ELF1_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #GABPA
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.GABPA.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/GABPA_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 & 

    #GATA1
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.GATA1.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/GATA1_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &

    #MAX
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.MAX.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/MAX_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &
 
    #IRF1
    python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix k562.test.IRF1.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/IRF1_HUMAN.H10MO.A.pwm --p_val $pval  --test_to_perform score_cutoff --fdr_thresh 0.2 &
done
