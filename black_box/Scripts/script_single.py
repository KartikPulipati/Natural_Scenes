import cv2
import os
import random
import math

test_or_train = ['seg_test', 'seg_train']
cat_or_dog = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
directory = '../normal/archive'
dump = 'black_box_single'
color = (0, 0, 0)


for t in test_or_train:
    for cd in cat_or_dog:
        num = 1
        for fn in os.listdir(directory+'/'+t+'/'+cd):
            image = cv2.imread(os.path.join(directory+'/'+t+'/'+cd, fn))
            if image is not None:

                h, w = image.shape[0:2]

                rh = random.randint(0, h - math.ceil(h/math.sqrt(10)))
                rw = random.randint(0, w - math.ceil(w/math.sqrt(10)))

                image = cv2.rectangle(image, (rw, rh), (rw+math.floor(w/math.sqrt(10)), rh+math.floor(h/math.sqrt(10))), color, -1)

                cv2.imwrite(os.path.join(dump+'/'+t+'/'+cd, t+cd+str(num)+'.jpg'), image)
                num += 1
