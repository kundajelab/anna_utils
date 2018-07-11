accessions=open('accessions','r').read().strip().split('\n') 
outf=open('accessions.url','w')
for line in accessions: 
    outf.write("http://www.encodeproject.org/annotations/"+line+"/?format=json\n")
