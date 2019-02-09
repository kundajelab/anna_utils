#generates splits for cross-validation
#hg19 (i.e. /mnt/data/annotations/by_release/hg19.GRCh37/hg19.chrom.sizes) 
splits=dict()
splits[0]={'test':['chr1'],
           'valid':['chr10','chr8']}
splits[1]={'test':['chr19','chr2'],
           'valid':['chr1']}
splits[2]={'test':['chr3','chr20'],
           'valid':['chr1']}
splits[3]={'test':['chr13','chr6'],
           'valid':['chr3','chr20']}
splits[4]={'test':['chr5','chr16','chrY'],
           'valid':['chr13','chr6','chr22']}
splits[5]={'test':['chr4','chr15','chr21'],
           'valid':['chr5','chr16','chrY']}
splits[6]={'test':['chr7','chr18','chr14'],
           'valid':['chr4','chr15','chr21']}
splits[7]={'test':['chr11','chr17','chrX'],
           'valid':['chr7','chr18','chr14']}
splits[8]={'test':['chr12','chr9'],
           'valid':['chr11','chr17','chrX']}
splits[9]={'test':['chr10','chr8'],
           'valid':['chr12','chr9']}
