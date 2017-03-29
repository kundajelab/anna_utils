genes=open('DESEQ2.genes.pval.0.05.significant.csv','r').read().strip().split('\n')
outf_genes=open('gene_heatmap_inputs.tsv','w')
outf_genes.write('GeneName\tWT_R\tWT_L\tMDX_R\tMDX_L\n')
sig_gene_dict=dict()

print("genes:") 
for line in genes:
    tokens=line.split('\t')
    if (tokens[10]=="1") or (tokens[11]=="1"):
        fpkm_vals=tokens[2:6]
        outf_genes.write(tokens[0]+'\t'+'\t'.join(fpkm_vals)+'\n')
