#!/usr/bin/env fish

cd ./PDF

mkdir -p backup-pdf

for file in *.pdf
    set output_file (string replace -r '.pdf$' '_unencrypted.pdf' $file)
    
    set input_path (pwd)/$file
    set output_path (pwd)/$output_file
    set backup_path (pwd)/backup-pdf/$file
    
    qpdf --decrypt $input_path $output_path
    
    mv $input_path $backup_path
end

