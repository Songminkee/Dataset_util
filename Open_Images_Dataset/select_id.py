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
        flag=False
        for ifo in info[id]:
            if ifo[1] == want_id: # 1: LabelName
                if ifo[11]=='0' and ifo[9]=='0': # 9: IsGroupOf , 11: IsInside
                    flag=True
                else:
                    flag=False
                    break
        if flag:
          dst.append(id)


    if not os.path.exists(dst_img_folder):
        os.makedirs(dst_img_folder)
    if not os.path.exists(dst_label_foler):
        os.makedirs(dst_label_foler)
    print('Find total {} data'.format(len(dst)))
    print('Move file from {} to {}'.format(image_folder,dst_img_folder))

    for id in dst:
        src_path = os.path.join(image_folder,id+'.jpg')
        subprocess.call(['mv',src_path,dst_img_folder])
        with open(os.path.join(dst_label_foler,id+'.txt'),'w') as f:
            for ifo in info[id]:
                if ifo[1] != want_id:
                    continue
                x_min,x_max,y_min,y_max = ifo[3:7]
                x_min, x_max, y_min, y_max = float(x_min),float(x_max),float(y_min),float(y_max)
                cx,cy = (x_min+x_max)/2,(y_min+y_max)/2
                w,h = (x_max-x_min),(y_max-y_min)
                f.write('{} {} {} {}\n'.format(cx,cy,w,h))

    print('Done!')

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Extracting specific IDs from Open Images Dataset V6 folders')
    parser.add_argument('--id', type=str, help='id you want extract', default='/m/025dyy')
    parser.add_argument('--annotation_file', type=str, help='oidv6-train-annotations-bbox.csv file path', default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/oidv6-train-annotations-bbox.csv')
    parser.add_argument('--image_folder', type=str, help='folder of data image',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/train_7')
    parser.add_argument('--dst_img_folder', type=str, help='image folder you want save',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/images')
    parser.add_argument('--dst_label_foler', type=str, help='label folder you want save',
                        default='/home/aiffel0042/Desktop/project/02.OBD,CD/object_dataset/labels')
    # 0~3 다시
    args = parser.parse_args()
    move_file(args)