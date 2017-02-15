for chrom in `seq 1 22` X Y M
do
    python permute_genome.py --reference hg19/hg19.genome.fa --out_prefix hg19/hg19.suffled --chrom_sizes hg19/hg19.chrom.sizes --bin_size 1000 --chrom chr$chrom
    echo "finished!:"+chr$chrom
done
