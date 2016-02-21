[Compile openalpr](https://github.com/openalpr/openalpr/wiki)

LIBRARIES
=========

Install or just copy the following files to alpr/blobs dir (create it):
* libopenalprpy.so.2  ($build/bindings/python/libopenalprpy.so.2)
* libopenalpr.so.2  ($build/openalpr/libopenalpr.so.2)
* libstatedetection.so.2 ($build/statedetection/libstatedetection.so.2)

If you choose to copy openalpr libraries (not install them), remember to set LD_LIBRARY_PATH:

```bash
export LD_LIBRARY_PATH=$src/alpr/blobs:$LD_LIBRARY_PATH
```

CONFIG
=======

Copy openalpr.conf ($build/config/openalpr.conf) to alpr dir

RUNTIME
=======

Copy directory 'runtime_data' to alpr dir

