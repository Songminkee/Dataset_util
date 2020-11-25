import os
import subprocess
import glob
import argparse

def move_file(args):
    annotation_file = args.annotation_file
    image_folder = args.image_folder
    im_path = glob.glob(os.path.join(image_folder,'*'))
    dst_img_folder = args.dst_img_folder
    dst_label_foler = args.dst_label_foler
    want_id = args.id

    print('Read image id')
    info = dict()
    for p in im_path:
        info[p.split('/')[-1].split('.')[0]]=[]

    print('Read image info')
    f = open(annotation_file,'r')
    lines = f.readlines()
    for i in range(1,len(lines)):
        l = lines[i].strip('\n').split(',')
        if l[0] in info.keys():
            info[l[0]].append(l[1:])
    f.close()

    print('Select image of box')
    dst=[]
    for id in info.keys():
        flag=True
        for ifo in info[id]:
            if ifo[1] != want_id:
                flag=False
                break
        if flag:
          dst.append(id)


    if not os.path.exists(dst_img_folder):
        os.makedirs(dst_img_folder)
    if not os.path.exists(dst_label_foler):
        os.makedirs(dst_label_foler)

    print('Move file from {} to {}'.format(image_folder,dst_img_folder))

    for id in dst:
        src_path = os.path.join(image_folder,id+'.jpg')
        subprocess.call(['mv',src_path,dst_img_folder])

    # TODO: extract bounding box info:

    print('Done!')

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Classifying specific IDs from Open Images Dataset V6 folders')
    parser.add_argument('--id', type=str, help='', default='/m/025dyy')
    parser.add_argument('--annotation_file', type=str, help='', default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/oidv6-train-annotations-bbox.csv')
    parser.add_argument('--image_folder', type=str, help='',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/train_1')
    parser.add_argument('--dst_img_folder', type=str, help='',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/box_img')
    parser.add_argument('--dst_label_foler', type=str, help='',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/labels')

    args = parser.parse_args()
    move_file(args)