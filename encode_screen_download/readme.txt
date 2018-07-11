1. download ENCODE summary JSON: https://www.encodeproject.org/search/?searchTerm=cREs&type=FileSet&limit=all&format=json
2. grep out accessions to a file called "accessions". See example here 
3. convert accessions to url: https://www.encodeproject.org/publication-data/[ACCESSION]?format=json 
To do this, run "accession_to_download_link.py"
4. download accession urls
5. extract summary file for screen datasets.
To do this, run "parse_accession_jsons.sh"
6 run wget to download the files in column 2 of the resulting "screen_bed_files.txt" file

