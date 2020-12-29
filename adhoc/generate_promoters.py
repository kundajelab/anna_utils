data=open('/mnt/lab_data/kundaje/annashch/hg19.tss.bed','r').read().strip().split('\n')
outf=open("hg19.2kb.promters.bed",'w')
for line in data:
    tokens=line.split('\t')
    chrom=tokens[0]
    startpos=tokens[3]
    endpos=tokens[4]
    strand=tokens[6]
    #get teh gene id & name
    meta=[i.strip() for i in tokens[8].split(';')]
    cur_name=None
    cur_id=None
    for m in meta:
        if m.startswith('gene_id'):
            cur_id=m.split('"')[1]
        elif m.startswith('gene_name'):
            cur_name=m.split('"')[1]
    if strand=="+":
        prom_start=str(int(startpos)-2000)
        prom_end=startpos
    elif strand=="-":
        prom_start=endpos
        prom_end=str(int(endpos)+2000)
    else:
        print(strand)
        print('invalid strand specified; must be + or - ') 
    outf.write(chrom+'\t'+prom_start+'\t'+prom_end+'\t'+strand+'\t'+str(cur_id)+'\t'+str(cur_name)+'\n')
    
    
