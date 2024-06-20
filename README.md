도커를 이용한 영화 추천시스템 복습하기

[rocky@localhost movie]$ sudo dnf update
[sudo] rocky의 암호: 
Repository baseos is listed more than once in the configuration
Repository appstream is listed more than once in the configuration
Repository crb is listed more than once in the configuration
Repository extras is listed more than once in the configuration
Repository plus is listed more than once in the configuration
마지막 메타자료 만료확인 22:43:50 이전인: 2024년 06월 18일 (화) 오후 12시 10분 13초.
종속성이 해결되었습니다.
처리가 필요하지 않습니다.
완료되었습니다!
[rocky@localhost movie]$ sudo dnf install docker.io
Repository baseos is listed more than once in the configuration
Repository appstream is listed more than once in the configuration
Repository crb is listed more than once in the configuration
Repository extras is listed more than once in the configuration
Repository plus is listed more than once in the configuration
마지막 메타자료 만료확인 22:44:54 이전인: 2024년 06월 18일 (화) 오후 12시 10분 13초.
일치하는 인수가 없습니다: docker.io
오류: 일치하는 항목을 찾을 수 없습니다: docker.io
[rocky@localhost movie]$ sudo docker --version
[sudo] rocky의 암호: 
Docker version 26.1.4, build 5650f9b
[rocky@localhost movie]$ docker status
docker: 'status' is not a docker command.
See 'docker --help'
[rocky@localhost movie]$ ls
[rocky@localhost movie]$ gedit
[rocky@localhost movie]$ gedit index.html
[rocky@localhost movie]$ gedit
[rocky@localhost movie]$ gedit Dockerfile
[rocky@localhost movie]$ sudo docker build -t my-web-server .
[+] Building 14.3s (7/7) FINISHED                                docker:default
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 369B                                       0.0s
 => [internal] load metadata for docker.io/library/nginx:latest            3.8s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load build context                                          0.0s
 => => transferring context: 228B                                          0.0s
 => [1/2] FROM docker.io/library/nginx:latest@sha256:56b388b0d79c738f4cf  10.0s
 => => resolve docker.io/library/nginx:latest@sha256:56b388b0d79c738f4cf5  0.0s
 => => sha256:56b388b0d79c738f4cf51bbaf184a14fab19337f4 10.27kB / 10.27kB  0.0s
 => => sha256:dca6c1f16ab4ac041e55a10ad840e6609a953e1b2ee 2.29kB / 2.29kB  0.0s
 => => sha256:0b432cb2d95eea3d638db7e7cfb51eb7d7828f87c31d7a8 959B / 959B  0.6s
 => => sha256:dde0cca083bc75a0af14262b1469b5141284b4399a6 7.16kB / 7.16kB  0.0s
 => => sha256:a97f9034bc9b7e813d93db97482046e20f581e1a8 41.83MB / 41.83MB  8.4s
 => => sha256:9571e65a55a3fd4ccd461b4fbaf5e8e38242317add94cb0 627B / 627B  1.1s
 => => sha256:24436676f2decbc5ed11c2e5786faa3dd103bc0fc738a20 398B / 398B  1.3s
 => => sha256:928cc9acedf0354de565f85d9df9d519e44a29a585d 1.21kB / 1.21kB  2.0s
 => => sha256:ca6fb48c6db48342a3905bf65037e97543080a052a5 1.40kB / 1.40kB  2.2s
 => => extracting sha256:a97f9034bc9b7e813d93db97482046e20f581e1a80ddeda9  1.4s
 => => extracting sha256:9571e65a55a3fd4ccd461b4fbaf5e8e38242317add94cb08  0.0s
 => => extracting sha256:0b432cb2d95eea3d638db7e7cfb51eb7d7828f87c31d7a8c  0.0s
 => => extracting sha256:24436676f2decbc5ed11c2e5786faa3dd103bc0fc738a203  0.0s
 => => extracting sha256:928cc9acedf0354de565f85d9df9d519e44a29a585d6c19a  0.0s
 => => extracting sha256:ca6fb48c6db48342a3905bf65037e97543080a052a5f169b  0.0s
 => [2/2] COPY index.html /usr/share/nginx/html                            0.2s
 => exporting to image                                                     0.0s
 => => exporting layers                                                    0.0s
 => => writing image sha256:0bdc9c0c61300a661b7c858d66beeeaf92d271a794bcf  0.0s
 => => naming to docker.io/library/my-web-server                           0.0s
