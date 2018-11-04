import xlsxwriter
import glob
import csv
import argparse
def parse_args():
    parser=argparse.ArgumentParser(description="merge multiple tsv or csv into 1 excel")
    parser.add_argument("--input_f",nargs="+")
    parser.add_argument("--input_delim",default="\t") 
    parser.add_argument("--outf")
    return parser.parse_args()

def main():
    args=parse_args() 
    workbook = xlsxwriter.Workbook(args.outf)
    for filename in args.input_f: 
        ws = workbook.add_worksheet(str(filename.split('/')[-1]))
        spamReader = csv.reader(open(filename, 'r'), delimiter=args.input_delim,quotechar='"')
        row_count = 0
        print(filename)
        for row in spamReader:
            for col in range(len(row)):
                ws.write(row_count,col,row[col])
            row_count +=1

    workbook.close()

if __name__=="__main__":
    main()
    