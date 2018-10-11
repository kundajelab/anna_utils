source=open('RSEM.genes.fpkm.gt1.tsv','r').read().strip().split('\n')
outf=open('RSEM.genes.fpkm.gt1.averaged.tsv','w')
outf.write('GeneName\tGeneID\tWT_R\tWT_L\tMDX_R\tMDX_L\n')
for line in source[1::]:
    tokens=line.split('\t')
    gene_info=tokens[0:2]
    wt_r=0.5*(float(tokens[3])+float(tokens[4]))
    wt_l=0.5*(float(tokens[5])+float(tokens[6]))
    mdx_r=0.333*(float(tokens[8])+float(tokens[9])+float(tokens[10]))
    mdx_l=0.333*(float(tokens[11])+float(tokens[12])+float(tokens[13]))
    outf.write(tokens[0]+'\t'+tokens[1]+'\t'+str(round(wt_r,3))+'\t'+str(round(wt_l,3))+'\t'+str(round(mdx_r,3))+'\t'+str(round(mdx_l,3))+'\n')
    

source=open('RSEM.isoforms.fpkm.tsv','r').read().strip().split('\n')
outf=open('RSEM.isoforms.fpkm.averaged.tsv','w')
outf.write('GeneName\tTranscriptID\tGeneID\tWT_R\tWT_L\tMDX_R\tMDX_L\n')
for line in source[1::]:
    tokens=line.split('\t')
    gene_info=tokens[0:3]
    wt_r=0.5*(float(tokens[4])+float(tokens[5]))
    wt_l=0.5*(float(tokens[6])+float(tokens[7]))
    mdx_r=0.333*(float(tokens[9])+float(tokens[10])+float(tokens[11]))
    mdx_l=0.333*(float(tokens[12])+float(tokens[13])+float(tokens[14]))
    outf.write(tokens[0]+'\t'+tokens[1]+'\t'+tokens[2]+'\t'+str(round(wt_r,3))+'\t'+str(round(wt_l,3))+'\t'+str(round(mdx_r,3))+'\t'+str(round(mdx_l,3))+'\n')
    