[rocky@localhost movie]$ sudo docker run -d -p 80:80 my-web-server
71e46ea724080dee6a848e9d188dcaf870384fc493c051d2853eae4ec40907fb
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE           COMMAND                   CREATED         STATUS         PORTS                               NAMES
71e46ea72408   my-web-server   "/docker-entrypoint.…"   6 seconds ago   Up 5 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp   trusting_turing
[rocky@localhost movie]$ gedit Dockerfile
[rocky@localhost movie]$ gedit app.py
[rocky@localhost movie]$ gedit requirements.txt
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[sudo] rocky의 암호: 
[+] Building 10.5s (9/9) FINISHED                                docker:default
 => [internal] load build definition from Dockerfile                       0.0s
 => => transferring dockerfile: 448B                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim         3.5s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e35396  2.6s
 => => resolve docker.io/library/python:3.8-slim@sha256:0d83eed55f9e35396  0.0s
 => => sha256:0d83eed55f9e3539656956aacd9732922fd038a9528 1.86kB / 1.86kB  0.0s
 => => sha256:447046401e41b924996004c899f94b070190ee936eb 1.37kB / 1.37kB  0.0s
 => => sha256:c40d5cf308df328cfd2fba85f746392fda2e2963c0d 7.57kB / 7.57kB  0.0s
 => => sha256:ec71c857f19bfca4e0b37b6f175e627e1065e1f3d 11.68MB / 11.68MB  1.6s
 => => sha256:722b4c0d9bb48bd99aea34e948d798db0e330da4abce254 244B / 244B  0.5s
 => => sha256:a7e80e97f197ca39d74e9b3e7d0f667d619835f6cee 3.14MB / 3.14MB  1.3s
 => => extracting sha256:ec71c857f19bfca4e0b37b6f175e627e1065e1f3de34e074  0.5s
 => => extracting sha256:722b4c0d9bb48bd99aea34e948d798db0e330da4abce254f  0.0s
 => => extracting sha256:a7e80e97f197ca39d74e9b3e7d0f667d619835f6cee15c2d  0.3s
 => [internal] load build context                                          0.0s
 => => transferring context: 1.27kB                                        0.0s
 => [2/4] WORKDIR /app                                                     0.1s
 => [3/4] COPY . .                                                         0.0s
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt               3.9s
 => exporting to image                                                     0.2s 
 => => exporting layers                                                    0.2s
 => => writing image sha256:78348a209ee7ade53a41f7406f5990d576728e56ebf58  0.0s
 => => naming to docker.io/library/movie-recommendation                    0.0s
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation
36893bd50d690de12d8d0c87c45963ea7df647a7aa23111d28022b9473a1ad41
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE           COMMAND                   CREATED         STATUS         PORTS                               NAMES
71e46ea72408   my-web-server   "/docker-entrypoint.…"   6 minutes ago   Up 6 minutes   0.0.0.0:80->80/tcp, :::80->80/tcp   trusting_turing
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                         COMMAND                   CREATED          STATUS                      PORTS                               NAMES
36893bd50d69   movie-recommendation          "python app.py"           18 seconds ago   Exited (1) 17 seconds ago                                       beautiful_panini
71e46ea72408   my-web-server                 "/docker-entrypoint.…"   6 minutes ago    Up 6 minutes                0.0.0.0:80->80/tcp, :::80->80/tcp   trusting_turing
94842e81cb74   movie-recommendation-system   "python app/main.py"      16 hours ago     Exited (1) 16 hours ago                                         keen_kepler
[rocky@localhost movie]$ docker stop 71
71
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation
9577a1c1528d75dc271babab67a4f9d95a694821aeb47d92eb901bb265c5a300
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[rocky@localhost movie]$ sudo docker logs ^C
[rocky@localhost movie]$ docker rm 36 71 94
36
71
94
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS                     PORTS     NAMES
9577a1c1528d   movie-recommendation   "python app.py"   3 minutes ago   Exited (1) 3 minutes ago             confident_hofstadter
[rocky@localhost movie]$ docker rm 95
95
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[+] Building 2.0s (9/9) FINISHED                                                                                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                                                                                       0.0s
 => => transferring dockerfile: 448B                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                                                                                         1.9s
 => [internal] load .dockerignore                                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                                            0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1b8438c581bd                                                   0.0s
 => [internal] load build context                                                                                                                                          0.0s
 => => transferring context: 123B                                                                                                                                          0.0s
 => CACHED [2/4] WORKDIR /app                                                                                                                                              0.0s
 => CACHED [3/4] COPY . .                                                                                                                                                  0.0s
 => CACHED [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                                                                        0.0s
 => exporting to image                                                                                                                                                     0.0s
 => => exporting layers                                                                                                                                                    0.0s
 => => writing image sha256:78348a209ee7ade53a41f7406f5990d576728e56ebf58c748cb076e7e5b95520                                                                               0.0s
 => => naming to docker.io/library/movie-recommendation                                                                                                                    0.0s
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation
ca43cc4a4d154e15a850d1bec2aa5a987a51797cb70e48db01678f9a91918d2b
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND           CREATED          STATUS                      PORTS     NAMES
ca43cc4a4d15   movie-recommendation   "python app.py"   17 seconds ago   Exited (1) 15 seconds ago             optimistic_roentgen
[rocky@localhost movie]$ docker ps 
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[rocky@localhost movie]$ docker logs ca
Traceback (most recent call last):
  File "app.py", line 1, in <module>
    from flask import Flask, jsonify
  File "/usr/local/lib/python3.8/site-packages/flask/__init__.py", line 7, in <module>
    from .app import Flask as Flask
  File "/usr/local/lib/python3.8/site-packages/flask/app.py", line 28, in <module>
    from . import cli
  File "/usr/local/lib/python3.8/site-packages/flask/cli.py", line 18, in <module>
    from .helpers import get_debug_flag
  File "/usr/local/lib/python3.8/site-packages/flask/helpers.py", line 16, in <module>
    from werkzeug.urls import url_quote
ImportError: cannot import name 'url_quote' from 'werkzeug.urls' (/usr/local/lib/python3.8/site-packages/werkzeug/urls.py)
[rocky@localhost movie]$ sudo pip install --upgrade Flask Werkzeug
Collecting Flask
  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)
