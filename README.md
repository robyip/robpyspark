# robpyspark

This Docker image was created so I could learn Python and pyspark primarily
Also, I wanted to learn how to create a docker image

The folder code is used to store python scripts and test data

This is the command to build the docker image:

	docker build -t robpyspark:latest .

This is the docker run command to instantiate the docker container
setup a volume to the code folder
And then run the Python pyspark script from the mapped volume

docker run --rm -v $(pwd)/code:/app/code robpyspark:latest \
python /app/code/rob-pyspark.py
