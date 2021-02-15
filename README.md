Is Pic With Person
-------------------------

The idea is to build out a simple python script that uses ml to answer if a person is in a picture
From here there will be some utilities around this script to test it an eventually catalog my images

## Running

It's python... so it probably won't work

but in theory run

```
source ./venv/bin/activate
python ./is-pic-with-person.py /Path-To-Directory-With-Images
```

## Debug CUDA

CUDNN_LOGINFO_DBG=1;
CUDNN_LOGDEST_DBG=stdout

# try to work around gpu issues
#import tensorflow as tf
#config = tf.compat.v1.ConfigProto()
#config.gpu_otions.allow_growth = True
#session = tf.compat.v1.InteractiveSession

## Ideas

1. Build Quick Thumbnail gallery of directory to validate work
2. Make python script recursive (I think the recursion needs to be done in the script so we don't have to initial CUDA
   over and over)
3. Write data about images to sql light db, including full_path, hash, is_person_flag
