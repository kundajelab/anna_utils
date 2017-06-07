cut -f 1 /mnt/data/annotations/by_release/hg20.GRCh38/hg38.chrom.sizes >chrom_sizes
#for chrom in `seq 1 19`
for chrom in $(cat /mnt/data/annotations/by_release/hg20.GRCh38/hg38.chrom.sizes|cut -f1)
do
    #python permute_genome.py --reference hg19/hg19.genome.fa --out_prefix hg19/hg19.suffled --chrom_sizes hg19/hg19.chrom.sizes --bin_size 1000 --chrom chr$chrom
    #python permute_genome.py --reference /mnt/data/annotations/by_release/mm10/GRCm38.genome.fa --out_prefix mm10.shuffled --chrom_sizes /mnt/data/annotations/by_release/mm10/mm10.male.chrom.sizes --bin_size 1000 --chrom chr$chrom
    #echo "finished!:"+chr$chrom
    echo "finished!:" +$chrom	
done
