#for chrom in `seq 1 19`
for chrom in X
do
    #python permute_genome.py --reference hg19/hg19.genome.fa --out_prefix hg19/hg19.suffled --chrom_sizes hg19/hg19.chrom.sizes --bin_size 1000 --chrom chr$chrom
    #python permute_genome.py --reference /mnt/data/annotations/by_release/mm10/GRCm38.genome.fa --out_prefix mm10.shuffled --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --bin_size 1000 --chrom chr$chrom
    python permute_genome.py --reference mm10/GRCm38.genome.fa --out_prefix mm10.shuffled --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --bin_size 1000 --chrom chr$chrom 
    echo "finished!:"+chr$chrom
done
