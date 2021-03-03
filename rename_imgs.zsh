#!/bin/zsh

image_path=/enter/directory/here/Downloads/geoPose3K

new_path=/enter/directory/here/images

echo "Original Photo Amount plus the README file:"
ls -l $image_path | wc -l


# This for-loop takes opens each folder and copies the image twice: once to a folder with the info.txt file, 
# and again to a directory with all of the images only for data manipulation. It renames each image as "photo"+ 
# a number (i), and renames each info.txt file to include the corresonded (i) value. 

i=1
for folder in "${image_path}"/* ; do
    if [ -d "${folder}" ]; then
        if [[ -f ${folder}/photo.jpeg && -f ${folder}/info.txt ]]; then
            mkdir $new_path/photo${i}
            cp "$folder/photo.jpeg" "${new_path}/photo$i/photo$i.jpeg" #image + info dir
            cp "$folder/photo.jpeg" /enter/directory/here/imageonly/photo"${i}".jpeg #image only dir
            cp "$folder/info.txt" "${new_path}/photo$i/info$i.txt"
            ((i++))
        elif [[ -f ${folder}/photo.jpg && -f ${folder}/info.txt ]]; then
            mkdir $new_path/photo${i}
            cp "$folder/photo.jpg" "${new_path}/photo$i/photo$i.jpg"
            cp "$folder/photo.jpg" /enter/directory/here/imageonly/photo"${i}".jpg
            cp "$folder/info.txt" "${new_path}/photo$i/info$i.txt"
            ((i++))
        fi
    fi
done

echo "Final Amount Copied Over:" 
ls -l $new_path | wc -l

echo "ImageOnly: "
ls -l /enter/directory/here/imageonly | wc -l
