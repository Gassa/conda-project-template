# conda-project-template

## How to build base image

## How to generate executable

## Run a Jupyter session with all dependencies

```
docker run --rm -p 18888:8888 conda-template \
    jupyter notebook --notebook-dir=/opt/app \
    --ip=0.0.0.0 --port=8888 --allow-root --no-browser
```

## Reference
* [tini](https://ahmet.im/blog/minimal-init-process-for-containers/)
* [Dask docker image](https://github.com/dask/dask-docker)
* [Smaller Docker images with Conda](https://github.com/dask/dask-docker)
* [Chooseing an init process for multi-process containers](https://ahmet.im/blog/minimal-init-process-for-containers)