Is Pic With Person
-------------------------

A simple python script that answers the question: does this pic have a person in it?

The idea is to build out tools to indetify and catelog all the images on my computer with people in them.

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
