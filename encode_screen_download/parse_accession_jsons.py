import json 
import argparse
from os import listdir 
from os.path import isfile,join 
import pdb 

def parse_args(): 
    parser=argparse.ArgumentParser(description="download the 5-state bed files from ENCODE screen")
    parser.add_argument("--source",default=None)
    parser.add_argument("--source_dir",default=None)
    parser.add_argument("--source_dir_prefix",default=None) 
    parser.add_argument("--outf") 
    return parser.parse_args() 

def get_category(description): 
    options=['9-state high H3K27ac',
             '9-state high H3K4me3',
             '5-group',
             '9-state high CTCF',
             '9-state high DNase']
    for opt in options: 
        if description.startswith(opt): 
            return opt
    for opt in options: 
        if opt in description: 
            return opt
    return description


def identify_files_to_parse(args):
    #load the json(s) 
    to_load=[] 
    if args.source_dir!=None: 
        #get all files starting with a specific prefix in the directory 
        onlyfiles=[f for f in listdir(args.source_dir) if isfile(join(args.source_dir,f))]
        for f in onlyfiles: 
            if f.startswith(args.source_dir_prefix): 
                to_load.append('/'.join([args.source_dir,f]))
    else: 
        #only a single file specified 
        to_load.append(arg.source)
    return to_load

def main(): 
    args=parse_args() 
    to_load=identify_files_to_parse(args) 
    total=len(to_load) 

    #create output file 
    outf=open(args.outf,'w')
    outf.write('Accesion\tDownloadURL\tAssembly\tCategory\tDescription\tTissue\tDevelopmentalStage\tLifeStage\n')
    counter=0

    for f in to_load: 
        print(str(counter)+'/'+str(total))
        try:
            data=json.loads(open(f,'r').read())
            try:
                description=data['description'] 
                category=get_category(description)
            except: 
                description="NA"
                category="NA"
            try:
                assembly=','.join(data['assembly'])
            except: 
                assembly="NA"
            try:
                tissue=','.join(data['organ_slims'])
            except: 
                tissue='NA'
            try:
                developmental_slims=','.join(data['developmental_slims'])
            except: 
                developmantal_slims='NA'
            try:
                life_stage=data['relevant_life_stage'] 
            except: 
                life_stage='NA'
            all_files=data['files'] 
            for f in all_files: 
                accession=f['accession']             
                download_url=''.join(['https://www.encodeproject.org/files/',accession,'/@@download/',accession,'.bed.gz'])
                outf.write(accession+'\t'+
                           download_url+'\t'+
                           assembly+'\t'+
                           category+'\t'+
                           description+'\t'+
                           tissue+'\t'+
                           developmental_slims+'\t'+
                           life_stage+'\n')
        except:
            pdb.set_trace()
        counter+=1 


if __name__=="__main__": 
    main() 
