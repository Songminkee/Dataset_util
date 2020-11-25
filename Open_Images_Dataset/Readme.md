# Open Images Dataset v6 Util

- #### [Open Images Dataset v6 link](https://storage.googleapis.com/openimages/web/download.html)



## Data Download

1. install [awscli](https://aws.amazon.com/ko/cli/)
2. Visit site of [Open Images Dataset github](https://github.com/cvdfoundation/open-images-dataset#download-images-with-bounding-boxes-annotations)
3. Download the data you want using awscli
   - ex) aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_0.tar.gz [target_dir]



## Extracting specific IDs from Open Images Dataset V6 folders for Detection

```
python Open_Images_Dataset/select_di.py --id [id you want] --annotation_file[oidv6-train-annotations-bbox.csv fil path] --image_folder [folder of data image] --dst_img_folder [image folder you want save] --dst_label_folder [label folder you want save]
```



## TODO

- extract label info