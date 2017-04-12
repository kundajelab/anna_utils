#genome-wide scan 
#for chrom in `seq 1 22` X Y M
#do
    #python scan_motifs.py --pwm_dir=pwm --reference hg19/hg19.genome.fa --out_prefix hocomocov10_hg19_1kb_S_by_M  --chrom_sizes hg19/hg19.chrom.sizes --background_freqs hg19_background_freqs.txt --chrom chr$chrom --num_hits_per_motif 1 &
    #python scan_motifs.py --pwm_dir=pwm --reference hg19/hg19.genome.fa --out_prefix hocomocov10_hg19_1kb_S_by_M  --chrom_sizes hg19/hg19.chrom.sizes --background_freqs hg19_background_freqs.txt --chrom chr$chrom --num_hits_per_motif 1 --p_val 0.0001 &
    #python scan_motifs.py --pwm_dir=pwm --reference hg19/hg19.genome.fa --out_prefix hocomocov10_hg19_1kb_S_by_M  --chrom_sizes hg19/hg19.chrom.sizes --background_freqs hg19_background_freqs.txt --chrom chr$chrom --num_hits_per_motif 3 &
    #python scan_motifs.py --pwm_dir=pwm --reference hg19/hg19.genome.fa --out_prefix hocomocov10_hg19_1kb_S_by_M  --chrom_sizes hg19/hg19.chrom.sizes --background_freqs hg19_background_freqs.txt --chrom chr$chrom --num_hits_per_motif 3 --p_val 0.0001 
#done


#Nadine's project
python scan_motifs.py --pwm_dir=pwm --reference hg19/hg19.genome.fa --out_prefix nadine_heme_project --chrom_sizes hg19/hg19.chrom.sizes  --num_hits_per_motif 1 --p_val 0.00005 --positions_bed nadine_bed_file.padded.txt --binarize --thresholds fdr0.2.pval.0.00005.nadine_data.score_cutoffs.tsv 

#heterokaryon scan (training) 
##python scan_motifs.py --pwm_dir=pwm --reference /mnt/data/annotations/by_release/heterokaryon_hg19_mm9_WOALTERNATE/WOALTERNATES/hg19_mm9_phix_WOALTERNATES.fa --out_prefix het.train --chrom_sizes hg19_mm9_phix_WOALTERNATES.chrom.sizes  --background_freqs fdr0.2.pval.0.00005.heterokaryon_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed het.train.txt --thresholds fdr0.2.pval.0.00005.heterokaryon_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/heterokaryon/inputs/new.labels.txt --numlabels_for_hdf5 43

#heterokaryon gscan (validation) 
#python scan_motifs.py --pwm_dir=pwm --reference /mnt/data/annotations/by_release/heterokaryon_hg19_mm9_WOALTERNATE/WOALTERNATES/hg19_mm9_phix_WOALTERNATES.fa --out_prefix het.validate --chrom_sizes hg19_mm9_phix_WOALTERNATES.chrom.sizes  --background_freqs fdr0.2.pval.0.00005.heterokaryon_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed het.validate.txt --thresholds fdr0.2.pval.0.00005.heterokaryon_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/heterokaryon/inputs/new.labels.txt --numlabels_for_hdf5 43

#heterokaryon scan (test) 
#python scan_motifs.py --pwm_dir=pwm --reference /mnt/data/annotations/by_release/heterokaryon_hg19_mm9_WOALTERNATE/WOALTERNATES/hg19_mm9_phix_WOALTERNATES.fa --out_prefix het.test --chrom_sizes hg19_mm9_phix_WOALTERNATES.chrom.sizes  --background_freqs fdr0.2.pval.0.00005.heterokaryon_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed het.test.txt --thresholds fdr0.2.pval.0.00005.heterokaryon_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/heterokaryon/inputs/new.labels.txt --numlabels_for_hdf5 43


#gecco scan training
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix gecco.train --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.gecco_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed gecco.sampled.train.txt --thresholds fdr0.2.pval.0.00005.gecco_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/gecco/inputs/gecco.sampled.labels.txt --numlabels_for_hdf5 61

#gecco scan validation
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix gecco.validate --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.gecco_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed gecco.sampled.validate.txt --thresholds fdr0.2.pval.0.00005.gecco_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/gecco/inputs/gecco.sampled.labels.txt --numlabels_for_hdf5 61

#gecco scan test
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix gecco.test --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.gecco_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed gecco.sampled.test.txt --thresholds fdr0.2.pval.0.00005.gecco_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/gecco/inputs/gecco.sampled.labels.txt --numlabels_for_hdf5 61

#dmso scan train
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix dmso.train --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed dmso.train.txt --thresholds fdr0.2.pval.0.00005.dmso_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/dmso/inputs/newNegativeSet.labels.txt --numlabels_for_hdf5 12


#dmso scan validate
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix dmso.validate --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed dmso.validate.txt --thresholds fdr0.2.pval.0.00005.dmso_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/dmso/inputs/newNegativeSet.labels.txt --numlabels_for_hdf5 12


#dmso scan test
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix dmso.test --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed dmso.test.txt --thresholds fdr0.2.pval.0.00005.dmso_data.score_cutoffs.tsv --position_bin_size 250 --dump_hdf5 --labels_for_hdf5 /srv/scratch/annashch/deeplearning/dmso/inputs/newNegativeSet.labels.txt --numlabels_for_hdf5 12


#positions 
#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix gecco.deeplift.vars --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.gecco_data.foreground_freqs.txt --num_hits_per_motif 3 --p_val 0.00005 --positions_bed ref.seq.inputs.gdl --thresholds fdr0.2.pval.0.00005.gecco_data.score_cutoffs.tsv --position_bin_size 250 


#for medusa-- PRESENCE 
#python scan_motifs.py --pwm_dir=pwm --reference /mnt/data/annotations/by_release/heterokaryon_hg19_mm9_WOALTERNATE/WOALTERNATES/hg19_mm9_phix_WOALTERNATES.fa --out_prefix het.medusa.presence --chrom_sizes hg19_mm9_phix_WOALTERNATES.chrom.sizes  --background_freqs fdr0.2.pval.0.00005.heterokaryon_data.foreground_freqs.txt --num_hits_per_motif 1 --p_val 0.00005 --positions_bed het_peaks_medusa_presence.bed --thresholds fdr0.2.pval.0.00005.heterokaryon_data.score_cutoffs.tsv --binarize

#for medusa -- DIFFERENTIAL
#python scan_motifs.py --pwm_dir=pwm --reference /mnt/data/annotations/by_release/heterokaryon_hg19_mm9_WOALTERNATE/WOALTERNATES/hg19_mm9_phix_WOALTERNATES.fa --out_prefix het.medusa.differential --chrom_sizes hg19_mm9_phix_WOALTERNATES.chrom.sizes  --background_freqs fdr0.2.pval.0.00005.heterokaryon_data.foreground_freqs.txt --num_hits_per_motif 1 --p_val 0.00005 --positions_bed het_peaks_medusa_differential.bed --thresholds fdr0.2.pval.0.00005.heterokaryon_data.score_cutoffs.tsv --binarize



#python scan_motifs.py --pwm_dir pwm --reference hg19/hg19.genome.fa --out_prefix dmso.labels --chrom_sizes hg19/hg19.chrom.sizes --background_freqs fdr0.2.pval.0.00005.dmso_data.foreground_freqs.txt --num_hits_per_motif 1 --p_val 0.00005 --positions_bed dmso.labels.txt --thresholds fdr0.2.pval.0.00005.dmso_data.score_cutoffs.tsv