Collecting Werkzeug
  Downloading werkzeug-3.0.3-py3-none-any.whl.metadata (3.7 kB)
Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.9/site-packages (from Flask) (3.1.3)
Collecting itsdangerous>=2.1.2 (from Flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from Flask)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Collecting blinker>=1.6.2 (from Flask)
  Downloading blinker-1.8.2-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.9/site-packages (from Flask) (7.0.2)
Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib64/python3.9/site-packages (from Werkzeug) (2.1.5)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/site-packages (from importlib-metadata>=3.6.0->Flask) (3.18.1)
Downloading flask-3.0.3-py3-none-any.whl (101 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 101.7/101.7 kB 5.3 MB/s eta 0:00:00
Downloading werkzeug-3.0.3-py3-none-any.whl (227 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 227.3/227.3 kB 12.1 MB/s eta 0:00:00
Downloading blinker-1.8.2-py3-none-any.whl (9.5 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 19.5 MB/s eta 0:00:00
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Installing collected packages: Werkzeug, itsdangerous, click, blinker, Flask
  WARNING: The script flask is installed in '/usr/local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Flask-3.0.3 Werkzeug-3.0.3 blinker-1.8.2 click-8.1.7 itsdangerous-2.2.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
[rocky@localhost movie]$ gedit requirements.txt
[rocky@localhost movie]$ sudo pip install --upgrade Flask Werkzeug

Requirement already satisfied: Flask in /usr/local/lib/python3.9/site-packages (3.0.3)
Requirement already satisfied: Werkzeug in /usr/local/lib/python3.9/site-packages (3.0.3)
Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.9/site-packages (from Flask) (3.1.3)
Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.9/site-packages (from Flask) (2.2.0)
Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.9/site-packages (from Flask) (8.1.7)
Requirement already satisfied: blinker>=1.6.2 in /usr/local/lib/python3.9/site-packages (from Flask) (1.8.2)
Requirement already satisfied: importlib-metadata>=3.6.0 in /usr/local/lib/python3.9/site-packages (from Flask) (7.0.2)
Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib64/python3.9/site-packages (from Werkzeug) (2.1.5)
Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.9/site-packages (from importlib-metadata>=3.6.0->Flask) (3.18.1)
^[[AWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
[rocky@localhost movie]$ 
[rocky@localhost movie]$ gedit Dockerfile
[rocky@localhost movie]$ sudo docker build --no-cache -t movie-recommendation .
[+] Building 4.9s (9/9) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 381B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                             0.9s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 72B                                                                               0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => [3/4] COPY requirements.txt requirements.txt                                                               0.0s
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt                                                   3.7s
 => exporting to image                                                                                         0.2s 
 => => exporting layers                                                                                        0.1s 
 => => writing image sha256:df3d63c22148d206a8a24d706a8a7e2091a0798b83c2e593a65509bdc8ef86ca                   0.0s 
 => => naming to docker.io/library/movie-recommendation                                                        0.0s 
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[+] Building 1.9s (9/9) FINISHED                                                                     docker:default 
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 381B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                             1.8s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 37B                                                                               0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => CACHED [3/4] COPY requirements.txt requirements.txt                                                        0.0s
 => CACHED [4/4] RUN pip install --no-cache-dir -r requirements.txt                                            0.0s
 => exporting to image                                                                                         0.0s
 => => exporting layers                                                                                        0.0s
 => => writing image sha256:df3d63c22148d206a8a24d706a8a7e2091a0798b83c2e593a65509bdc8ef86ca                   0.0s
 => => naming to docker.io/library/movie-recommendation                                                        0.0s
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE          COMMAND           CREATED         STATUS                     PORTS     NAMES
ca43cc4a4d15   78348a209ee7   "python app.py"   4 minutes ago   Exited (1) 4 minutes ago             optimistic_roentgen
[rocky@localhost movie]$ docker rm ca
ca
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation
a71668d3e1d79ad385fd2438e7b4e57a0cb16abdcb0a96e5affea99b8d1e6f02
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS                     PORTS     NAMES
a71668d3e1d7   movie-recommendation   "python app.py"   5 seconds ago   Exited (2) 4 seconds ago             happy_diffie
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
[rocky@localhost movie]$ docker logs a71668d3e1d7
python: can't open file 'app.py': [Errno 2] No such file or directory
[rocky@localhost movie]$ ^C
[rocky@localhost movie]$ gedit Dockerfile
[rocky@localhost movie]$ gedit Dockerfile
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS                     PORTS     NAMES
a71668d3e1d7   movie-recommendation   "python app.py"   3 minutes ago   Exited (2) 3 minutes ago             happy_diffie
[rocky@localhost movie]$ docker rm a7
a7
[rocky@localhost movie]$ docker image

Usage:  docker image COMMAND

Manage images

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Download an image from a registry
  push        Upload an image to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[+] Building 8.6s (9/9) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 434B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                             3.8s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 1.44kB                                                                            0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => [3/4] COPY . .                                                                                             0.1s
 => [4/4] RUN pip install --no-cache-dir Flask                                                                 4.5s
 => exporting to image                                                                                         0.2s 
 => => exporting layers                                                                                        0.2s 
 => => writing image sha256:75e2f00b71b1260c6a86e0a59414f0c3f6809ba30d249988dae035463c8bab6c                   0.0s 
 => => naming to docker.io/library/movie-recommendation                                                        0.0s 
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation                                       
4fa8d7dc6ff8c4056f71f794559f3bf26bf8aaefc40504abb2a0a74cc0fa7bc3                                                    
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS         PORTS                                       NAMES
4fa8d7dc6ff8   movie-recommendation   "python app.py"   4 seconds ago   Up 3 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   frosty_euler
[rocky@localhost movie]$ gedit app.py
[rocky@localhost movie]$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS         PORTS                                       NAMES
4fa8d7dc6ff8   movie-recommendation   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   frosty_euler
[rocky@localhost movie]$ docker stop 4f
4f
[rocky@localhost movie]$ docker rm 4f
4f
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[+] Building 5.2s (9/9) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 434B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                             0.9s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 611B                                                                              0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => [3/4] COPY . .                                                                                             0.0s
 => [4/4] RUN pip install --no-cache-dir Flask                                                                 4.0s
 => exporting to image                                                                                         0.2s 
 => => exporting layers                                                                                        0.2s 
 => => writing image sha256:23b9e68e0578fbb7ded66f33f97753b2604f6cf9f4890466e1758abbf155949d                   0.0s 
 => => naming to docker.io/library/movie-recommendation                                                        0.0s 
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation                                       
339862a4086527dc1f809d9efdfbb701e054acbd42834f1e7b6107f6b89b3864                                                    
[rocky@localhost movie]$ docker ps
CONTAINER ID   IMAGE                  COMMAND           CREATED         STATUS         PORTS                                       NAMES
339862a40865   movie-recommendation   "python app.py"   6 seconds ago   Up 5 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   bold_mclaren
[rocky@localhost movie]$ docker stop 33
33
[rocky@localhost movie]$ docker rm 33
33
[rocky@localhost movie]$ gedit app.py
[rocky@localhost movie]$ sudo docker build -t movie-recommendation .
[sudo] rocky의 암호: 
[+] Building 6.3s (9/9) FINISHED                                                                     docker:default
 => [internal] load build definition from Dockerfile                                                           0.0s
 => => transferring dockerfile: 434B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.8-slim                                             1.8s
 => [internal] load .dockerignore                                                                              0.0s
 => => transferring context: 2B                                                                                0.0s
 => [1/4] FROM docker.io/library/python:3.8-slim@sha256:0d83eed55f9e3539656956aacd9732922fd038a95281a4ddd3ec1  0.0s
 => [internal] load build context                                                                              0.0s
 => => transferring context: 970B                                                                              0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => [3/4] COPY . .                                                                                             0.0s
 => [4/4] RUN pip install --no-cache-dir Flask                                                                 4.2s
 => exporting to image                                                                                         0.2s 
 => => exporting layers                                                                                        0.2s 
 => => writing image sha256:61bc3dfbab72bc6ac0ddc9d63573e1fdc933058404ddb57e0b60425fe461c3da                   0.0s 
 => => naming to docker.io/library/movie-recommendation                                                        0.0s 
[rocky@localhost movie]$ sudo docker run -d -p 5000:5000 movie-recommendation
6621e4958b6cc075f69ab721006f525cb46d90449adc43eaa816580741752439 

