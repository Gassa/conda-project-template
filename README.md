# conda-project-template

## How to build base image

## How to generate executable

## Run a Jupyter session with all dependencies

```
docker run --rm -p 18888:8888 conda-template \
    jupyter notebook --notebook-dir=/opt/app \
    --ip=0.0.0.0 --port=8888 --allow-root --no-browser
```

## Docker environmental variables

If `environment.yml` exists, the image will install all dependencies in the environment.



|environment vaiables|default value|
|--------------------|-------------|
| EXTRA_APT_PACKAGES |     Nil     |
|EXTRA_CONDA_PACKAGES|     Nil     |
| EXTRA_PIP_PACKAGES |     Nil     |

## Reference
* [tini](https://ahmet.im/blog/minimal-init-process-for-containers/)
* [Dask docker image](https://github.com/dask/dask-docker)
* [Smaller Docker images with Conda](https://github.com/dask/dask-docker)
* [Chooseing an init process for multi-process containers](https://ahmet.im/blog/minimal-init-process-for-containers)