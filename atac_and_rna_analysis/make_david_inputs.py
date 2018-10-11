data=open("DESEQ2.genes.pval.0.05.significant.csv",'r').read().strip().replace('\tNA','\t0').split('\n')
#we care about the MDX_L vs MDX_R and WT_L vs WT_R comparisons & the intersection of these.
group_dict=dict()
group_dict['mdx_only_up']=[]
group_dict['mdx_only_down']=[]
group_dict['wt_only_up']=[]
group_dict['wt_only_down']=[]
group_dict['both_up']=[]
group_dict['both_down']=[]
group_dict['mdx_only_diff']=[]
group_dict['wt_only_diff']=[]
group_dict['both_diff']=[]

for line in data[2::]:
    tokens=line.split('\t')
    gene_names=tokens[0:2] 
    wt_sig=int(tokens[10])
    mdx_sig=int(tokens[11])
    if (wt_sig==True) and (mdx_sig==True):
        group_dict['both_diff'].append(tuple(gene_names))
    if (wt_sig==True) and (mdx_sig==False):
        group_dict['wt_only_diff'].append(tuple(gene_names))
    if (wt_sig==False) and (mdx_sig==True):
        group_dict['mdx_only_diff'].append(tuple(gene_names))
    
    wt_fc=float(tokens[6])
    mdx_fc=float(tokens[7])
    mdx_up=False
    mdx_down=False
    wt_up=False
    wt_down=False    
    if mdx_sig and (mdx_fc >0):
        mdx_up=True
    if mdx_sig and (mdx_fc <0):
        mdx_down=True
    if wt_sig and (wt_fc >0):
        wt_up=True
    if wt_sig and (wt_fc <0):
        wt_down=True
    #check both up
    if (wt_up==True) and (mdx_up==True):
        group_dict['both_up'].append(tuple(gene_names))
    if (wt_down==True) and (mdx_down==True):
        group_dict['both_down'].append(tuple(gene_names))
    if (wt_up==True) and (mdx_up==False):
        group_dict['wt_only_up'].append(tuple(gene_names))
    if (wt_up==False) and (mdx_up==True):
        group_dict['mdx_only_up'].append(tuple(gene_names))
    if (wt_down==True) and (mdx_down==False):
        group_dict['wt_only_down'].append(tuple(gene_names))
    if (wt_down==False) and (mdx_down==True):
        group_dict['mdx_only_down'].append(tuple(gene_names))
#print the results
for key in group_dict:
    outf=open('DAVID.inputs.'+key,'w')
    for value in group_dict[key]:
        outf.write(value[0]+'\n')
            
    
        
