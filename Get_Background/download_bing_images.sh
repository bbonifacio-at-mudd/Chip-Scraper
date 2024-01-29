#!/bin/bash

ORIGDIR=$PWD
TEMPDIR=$(mktemp -d)
DESTDIR="$HOME/Desktop/Active Insights/Starting Projects/Chip-Scraper/Get_Background/backgrounds"

fullurl() {
  python <<EOF
dombase = ["http://az608707.vo.msecnd.net/files/", "http://az619519.vo.msecnd.net/files/", "http://az619822.vo.msecnd.net/files/"]
imgfn = "$1"
index = 0
for char in list(imgfn):
  index = (index << 5) - index + ord(char)
  index &= index
print(dombase[abs(index) % len(dombase)] + imgfn)
EOF
}

mkdir -p "$DESTDIR"
pushd "$TEMPDIR"
mkdir info

# Debug: Check if the correct page is downloaded
echo "Downloading image list..."
wget 'https://www.bing.com/gallery/home/browsedata?z=0' -O imagelist

# Debug: Check the contents of the downloaded file
echo "Contents of the imagelist file:"
cat imagelist

cat imagelist | cut -d] -f3 | cut -d[ -f2 | tr -d '"' | sed 's/,/\n/g' > imageids

for id in $(head -n4 imageids)
do
  echo "Processing ID: $id"
  wget "https://www.bing.com/gallery/home/imagedetails/${id}?z=0" -O "info/${id}"

  # Debug: Check the contents of the info file
  echo "Contents of the info file for ID $id:"
  cat "info/${id}"

  imgfn=$(cat "info/${id}" | sed 's/,/\n/g' | tr -d '"' | grep ^wpFullFilename | cut -d: -f2)
  sanitized_imgfn=$(echo "$imgfn" | sed 's/[^a-zA-Z0-9._-]/_/g') # Sanitize filename

  # Debug: Print out the image filename
  echo "Image filename: $sanitized_imgfn"

  full_image_url=$(fullurl "$imgfn")
  
  # Debug: Print out the full image URL
  echo "Full image URL: $full_image_url"

  if [[ -n "$sanitized_imgfn" ]]; then
    wget "$full_image_url" -O "$DESTDIR/$sanitized_imgfn"
  else
    echo "Failed to extract image filename for ID $id"
  fi
done

popd
rm -r "$TEMPDIR"
