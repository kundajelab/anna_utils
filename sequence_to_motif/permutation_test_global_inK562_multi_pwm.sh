for pval in 0.0001 0.00005 0.00001
do
    for thresh in 0.3 0.35 0.4 #0.01 0.05 0.1 0.15 0.25
    do
	python permutation_test_global.py --foreground_bed ENCSR000EPC.K562_Leukemia_Cells.UW_Stam.DNase-seq_rep1-pr.IDR0.1.filt.narrowPeak --reference hg19/hg19.genome.fa --out_prefix fdr$thresh.pval.$pval --foreground_freqs k562.test.ATF3.0.01.foreground_freqs.txt  --permuted_reference hg19/hg19.shuffled.fa --pwm pwm/ATF3_HUMAN.H10MO.A.pwm pwm/TAL1_HUMAN.H10MO.A.pwm pwm/CREB1_HUMAN.H10MO.A.pwm pwm/CTCF_HUMAN.H10MO.A.pwm pwm/E2F4_HUMAN.H10MO.A.pwm pwm/ELF1_HUMAN.H10MO.A.pwm pwm/GABPA_HUMAN.H10MO.A.pwm pwm/GATA1_HUMAN.H10MO.A.pwm pwm/MAX_HUMAN.H10MO.A.pwm pwm/IRF1_HUMAN.H10MO.A.pwm --p_val $pval --test_to_perform score_cutoff --fdr_thresh $thresh
	echo "done!: $pval $thresh"
    done
done
