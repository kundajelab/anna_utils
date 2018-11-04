import argparse
def parse_args():
    parser=argparse.ArgumentParser(description="extract gene coordinates for a gene list")
    parser.add_argument("--ref_gtf",default="/mnt/data/annotations/by_release/hg19.GRCh37/GENCODE_ann/gencode.v19.annotation.gtf")
    parser.add_argument("--gene_list")
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args()
    gene_list=open(args.gene_list,'r').read().strip().split('\n')
    gene_dict=dict()
    for gene in gene_list:
        gene_dict[gene]=1
    print("loaded gene list")
    data=open(args.ref_gtf,'r').read().split('\n')
    print("loaded source gtf")
    outf=open(args.outf,'w')
    header=data[0]
    for line in data[1::]:
        if line.startswith('#'):
            continue 
        tokens=line.split(';')
        for token in tokens:
            if token.strip().startswith('gene_name'):
                posinfo=tokens[0].split()
                chrom=posinfo[0]
                startpos=posinfo[3]
                endpos=posinfo[4]
                genename=token.split('"')[1]
                if genename in gene_dict:
                    outf.write('\t'.join([chrom,startpos,endpos,genename])+'\n')
        
                
if __name__=="__main__":
    main()
