# master_mind
A *mastermind* game in python

## Install instructions

It is assumed you have any working version of docker available.
If not, please visit https://docs.docker.com/get-started/get-docker/.

1. In the same directory as the source, run 'docker build -t pyth_ubu --build-arg debug=[REPLACE WITH OWN DEBUG PASS] .'
<br>
<br>
2. Then in the directory above it, run 'docker run -dt --mount type=bind,src=./[REPLACE WITH SOURCE DIR NAME],dst=/usr/games/master_mind --name master_mind pyth_ubu'
<br>
<br>
3. After initialising the container, you can run 'docker exec -it master_mind /bin/bash' to enter the container's shell
<br>
<br>
4. Navigate to the source dir with 'cd /usr/games/master_mind'
<br>
<br>
5. Now you can play the game by running 'python3 master_mind.py'


# Good Luck!


